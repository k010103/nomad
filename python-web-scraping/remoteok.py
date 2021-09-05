import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}


# "title" "company" "location" "apply_link"
def extract_job(html):
	title = html.find("h2", itemprop="title")
	company = html.find("h3", itemprop="name")
	location = html.find("div", class_="location tooltip", title=True)
	link = html.find("a", itemprop="url", class_="preventLink")
	if title:
		title = title.get_text()
	if company:
		company = company.get_text()
	if location:
		location = location.get_text()
	if link:
		link = link["href"]
	if not title or not company or not location or not link:
		return
	return {
		"title": title,
		"company": company,
		"location": location,
		"apply_link": f"https://remoteok.io{link}",
	}


# td class="company position company_and_position"
def extract_jobs(url):
	jobs = []
	result = requests.get(url, headers=headers)
	print(result.url)
	print(f"scrapping REMOTEOK....")
	soup = BeautifulSoup(result.text, "html.parser")
	try:
		job_list = soup.find("table", id="jobsboard").find_all("td", class_="company position company_and_position")
	except:
		return []
	for job in job_list:
		result = extract_job(job)
		if result:
			jobs.append(result)
	return jobs


def	get_remoteok_jobs(word):
	url = f"https://remoteok.io/remote-{word}-jobs"
	jobs = extract_jobs(url)
	return jobs