from GoogleAPI import GoogleAPI

google = GoogleAPI()

# google.create(["my_folders"])
# google.create(['name']) get a list with a name


# google.upload('1UZATbBRNVAq547uEc-Ep1IFa0v5NU-HM', [
#               'd7da75accefe0e3b445d3cd078429b074d9cd7a5.jpg', 'upload.csv', 'fdafs.csv', 'fasdfas.html'], ['image/jpeg', 'text/csv', 'text/csv', 'text/html'])
# google.upload() 1 argument - id of the folder, 2 argument - list of the names, 3 argument - list of the mime types https://learndataanalysis.org/commonly-used-mime-types/


# google.download(['12-ZygtZbKP-K4-bm2PGB8LTJmpxaTPLr',
#                  '1cAeSWgkogytW_v-qT_TRapILB2uAPfgU'], ['photo.jpeg', 'test.csv'])
# google.download() 1 argument - list of the ids of the items, 2 argument - list with the names of the files with extensions


# google.copy('1rDd56cUcJkicyathIjx7M8UGVT-wd_-KcY-FjnqgjGk',
#             ['10pumJciJBybm18vRBozFoOSIahVWvex9', '1rVNBk2oTNDGruCJFFmSLoY1TiXs6aAP1'])
# google.copy() 1 argument - id of the file, 2 argument - list of the file's ids where you want to copy

google.info('1UZATbBRNVAq547uEc-Ep1IFa0v5NU-HM')
# google.info('id') show info about file
# google.info('id') 1 argument - id of the folder,
