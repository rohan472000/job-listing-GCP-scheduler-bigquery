from bs4 import BeautifulSoup
import requests

# Fetch the job listings from the website
response = requests.get('https://www.jobboard.com/jobs/data-engineer')
html = response.text

# Parse the HTML to extract the job data using bs4(BeautifulSoup)
soup = BeautifulSoup(html, 'html.parser')
jobs = []
for div in soup.find_all('div', class_='job-listing'):
    title = div.find('h2').text
    company = div.find('h3').text
    location = div.find('span', class_='location').text
    jobs.append({'title': title, 'company': company, 'location': location})

# Send the job data to the server
requests.post('https://mysite.com/save_jobs', json=jobs)

