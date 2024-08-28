import os
import re


def find_data_strings_in_file(file_path):
    """
    Reads a file and prints all strings containing '.\Data\' in a case-insensitive manner, excluding non-text characters.
    """
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            # Convert binary content to a string with 'replace' to handle any decoding issues
            content_str = content.decode(errors='replace')  # Convert content to lowercase

            # Use regex to find all occurrences of the search term followed by a string of characters
            pattern = re.compile(r'hcg', re.IGNORECASE)
            matches = pattern.findall(content_str)

            # Print unique matches (optional, if you want to avoid duplicate entries)
            unique_matches = set(matches)
            for match in unique_matches:
                print("File path: ", file_path)
                print(match)

    except Exception as e:
        print(f"Error reading file {file_path}: {e}")


def search_files_in_folder(folder_path):
    """
    Searches all files in a given folder for strings containing '.\Data\' in a case-insensitive manner.
    """
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            find_data_strings_in_file(file_path)


folder_path = "files"
search_files_in_folder(folder_path)

