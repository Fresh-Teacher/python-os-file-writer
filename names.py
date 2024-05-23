import os
import re
from bs4 import BeautifulSoup

# Define the folder containing the HTML files
folder_path = 'output_html_files'  # Update this path to your actual folder

# Function to convert CamelCase to a spaced title
def camel_case_to_title(camel_case_str):
    # Insert space before each capital letter, but not at the start
    spaced_str = re.sub(r'(?<!^)(?=[A-Z])', ' ', camel_case_str)
    return spaced_str

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an HTML file
    if filename.endswith('.html'):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract the file name without extension
        file_title = os.path.splitext(filename)[0]
        
        # Convert CamelCase to a properly spaced title
        formatted_title = camel_case_to_title(file_title)
        
        # Find the <title> tag and replace its content
        if soup.title:
            soup.title.string = formatted_title
        else:
            # If no <title> tag exists, create one and add it to the head
            new_title_tag = soup.new_tag('title')
            new_title_tag.string = formatted_title
            if soup.head:
                soup.head.append(new_title_tag)
            else:
                new_head_tag = soup.new_tag('head')
                new_head_tag.append(new_title_tag)
                soup.insert(0, new_head_tag)
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("All titles have been updated.")
