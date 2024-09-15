import os
import re
from patterns import patterns

def process_files(input_dir="1.original_files"):
    file_dict = {}

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if not file.endswith(".FOB"):
                continue

            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            file_dict[file_path] = data

    return file_dict


def replace_bytecode_patterns(file_bytecode_dict, patterns):
    modified_files = {}

    for file_path, bytecode in file_bytecode_dict.items():
        modified_bytecode = bytecode
        for pattern_info in patterns:
            pattern = pattern_info["pattern"]
            replacement_string = pattern_info["string"]
            # Convert the pattern to bytes
            byte_pattern = b''.join([bytes.fromhex(hex_str.decode()) for hex_str in pattern])

            # Replace the byte pattern with the string in the bytecode
            modified_bytecode = modified_bytecode.replace(byte_pattern, replacement_string.encode())

        modified_files[file_path] = modified_bytecode

    return modified_files


def format_bytecode_for_writing(bytecode, path):
    string_code = []
    bytecode_list = bytecode.split(b'\n')
    is_japanese = False
    for i in bytecode_list:
        if i == b'END_JAPANESE':
            is_japanese = False

        if is_japanese:
            string_code.append(str(i.decode('shift jis', errors="ignore")))
        else:
            string_code.append(str(i)[2:-1])

        if i == b'START_JAPANESE' \
                and path != "1.original_files\scenario\\089C.FOB" \
                and path != "1.original_files\scenario\\090C.FOB" \
                and path != "1.original_files\scenario\\241C.FOB" \
                and path != "1.original_files\scenario\\244C.FOB" \
                and path != "1.original_files\scenario\\247C.FOB":
            is_japanese = False
    return string_code


def write_modified_files(file_bytecode_dict, output_dir="2.modified_files"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_path, bytecode in file_bytecode_dict.items():
        # Create the corresponding path in the output directory
        relative_path = os.path.relpath(file_path, "1.original_files")
        output_path = os.path.join(output_dir, relative_path)

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Format the bytecode for writing to file
        formatted_bytecode = format_bytecode_for_writing(bytecode, file_path)

        # Write the formatted bytecode to the file with UTF-8 encoding
        with open(output_path, "w", encoding='utf-8') as f:
            for i in formatted_bytecode:
                f.write(i + "\n")


file_bytecode_dict = process_files()

# Call the function to replace patterns
modified_files_dict = replace_bytecode_patterns(file_bytecode_dict, patterns)

# Write the modified files to the new directory
write_modified_files(modified_files_dict)

