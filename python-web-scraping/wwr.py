from typing import Text
import requests
from bs4 import BeautifulSoup

# "title" "company" "location" "apply_link"
def extract_job(html):
	# print(html, "\n\n")
	title = html.find("span", class_="title").get_text()
	company = html.find("span", class_="region company").get_text()
	location = html.find("span", class_="company").get_text()
	link = html.find("a", recursive=False)["href"]
	if not title or not company or not location or not link:
		return
	return {
		"title": title,
		"company": company,
		"location": location,
		"apply_link": f"https://weworkremotely.com{link}",
	}


def	extract_job_categories(url):
	jobs = []
	result = requests.get(url)
	print(result.url)
	print(f"scrapping WWR....")
	soup = BeautifulSoup(result.text, "html.parser")
	job_categories = soup.find("div", id="job_list").find_all("section", class_="jobs")
	for job_categorie in job_categories:
		job_list = job_categorie.find("ul").find_all("li", class_="feature")
		for job in job_list:
			result = extract_job(job)
			if result:
				jobs.append(result)
	return jobs

def	get_wwr_jobs(word):
	url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
	jobs = extract_job_categories(url)
	return jobs