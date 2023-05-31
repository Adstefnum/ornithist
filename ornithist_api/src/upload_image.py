from flask import Flask, request, jsonify
import base64
import os
from appwrite.client import Client
from appwrite.services.storage import Storage
from dotenv import load_dotenv
from appwrite.input_file import InputFile
import string
import random

app = Flask(__name__)

load_dotenv()
endpoint = os.environ.get('APPWRITE_ENDPOINT')
project_id = os.environ.get('APPWRITE_PROJECT_ID')
database_id = os.environ.get('APPWRITE_DATABASE_ID')
collection_id = os.environ.get('APPWRITE_COLLECTION_ID')
secret_key = os.environ.get('APPWRITE_SECRET_KEY')
bucket_id = os.environ.get('APPWRITE_BUCKET_ID')

client = Client()
client.set_endpoint(endpoint) 
client.set_project(project_id) 
client.set_key(secret_key)



# Initialize the Appwrite storage service
storage = Storage(client)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        image_data = request.form.get('imageData')  # Get the base64 image data from the request
        file_id = generate_file_id()
        image_bytes = base64.b64decode(image_data)

        file = storage.create_file(bucket_id, file_id, InputFile.from_bytes(image_bytes))
        

        return jsonify({'fileId': file['$id']})  # Return the ID of the uploaded file
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def generate_file_id():
    chars = string.ascii_letters + string.digits + '._-' 
    return ''.join(random.choices(chars, k=32))
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
