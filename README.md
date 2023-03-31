# Job Listing GCP Scheduler BigQuery
This repository contains code for scraping job listings from various websites and storing the data in BigQuery using the Google Cloud Platform (GCP) Scheduler. The code consists of three Python scripts: scraper.py, scheduler.py, and server.py, and a requirements.txt file listing the required Python packages.

## Getting Started
To get started, you will need to set up a GCP account and create a project. You will also need to create a BigQuery dataset and table to store the scraped data. The scheduler.py script uses GCP Scheduler to run the scraper.py script at regular intervals, so you will also need to set up a Scheduler job.

## Prerequisites
I have done this project in my GCP, I didn't added any code for authorization with client services, Please add as contribution to this project or you can search it out on internt.

To run the scripts, you will need to install the required Python packages listed in the requirements.txt file. You can install the packages using pip:

`pip install -r requirements.txt`

You will also need to set up authentication for your GCP project. You can follow the instructions in the GCP documentation to set up authentication.

## Scripts

- scraper.py

The scraper.py script scrapes job listings from various websites and stores the data in a BigQuery table. 


- scheduler.py

The scheduler.py script sets up a Scheduler job to run the scraper.py script at regular intervals. To run the script, you will need to provide the following arguments:

--project: the ID of your GCP project
--name: the name of your Scheduler job
--dataset: the ID of your BigQuery dataset
--table: the ID of your BigQuery table
--interval: the interval at which to run the job, in cron format


- server.py

The server.py script sets up a Flask web server to serve the scraped job listings. To run the script, you will need to provide the following arguments:

--project: the ID of your GCP project
--dataset: the ID of your BigQuery dataset
--table: the ID of your BigQuery table

## Contributing
Contributions to this repository are welcome. If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request.
