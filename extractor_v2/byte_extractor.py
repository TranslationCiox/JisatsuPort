import os
import re

patterns = [
    {
        "pattern": [b'5C 77 5C 6E 5C 7A'],
        #
        "string": "\nEND_JAPANESE\n"
    },
    {
        "pattern": [b'5c 65'],
        #
        "string": "\nSTART_JAPANESE\n"
    },
    {
        "pattern": [b'00 00 0c 00 02 00 00 00 22 00 1f'],
        #
        "string": " CALL1 "
    },
    {
        "pattern": [b'00 0c 00 02 00 00 00 22 00'],
        #
        "string": " CALL2 "
    },
    {
        "pattern": [b'00 00 0c 00 00 00 00 00 22'],
        #
        "string": " CALL3 "
    },
    {
        "pattern": [b'00 1e 02 00 00 05 1f'],
        #
        "string": " CALL4 "
    },
    {
        "pattern": [b'00 00 00 1e 00 02 00 00 00 35 00'],
        #
        "string": " CALL5 "
    },
    {
        "pattern": [b'00 1e 02 00 00 1f'],
        #
        "string": " CALL6 "
    },
    {
        "pattern": [b'00 00 1e 00 02 00 00 00'],
        #
        "string": " CALL7 "
    },
    {
        "pattern": [b'ef 00 21 00 1e 00 00 00 00 00 0d 00 00 00 1e 00'],
        #
        "string": "\nSEQ1 "
    },
    {
        "pattern": [b'00 1e 00 00 00 00 00 0d 00 00 00 1e 00'],
        #
        "string": "\nSEQ2 "
    },
    {
        "pattern": [b'20 00 1e 00 00 00 00 00 0d 00 00'],
        #
        "string": "\nSEQ3 "
    },
    {
        "pattern": [b'00 0d 00 02 00 1e 00'],
        #
        "string": " SEQ4 "
    },
    {
        "pattern": [b'03 00 02 00 00 00'],
        # BgOn, PlayCD, TextOn
        "string": "\nLOAD2 "
    },
    {
        "pattern": [b'03 00 03 00 00 00'],
        # BgOn, PlayCD, TextOn
        "string": "\nLOAD3 "
    },
    {
        "pattern": [b'03 00 04 00 00 00'],
        # BgOn, PlayCD, TextOn
        "string": "\nLOAD4 "
    },
    {
        "pattern": [b'03 00 06 00 00 00'],
        # BgOn, PlayCD, TextOn
        "string": "\nLOAD6 "
    },
    {
        "pattern": [b'03 00 07 00 00 00'],
        # BgOn, PlayCD, TextOn
        "string": "\nLOAD7 "
    },
    {
        "pattern": [b'03 00 4F 00 00 00'],
        # BgOn, PlayCD, TextOn
        "string": "\nLOAD8 "
    },
    {
        "pattern": [b'03 00 61 00 00 00'],
        # BgOn, PlayCD, TextOn
        "string": "\nLOAD8 "
    },

    ########################### 1 Byte ###########################
    {
        "pattern": [b'00 73 76 81 1f'],
        #
        "string": " REF1 "
    },
    {
        "pattern": [b'76 81 1f'],
        #
        "string": " REF2 "
    },
    {
        "pattern": [b'36 74 81 1f'],
        #
        "string": " REF3 "
    },
    {
        "pattern": [b'74 81 1f'],
        #
        "string": " REF4 "
    },
    {
        "pattern": [b'81 1f'],
        #
        "string": " REF3 "
    },
    {
        "pattern": [b'00 1f'],
        #
        "string": " REF6 "
    },
    {
        "pattern": [b'1f'],
        #
        "string": " REF7 "
    },
    {
        "pattern": [b'2c 02'],
        #
        "string": " CHOICE "
    },

    ########################### Special ###########################
    {
        "pattern": [b'5C 70 5C 6E'],
        # Start the script
        "string": "@\n"
    },
    {
        "pattern": [b'01 00 00 00 73 74 61 72 74 00 ef 00 69 01 43 00'],
        # Start the script
        "string": "START_FILE "
    },
    {
        "pattern": [b'36 00 f1 00'],
        # End the script
        "string": "\nEND_FILE"
    },
    {
        "pattern": [b'01 00 00 00 00 00 00 00 00 00 00 00'],
        # Often between sequences after START_FILE
        "string": "\nHEADER "
    },

]

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


def format_bytecode_for_writing(bytecode):
    string_code = []
    bytecode_list = bytecode.split(b'\n')
    is_japanese = False
    for i in bytecode_list:
        if i == b'END_JAPANESE':
            is_japanese = False

        if is_japanese:
            string_code.append(str(i.decode('shift_jis', errors='replace')))
        else:
            string_code.append(str(i)[2:-1])

        if i == b'START_JAPANESE':
            is_japanese = True
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
        formatted_bytecode = format_bytecode_for_writing(bytecode)

        # Write the formatted bytecode to the file with UTF-8 encoding
        with open(output_path, "w", encoding='utf-8') as f:
            for i in formatted_bytecode:
                f.write(i + "\n")


file_bytecode_dict = process_files()

# Call the function to replace patterns
modified_files_dict = replace_bytecode_patterns(file_bytecode_dict, patterns)

# Write the modified files to the new directory
write_modified_files(modified_files_dict)

