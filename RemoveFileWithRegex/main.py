import os
import re

# Get the Inputs from the User
FILE_PATH = input("Enter the File Path: ")
FILE_PATTERN = input("Enter the File Pattern: ")
PATTERN_FILE_STATUS = int(input("You want to Keep (0) or Remove(1) Pattern File: "))

def RemoveFileWithPattern(PATH):
    # Get the list of Files from provided path
    listDir = os.listdir(PATH)


    # Loop through the list
    for listFile in listDir:
        # Check the file or directory
        isFile = re.search("\.[a-zA-Z0-9]+$", listFile)


        # when list item is directory
        if not isFile:

            # Goes to inner directory
            RemoveFileWithPattern(f"{PATH}/{listFile}")

            # skip the current loop
            continue

        # Match the file with user pattern
        isPatternedFile = bool(re.search(FILE_PATTERN, listFile))

        """
        Cases:
            Case 1: File Matched & Keep == true (0)
                Remove the matched files only

            Case 2: File Matched & Keep == false (1)
                Remove the non match files only
        """
        if isPatternedFile == PATTERN_FILE_STATUS:
            os.remove(f"{PATH}/{listFile}")

RemoveFileWithPattern(FILE_PATH)