from google.cloud import scheduler

# Create a Cloud Scheduler client
client = scheduler.Client()

# Create a new job
job = client.create_job(name='fetch_jobs_data_engineer', body={
    'schedule': '* 6 * * *',
    'time_zone': 'UTC',
    'http_target': {
        'uri': 'https://mysite.com/scraper', # this is a just sample for uri it will differ
        'http_method': 'POST'
    }
})
