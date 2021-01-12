from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
import os
import mimetypes
import io
import pandas as pd
import schedule
import time
import threading


CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


class GoogleAPI():
    def create(self, my_folders):
        for folders in my_folders:
            file_metadata = {
                'name': folders,
                'mimeType': 'application/vnd.google-apps.folder'
            }

        service.files().create(body=file_metadata).execute()

    def delete(self, file_id):
        try:
            service.files().delete(fileId=file_id).execute()
        except:
            print('File not found')

    def download(self, file_ids, file_names):

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

    def upload(self, folder_id, file_names, mime_types):
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

    def copy(self, file_id, folder_ids):
        for folder_id in folder_ids:
            file_metadata = {
                'parents': [folder_id],
                'starred': True
            }

            service.files().copy(
                fileId=file_id,
                body=file_metadata
            ).execute()

    def info(self, folder_id):
        query = "parents = '{}'".format(folder_id)

        response = service.files().list(q=query).execute()
        files = response.get('files')
        nextPageToken = response.get('nextPageToken')

        while nextPageToken:
            response = service.files().list(q=query).execute()
            files.extend(response.get('files'))
            nextPageToken = response.get('nextPageToken')

        df = pd.DataFrame(files)
        print(df)

    def move(self, from_folder, to_folder):
        query = "parents = '{}'".format(from_folder)

        response = service.files().list(q=query).execute()
        files = response.get('files')
        nextPageToken = response.get('nextPageToken')

        while nextPageToken:
            response = service.files().list(q=query, pageToken=nextPageToken).execute()
            files.extend(response.get('files'))
            nextPageToken = response.get('nextPageToken')

        for x in files:
            if x['mimeType'] != 'application/vnd.google-apps.folder':
                service.files().update(
                    fileId=x.get('id'),
                    addParents=to_folder,
                    removeParents=from_folder
                ).execute()

    def __downloadAll(self):
        driveQuery = "(mimeType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or " \
            " mimeType = 'text/csv' or mimeType = 'application/pdf' or mimeType = 'image/jpeg' or mimeType = 'text/html')"

        driveQuery = driveQuery + ' and ' "trashed = false and 'me' in owners "

        fieldsString = 'files(id, mimeType, parents, name)'

        response = service.files().list(
            pageSize=1000,
            q=driveQuery,
            fields=fieldsString
        ).execute()

        lstFiles = response['files']
        nextPageToken = response.get('nextPageToken')

        while nextPageToken:
            response = service.files().list(
                pageSize=1000,
                q=driveQuery,
                fields=fieldsString,
                pageToken=nextPageToken
            ).execute()

            lstFiles.extend(response['files'])
            nextPageToken = response.get('nextPageToken')

        for item in lstFiles:
            if not item['name'].startswith('~$'):
                request = service.files().get_media(fileId=item['id'])

                fh = io.BytesIO()
                downloader = MediaIoBaseDownload(fh, request)

                done = False
                while not done:
                    status, done = downloader.next_chunk()
                    print('Download progress {0:.0%}'.format(
                        int(status.progress())))

                fh.seek(0)
                file_name = item['name']

                with open(os.path.join('./backups', file_name), 'wb') as f:
                    f.write(fh.read())
                    f.close()
        print('finished')

    def __thread(self, time_in_sec):
        schedule.every(time_in_sec).seconds.do(self.__downloadAll)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def backup(self, time_in_sec):
        my_thread = threading.Thread(target=self.__thread(time_in_sec))
        my_thread.start()
