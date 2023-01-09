from google.cloud import bigquery


def save_jobs(request):
    # Extract the job data from the request
    request_json = request.get_json()
    jobs = request_json['jobs']

    # Create a BigQuery client
    client = bigquery.Client()

    # Create a new dataset
    dataset = bigquery.Dataset(client.dataset('job_data'))
    dataset.location = 'US'
    dataset = client.create_dataset(dataset)

    # Create a new table in the dataset
    table = bigquery.Table(dataset.table('job_listings_jobboard'), schema=[
        bigquery.SchemaField('Title', 'STRING'),
        bigquery.SchemaField('Company', 'STRING'),
        bigquery.SchemaField('Location', 'STRING')
    ])
    table = client.create_table(table)

    # Load the data into the table
    errors = client.insert_rows(table, rows=jobs)
    if errors:
        print(errors)
