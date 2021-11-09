from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.reed.co.uk/jobs/python-jobs").text
soup = BeautifulSoup(html_text, "lxml")

#scraping just the first card of the webpage
job = soup.find("article", class_="job-result")



title = job.find("h3", class_="title").text.replace("\n", "")
company_name = job.find(class_="posted-by").a.text
company= job.find("div", class_="posted-by").text
company = company.strip()
company = company.split("by")
company[0] = company[0][7:]


metadata = job.find("div", class_="metadata")
salary = metadata.find("li", class_="salary").text
location = metadata.find("span").text
time = metadata.find("li", class_="time").text

long_description = job.find(class_="description").p.text

result = f"""
	Date Posted: {company[0]}
	company: {company_name}
	Job Title: {title}
	Salary: {salary}
	Location: {location}
	Time:: {time}
	Description: {long_description}
"""




print(result)