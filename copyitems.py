from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_id = '1-rptMfaX5TFupgSRFPJwDAd1omrHHqdwdRajmBzeh18'
folder_ids = ['1YGT58sh_6YlmDGKFTOU_3DuWQccGgolh',
              '1N_VSS0LIvP4jRgfrpkTeFFFdnWBn3DSo',
              '1Sg4FKu238lOl8y-kkHG_QaejUNW_KLdh']


for folder_id in folder_ids:
    file_metadata = {
        'name': 'Тестовый документ',
        'parents': [folder_id],
        'starred': True,
        'description': 'Первый тестовый документ'
    }

    service.files().copy(
        fileId=file_id,
        body=file_metadata
    ).execute()
