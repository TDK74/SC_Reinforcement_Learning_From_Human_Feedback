import google.cloud.aiplatform as aiplatform
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials


## ------------------------------------------------------ ##
key_path = 'your_key.json'

## ------------------------------------------------------ ##
credentials = Credentials.from_service_account_file(
                key_path,
                scopes = ['https://www.googleapis.com/auth/cloud-platform'])

if credentials.expired:
    credentials.refresh(Request())

## ------------------------------------------------------ ##
PROJECT_ID = 'your_project_ID'
REGION = 'us-central1'

## ------------------------------------------------------ ##
aiplatform.init(project = PROJECT_ID, location = REGION, credentials = credentials)
