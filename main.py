from bs4 import BeautifulSoup
import requests
import time


def find_jobs():

	html_text = requests.get("https://www.reed.co.uk/jobs/python-jobs").text
	soup = BeautifulSoup(html_text, "lxml")
	jobs = soup.find_all("article", class_="job-result")

	for index, job in enumerate(jobs):
		with open(f"job_posts/{index}.txt", "w") as f:
			title = job.find("h3", class_="title").text.replace("\n", "")
			company_name = job.find(class_="posted-by").a.text
			company = job.find("div", class_="posted-by").text
			company = company.strip()
			company = company.split("by")
			company[0] = company[0][7:]

			metadata = job.find("div", class_="metadata")
			salary = metadata.find("li", class_="salary").text
			location = metadata.find("span").text
			time = metadata.find("li", class_="time").text
			description = job.find(class_="description").p.text

			remote = metadata.text
			if "Work from home" in remote:
				work_remotely = "Yes"
			else:
				work_remotely = "No"

			more_info = job.header.h3.a["href"]

			result = f"""
				Date Posted: {company[0]}
				company: {company_name}
				Job Title: {title}
				Salary: {salary}
				Location: {location}
				Time: {time}
				Work from home: {work_remotely}
				Description: {description}
				More info: {more_info}
			"""
			f.write(result)
			print(f"file {index} saved")

if __name__ == "__main__":
	while True:
		find_jobs()
		time_wait = 10
		time.sleep(time_wait*60)
		print(f"waiting {time_wait} minutes")
