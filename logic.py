from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
import os
import mimetypes
import io

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def create(names):
    my_folders = names

    for folders in my_folders:
        file_metadata = {
            'name': folders,
            'mimeType': 'application/vnd.google-apps.folder'
        }

    service.files().create(body=file_metadata).execute()


def download(ids_of_the_items, names_of_the_items):
    file_ids = ids_of_the_items

    file_names = names_of_the_items

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


def upload(folder_id, file_names, mime_types):
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


def copy_items(file_id, folder_ids):

    for folder_id in folder_ids:
        file_metadata = {
            'name': 'Тестовая таблица',
            'parents': [folder_id],
            'starred': True,
            'description': 'Первая тестовая таблица'
        }

        service.files().copy(
            fileId=file_id,
            body=file_metadata
        ).execute()
