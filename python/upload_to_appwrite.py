import requests

# Replace with your Appwrite endpoint and project ID
ENDPOINT = 'https://appwrite.example.com/v1'
PROJECT_ID = 'your-project-id'

# Replace with your Appwrite API key
API_KEY = 'your-api-key'

# Set up headers
headers = {
    'Content-Type': 'application/json',
    'X-Appwrite-Project': PROJECT_ID,
    'X-Appwrite-Key': API_KEY,
}

# Replace with the path and filename for your CSV file
csv_file = 'data.csv'

# Replace with the appropriate field names for your data
fieldnames = ['bird_name','wiki_url','image_link', 'desc']

# Create the CSV file and writer object
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

for record in processed_data:
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(record)

    # Upload record to the Appwrite database

    payload = {
        'name': record['name'],
        'description': record['description'],
        'field3': record['field3'],
        'field4': record['field4'],
        # Include additional fields as needed
    }

    response = requests.post(f'{ENDPOINT}/database/collections/<your-collection-id>/documents', headers=headers, json=payload)

    if response.status_code == 201:
        print('Record created successfully')
    else:
        print('Failed to create record:', response.json())
