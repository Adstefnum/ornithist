import csv
from appwrite.client import Client
from appwrite.services.databases import Databases
from dotenv import load_dotenv
import os
import uuid
import secrets
import string

load_dotenv()
endpoint = os.environ.get('APPWRITE_ENDPOINT')
project_id = os.environ.get('APPWRITE_PROJECT_ID')
database_id = os.environ.get('APPWRITE_DATABASE_ID')
collection_id = os.environ.get('APPWRITE_COLLECTION_ID')
secret_key = os.environ.get('APPWRITE_SECRET_KEY')
# Initialize the Appwrite client
client = Client()
client.set_endpoint(endpoint) 
client.set_project(project_id) 
client.set_key(secret_key)

# Initialize the Appwrite database service
db = Databases(client)
db.get_collection(database_id, collection_id) 

csv_file_path = './output_with_images.csv'

failures = open('failures.txt', 'w')

def generate_random_id(length):
    alphabet = string.ascii_letters + string.digits
    random_id = ''.join(secrets.choice(alphabet) for _ in range(length))
    return random_id

def prepare_data(row):
    bird_name = row[bird_name_index]
    wiki_url = row[wiki_url_index]
    image_link = row[image_link_index]
    
    data = {
        'bird_name': bird_name,
        'wiki_url': wiki_url,
        'image_link': image_link
    }

    return data
 

def upload_to_appwrite(data):
    document_id = generate_random_id(10)
    try:
        response = db.create_document(database_id,collection_id,document_id,data)
        print(f"Uploaded data for '{data['bird_name']}' - Document ID: {response['$id']}")
    except:
        failures.write(f"Failed to upload data for '{data['bird_name']}'")

with open(csv_file_path, 'r',encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Read the header row

    # Get the index of the required fields
    bird_name_index = headers.index('name')
    wiki_url_index = headers.index('wikipedia_link')
    image_link_index = headers.index('image_link')
    for row in reader:
        data = prepare_data(row)
        upload_to_appwrite(data)
    
    
    failures.close()


    



