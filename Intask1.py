# get any file with extension
# display only that extension
# check file extension. if mp3, print(not allowed)

import os

file = input("Enter file name with extension: ")
file_name, file_extension = os.path.splitext(file)
print(f'File name is {file_name}')
print(f'File extension is {file_extension}')

if file_extension == '.mp3':
	print('This file is not allowed')
else:
	print('Proceed to upload')