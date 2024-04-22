import os
from datetime import datetime


print(os.getcwd())
SHORTCUT = "C:\\Users\\juans\\Desktop\\pyt\\Primary\\test.url"

# Specify the desired directory path (replace with your actual path)
directory_path = "C:\\Users\\juans\\Desktop\\pyt\\Primary"  # Use a forward slash (/) on all systems
file_path = directory_path

def extract_url(file_path):
    try:
        with open(file_path, "r", encoding='utf-8') as infile:
            for line in infile:
                if (line.startswith('URL')):
                    url = line[4:]
                    creation_time = os.path.getctime(file_path)
                    modification_time = os.path.getmtime(file_path)
                    formatted_creation = datetime.fromtimestamp(creation_time).strftime("%Y%m%d%H%M%S")
                    formatted_modification = datetime.fromtimestamp(modification_time).strftime("%Y%m%d%H%M%S")
                    print("URL Processed")
                    return url, formatted_creation, formatted_modification
    except FileNotFoundError:
    # Handle potential file not found error (optional)
        print(f"Error: Shortcut file not found: {file_path}")
        return None, None, None  # Indicate error or file not found
    

foldername = (" ") 
def get_path(directory):
  """
  Retrieves creation and modification timestamps for a directory.

  Args:
      directory_path (str): Path to the directory.

  Returns:
      tuple: A tuple containing (creation_time, modification_time) as timestamps.
  """
  try:
    stat_result = os.stat(directory)
  except FileNotFoundError:
    print(f"Error: Directory not found: {directory}")
    return None, None, None

  
  creation_time = stat_result.st_ctime
  modification_time = stat_result.st_mtime
  folder_creation = datetime.fromtimestamp(creation_time).strftime("%Y%m%d%H%M%S")
  folder_modification = datetime.fromtimestamp(modification_time).strftime("%Y%m%d%H%M%S")
  return folder_creation, folder_modification, foldername






# Example usage

dirname = os.path.basename(directory_path)

html_content = f"""
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>{dirname}</TITLE>
"""



filecreate = "my_file.html" # Creates a new file in the current directory
with open(filecreate, "w") as file:  # Open the file in write mode
    file.write(html_content)  # Write the HTML content to the file

# Create the filename with full path
filecreate = f"{directory_path}/my_file.html"
# Get base directory path


#now = datetime.now()
#add_date = now.strftime("%Y%m%d%H%M%S")
#last_modified = add_date


def create_html_entry(url, formatted_creation, formatted_modification, filename):


    if url:
        url = url.rstrip()  # Only rstrip if URL is found
    else:
        url = ""  # Set to empty string if no URL
    return f"""<DT><A HREF="{url}" ADD_DATE="{formatted_creation}" LAST_MODIFIED="{formatted_modification}">{filename}</A>\n"""

def create_folder_entry(folder_creation, folder_modification, foldername):


    if foldername:
        return f"""<DT><H3 ADD_DATE="{folder_creation}" LAST_MODIFIED="{folder_modification}">{foldername}</H3>\n"""





def get_tabs(level):
  """
  Generates a string with the specified number of tabs for indentation.

  Args:
      level (int): The subdirectory level (number of tabs).

  Returns:
      str: A string containing the desired number of tabs.
  """
  return "\t" * level

# Example usage inside your loop
current_directory, subdirectories, files = os.walk(directory_path).__next__()
level = current_directory.count(os.sep) - 1  # Get subdirectory level from path
tabs = get_tabs(level)

# Example usage in your HTML file

directory_tab = (f"{tabs}")


existing_html = f"<TITLE>{dirname}</TITLE>\n<H1>Bookmarks</H1>\n<DL><p>\n    "
third_header = f'<DT><H3 ADD_DATE="dircre" LAST_MODIFIED="dirmod" PERSONAL_TOOLBAR_FOLDER="true">Bookmarks</H3>\n    '
new_entry = '<DL><p>\n'



#text_parts = [entry_content_1, f' ADD_DATE="">"google"</A>']
#entry_content = f'<DT><A HREF="{extracted_url}" ADD_DATE="">"{extracted_url}"</A>'
#combined_entry = '' .join(text_parts)

appended_html = existing_html + third_header + new_entry
finish_entry = "\n</DL><p>"


print("HTML file created successfully in the specified directory!")

file = open("my_file.html", "a")
file.write(appended_html)



for root, directories, files in os.walk(directory_path):
    # Process the current directory
    print(f"Current directory: {root}")
    foldername = f"{root}"  # Optionally, assign the full path to foldername
    folder = os.path.basename(root)
    directory = foldername
    creation_time, modification_time, foldername = get_path(os.path.join(root, directory))
        
    
    #created_folder = get_path
    created_path = create_folder_entry(creation_time, modification_time, foldername)

    with open("my_file.html", "a") as f:
        try:
            f.write(directory_tab + created_path)  # Write the HTML entry to the file
            print("Path extracted.")
        except IOError as e:
            print(f"Error writing to file: {e}")  # Handle potential errors

    # Iterate over the subdirectories
    for directory in directories:
        print(f"Subdirectory: {directory}")
        
        

    # Iterate over the files
    for file in files:
        if file.endswith(".url"):  # Check for shortcut file extension
            url, creation_date, modification_date = extract_url(os.path.join(root, file))
            
            filename = os.path.splitext(file)[0]  # Split filename and extension
            #extracted_url = extract_url(file)

            file_path = os.path.join(root, file)
            
            created_HTML = create_html_entry(url, creation_date, modification_date, filename)
            entry_content = created_HTML

            if url:
                url = url.rstrip()  # Only rstrip if URL is found
                with open("my_file.html", "a") as f:
                    try:
                        f.write(directory_tab + created_HTML)  # Write the HTML entry to the file
                        print("URL and metadata written successfully")
                    except IOError as e:
                        print(f"Error writing to file: {e}")  # Handle potential errors
            else:
                print(f"No URL found in file: {file}") # Or handle differently
            
            # Remove whitespace from the end of the URL
        else:
            print(f"Skipping file: {file}")
#loop_through_directories(directory_path)

appended_html_2 = finish_entry
file = open("my_file.html", "a")
file.write(appended_html_2)
file.close()
