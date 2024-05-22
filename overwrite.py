import os

# Define the directory containing your HTML files
directory = 'output_html_files copy'

# Function to update JSON file paths in the HTML files
def update_json_paths(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            html_file_path = os.path.join(directory, filename)
            json_filename = filename.replace('.html', '.json')

            with open(html_file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Construct the new $.getJSON line
            old_line = "$.getJSON('data.json', function(data) {"
            new_line = f"$.getJSON('{json_filename}', function(data) {{"

            # Replace the old $.getJSON line with the new one
            if old_line in content:
                new_content = content.replace(old_line, new_line)

                with open(html_file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f'Updated {html_file_path} to fetch data from {json_filename}')
            else:
                print(f'No change needed for {html_file_path}; old line not found.')

# Call the function to update JSON paths in the HTML files
update_json_paths(directory)
