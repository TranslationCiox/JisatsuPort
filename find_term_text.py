import os
import re

def find_data_strings_in_file(file_path, counter):
    """
    Reads a file and prints all strings containing '.\Data\' in a case-insensitive manner, excluding non-text characters.
    """
    try:
        with open(file_path, "rb") as file:
            content = file.read()
            content_decoded = content.decode("932", errors='ignore')
            # Use regex to find all occurrences of the search term followed by a string of characters
            pattern = re.compile(r'\\xc8\\x00', re.IGNORECASE)
            matches = pattern.findall(content_decoded)

            # Print unique matches (optional, if you want to avoid duplicate entries)
            unique_matches = set(matches)

            for match in unique_matches:
                print("File path: ", file_path)
                print(match)
                counter += 1

    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return counter

def search_files_in_folder(folder_path):
    """
    Searches all files in a given folder for strings containing '.\Data\' in a case-insensitive manner.
    """
    counter = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            counter = find_data_strings_in_file(file_path, counter)
    print("Matches: ", counter)


print("SCRIPTS")
folder_path = "scripts_txts"
search_files_in_folder(folder_path)

print("\nSCENARIOS")
folder_path = "scenario_txts"
search_files_in_folder(folder_path)