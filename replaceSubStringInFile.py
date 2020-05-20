import os
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove, path

# https://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python

FOLDER_PATH = '/home/grigoriy/Desktop/mask_dataset/'

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)
    
for filename in os.listdir(FOLDER_PATH):		
	if '.txt' in filename:
		replace(path.join(FOLDER_PATH, filename), pattern = '2 ', subst = '0 ')
