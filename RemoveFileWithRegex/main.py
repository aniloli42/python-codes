import os
import re

# Replace the PASTE_HERE_YOUR_FILE_PATH with your file path
FILE_PATH = "PASTE_HERE_YOUR_FILE_PATH"

fileList = os.listdir(FILE_PATH)

for file in fileList:
    fileName = file

    # main line which helps to match the file
    isMatched = re.search("Copy", fileName)

    # if match with our codition then
    if isMatched:
        # delete the file through this line
        os.remove(FILE_PATH + "/" + fileName)
