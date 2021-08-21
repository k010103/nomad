import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", class_="pagination")

    links = pagination('a')
    spans = []

    for page in links[:-1]:
        spans.append(int(page.string))

    max_page = spans[-1]
    return (max_page)

def extract_job(html):
    jobTitle = html.find("h2", class_="jobTitle").find("span", title=True).string
    company = html.find("span", class_="companyName")
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.select_one("pre > div").text
    job_id = html["data-jk"]
    # print(job_id)
    return {
        "title": jobTitle, 
        "company": company, 
        "location":location, 
        "link":f"https://www.indeed.com/jobs?as_and=python&limit=50start%3D0&vjk={job_id}"
        }


def extract_jobs(max_page):
    jobs = []
    # print(f"{URL}start={0 * LIMIT}")
    for page in range(max_page):
        print(f"scrapping indeed: page {page}")
        result = requests.get(f"{URL}start={page * LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup("a", class_="fs-unmask")
        # print(results)
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
