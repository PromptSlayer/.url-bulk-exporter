import os
from datetime import datetime

file_path = "C:\\Users\\juans\\Desktop\\pyt\\Primary\\test.url"





with open(file_path, "r", encoding='utf-8') as infile:
    for line in infile:
        if (line.endswith('.url')):
            url = line[4:]
            print(url)
            break
        else:
            print ("URL file contains no URL")
            break


'''
    #try:
with open(file_path, "r", encoding='utf-8') as infile:
    for line in infile:
        if (line.startswith('URL')):
            url = line[4:]
            break
            #return url, formatted_creation, formatted_modification
print (url)             
'''

'''except FileNotFoundError:
    # Handle potential file not found error (optional)
        print(f"Error: Shortcut file not found in: {file_path}")
        return None, None, None  # Indicate error or file not found
    '''

    
#url, formatted_creation, formatted_modification = extract_url(test_file_path)

'''
filename = 'C:\Temp\ROGUE ONE- A Star Wars Story TRAILER (2016) - YouTube.url'
with open(filename, "r") as infile:
    for line in infile:
        if (line.startswith('URL')):
            url = line[4:]
            break
            '''
