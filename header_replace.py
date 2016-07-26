""" The following Python 2.7 script is designed to update the headers
of Test Case text documents. The script will only affect text files 
that begin with 'TC'.

NOTE:
    Any Test Case file that does not have a 'REQUIREMENTS' section
    will not be updated by this script. Anytime this is the case
    an ERROR is printed.

TO RUN:
    Create a text document named 'header.txt' in the same directory as
    this script. The header.txt document is where the new header should
    be written, as it will replace the contents of the current headers
    in the TC documents.
    
    Run the script using python 2.7 and select the root directory from
    the pop up window. The script will traverse the root directory and
    all subdirectories beneath it to modify the headers.
"""

__author__  = "Zachary Hill"
__email__   = "zachary.hill@psware.com"

import os # needed for the os.walk function
from Tkinter import Tk
from tkFileDialog import askdirectory
headerFile = './header.txt'


def find_require_ln(fileName):
    """Method to find the line number of the location of 'REQUIREMENTS'
    in the text documents
    
    If no 'REQUIREMENTS' is found will return -1, otherwise returns line number
    """
    
    with open(fileName, 'r') as file:
        for num, line in enumerate(file, 1):
            if 'REQUIREMENTS' in line.upper():
                return num
        return -1 # if here no requirements found
    
    return

    
def replace_header(fileName):
    """Method to remove the old header and replace it with the new.
    
    The old header will start at the beginning of the file and
    go until the word 'REQUIREMENTS' (case insensitive)
    
    The new header should be put as desired in the 'header.txt' file
    before running the script and will replace the old header at the
    top of the document.
    """
    
    # Open the file for reading and writing
    
    line_number = find_require_ln(fileName)
    if line_number == -1:
        print('ERROR: Could not find REQUIREMENTS in ', fileName)
        return
    
    
    # read in the new header
    with open('header.txt', 'r') as fin:
        header = fin.read().splitlines(True)
    
    # Remove the old header
    with open(fileName, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(fileName, 'w') as fout:
        fout.writelines(header[:]) # write new header
        fout.write('\n') # write in newline for spacing
        fout.writelines(data[(line_number - 1):]) # write rest of file

    
def main():
    """Script designed to replace the headers of Test Case documents"""
    
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    rootDir = askdirectory() # show an "Open" dialog box and return the path to the selected file
    print('Head of tree travesal selected %s' % rootDir)
    
    # Traverse the tree
    for dirName, subdirList, fileList in os.walk(rootDir):
        # Ignore hidden files and directories
        fileList = [f for f in fileList if not f[0] == '.']
        subdirList[:] = [d for d in subdirList if not d[0] == '.']
        
        print('Found directory: %s' % dirName)
        for file in fileList:
            if file.endswith('.txt') and file.startswith('TC'):
                print('\tReplacing header for %s' % file)
                replace_header(os.path.join(dirName, file)) # needs absolute path

                
if __name__ == '__main__':
    main()