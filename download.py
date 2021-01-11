from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload
import os
import io

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_ids = ['1lxEDhr_U80nDXME8nNoT_O4QlkaJ2tLO',
            '1a7zaAWW_RAxA42qCVhNDoQmwwiGCil8p']
file_names = ['photo.jpeg', 'test.csv']

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False
    while not done:
        status, done = downloader.next_chunk()
        print('Download progress {}'.format(status.progress() * 100))

    fh.seek(0)

    with open(os.path.join('./downloaded', file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
