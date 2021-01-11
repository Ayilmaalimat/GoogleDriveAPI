from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1YGT58sh_6YlmDGKFTOU_3DuWQccGgolh'

file_names = ['d7da75accefe0e3b445d3cd078429b074d9cd7a5.jpg', 'upload.csv']
mime_types = ['image/jpeg', 'text/csv']

for file, mime_type in zip(file_names, mime_types):
    file_metadata = {
        'name': file,
        'parents': [folder_id],

    }

    media = MediaFileUpload(
        './uploadfiles/{0}'.format(file), mimetype=mime_type)

    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id',
    ).execute()
