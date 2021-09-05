import requests
from bs4 import BeautifulSoup

# URL = f"https://stackoverflow.com/jobs?q=python"
# headers = {"User-Agent" : 자신의 Agent(운영체제와 브라우저)에 대한 정보}

# response = requests.get(URL,headers=headers)


def	get_last_page(url):
	result = requests.get(url)
	# print(result.url)
	soup = BeautifulSoup(result.text, "html.parser")
	try:
		pages = soup.find("div", class_="s-pagination").find_all("a")
		last_page = pages[-2].get_text(strip=True)
		return int(last_page)
	except:
		return 1


def extract_job(html):
	title = html.find("h2", class_="mb4").find("a")["title"]
	company, location = html.find("h3", class_="mb4").find_all("span", recursive=False)
	company = company.get_text(strip=True)
	location = location.get_text(strip=True)
	job_id = html["data-jobid"]
	# print(company, location)
	return {
		"title": title,
		"company": company,
		"location": location,
		"apply_link": f"https://stackoverflow.com/jobs/{job_id}"
	}

def extract_jobs(last_page, url):
	jobs = []
	print(url)
	for page in range(last_page):
		result = requests.get(f"{url}&pg={page + 1}")
		print(f"scrapping so: page {page}")
		soup = BeautifulSoup(result.text, "html.parser")
		results = soup("div", {"class":"-job"})
		for result in results:
			job = extract_job(result)
			jobs.append(job)
	return jobs


def get_so_jobs(word):
	url = f"https://stackoverflow.com/jobs?q={word}"
	last_page = get_last_page(url)
	if last_page == 0:
		return []
	jobs = extract_jobs(last_page, url)
	return jobs