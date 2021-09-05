import csv

def save_to_file(word, jobs):
	file = open(f"{word}-jobs.csv", mode="w")
	writer = csv.writer(file)
	writer.writerow(["title", "company", "location", "link"])

	for job in jobs:
		writer.writerow(list(job.values()))
		# print(list(job.values()))
	# print(jobs)
	return