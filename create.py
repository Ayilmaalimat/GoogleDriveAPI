from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

my_folders = ['First-folder', 'Second-folder', 'Third-folder']

for folders in my_folders:
    file_metadata = {
        'name': folders,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    service.files().create(body=file_metadata).execute()
