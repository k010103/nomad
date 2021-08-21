from logging import error, exception
from flask import Flask, render_template, request, redirect, send_file
from so import get_so_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def	home():
	return render_template("index.html")


@app.route("/report")
def report():
	word = request.args.get("word")
	if word:
		word = word.lower()
		existing_jobs = db.get(word)
		if existing_jobs:
			jobs = existing_jobs
		else:
			jobs = get_so_jobs(word)
			db[word] = jobs
	else:
		return render_template("/")
	return render_template(
		"report.html", 
		SearchingBy = word,
		resultsNumber = len(jobs),
		jobs = jobs,
	)


@app.route("/export")
def	export():
	try:
		word = request.args.get('word')
		if not word:
			raise exception()
		word = word.lower()
		jobs = db.get(word)
		if not jobs:
			raise exception()
		save_to_file(word, jobs)
		return send_file(f"{word}-jobs.csv")
	except:
		return redirect("/")

app.run()