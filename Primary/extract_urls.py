import os
import shlex

SHORTCUT = "C:\\Users\\juans\\Desktop\\pyt\\Main\\test.url"


def extract_url():
    with open(SHORTCUT, "r", encoding='utf-8') as infile:
        for line in infile:
            if (line.startswith('URL')):
                url = line[4:]
                break
    if url:
        print (url)
    else:
        print("No URL found in file")

extract_url()



html_content = """
<!DOCTYPE html>
<html>
<body>

<h1>This is a simple HTML file created using Python</h1>

</body>
</html>
"""

# Specify the desired directory path (replace with your actual path)
directory_path = "C:\\Users\\juans\\Desktop\\pyt\\Main"  # Use a forward slash (/) on all systems

filename = "my_file.html"
with open(filename, "w") as file:  # Open the file in write mode
    file.write(html_content)  # Write the HTML content to the file

# Create the filename with full path
filename = f"{directory_path}/my_file.html"


print("HTML file created successfully in the specified directory!")

"""def extract_url(url_file):
    
    with open(url_file, 'r', encoding='utf-8') as f:
        contents = f.read()

    parsed_command = shlex.split(contents)

    if len(parsed_command) >= 2:
        extracted_url = parsed_command[1]
        print(f"Extracted URL: {extracted_url}")
        return extracted_url
    else:
        print(f"No URL found in file: {url_file}")
        return None
    
def generate_html(urls, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("<html><body>\n")
        for url in urls:
            if url:
                f.write(f"<a href='{url}'>{url}</a><br>\n")
        f.write("</body></html>\n")

def main():
    folder_path = "C:\\Users\\juans\\Desktop\\pyt\\Main"
    urls = []
    try:
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.endswith(".url"):
                    file_path = os.path.join(dirpath, filename)
                    extracted_url = extract_url(file_path)
                    urls.append(extracted_url)
    except (IOError, OSError) as e:
        print(f"An error ocurred while processing files: {e}")
    except ImportError as e:
        print(f"An error ocurred while processing files: {e}")

    output_file = "extracted_urls.html"
    generate_html(urls, output_file)

    print(f"Extracted URLs written to: {output_file}")"""