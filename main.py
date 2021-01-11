from logic import create, download, upload, copy_items

# create(['mysecond'])
""" function "create" require the list of names """


#download(['1JDi1oi3Rl-yaAEfCvFiQSJ0lR1qD7L5L','1ypw09y9AzREo8RNwuVfoFGfJGKVIDZKH'], ['photo.jpeg', 'test.csv'])

"""
    function 'download' get two lists. 
    first list contains ids_of_the_items, 
    second list contains names_of_the_items with its file extension
"""

# upload('1pcPaSvzgJBgHnSVe-nUymyNQNFlg6Fqw',
#        ['d7da75accefe0e3b445d3cd078429b074d9cd7a5.jpg', 'upload.csv'], ['image/jpeg', 'text/csv'])

"""
    fucntion 'upload' uploads file on google discs
    first argument should be the id of the folder where you want to upload the files
    second argument is a list of the names with extensions of the files that you want to upload
    third argument is also the list but with the mime types of the file ( you can find it on https://learndataanalysis.org/commonly-used-mime-types/)
"""

# #copy_items('13wwrXV-RyDB6pEyaJ5Q6iXNB1vZhMy4hGpYKsFO5ufQ',
#            ['1pcPaSvzgJBgHnSVe-nUymyNQNFlg6Fqw', '1SYEfS-aqb6AaTu2a-r0F3x5NVe02OYWz'])

"""
    function 'copy_items' copy files
    first argument get an id of the file you want to copy
    second argument get a list of file's ids where you want to copy
"""
