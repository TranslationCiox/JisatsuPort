import os
import re

patterns = [
    {
        "pattern": [b'00 0c 02 00 00 22 1f'],
        #
        "string": " CALL1 "
    },
    {
        "pattern": [b'00 0c 02 00 00 22'],
        #
        "string": " CALL2 "
    },
    {
        "pattern": [b'00 0c 00 00 00 00 22'],
        #
        "string": " CALL3 "
    },
    {
        "pattern": [b'00 1e 02 00 00 05 1f'],
        #
        "string": " CALL4 "
    },
    {
        "pattern": [b'00 1e 02 00 00 05'],
        #
        "string": " CALL5 "
    },
    {
        "pattern": [b'00 1e 02 00 00 1f'],
        #
        "string": " CALL6 "
    },
    {
        "pattern": [b'00 1e 02 00 00'],
        #
        "string": " CALL7 "
    },
    {
        "pattern": [b'ef 21 1e 00 00 00 00 0d 00 00 1e'],
        #
        "string": "|n SEQ1"
    },
    {
        "pattern": [b'20 1e 00 00 00 00 0d 00 00 1e'],
        #
        "string": "|n SEQ2"
    },
    {
        "pattern": [b'20 1e 00 00 00 00 0d 00 00'],
        #
        "string": "|n SEQ3"
    },
    {
        "pattern": [b'00 0d 02 1e'],
        #
        "string": " SEQ4 "
    },
    {
        "pattern": [b'03'],
        # BgOn, PlayCD, TextOn
        "string": "|n LOAD"
    },

    ########################### 1 Byte ###########################

    {
        "pattern": [b'81 1f'],
        #
        "string": " REF1 "
    },
    {
        "pattern": [b'76 81 1f'],
        #
        "string": " REF2 "
    },
    {
        "pattern": [b'73 76 81 1f'],
        #
        "string": " REF3 "
    },
    {
        "pattern": [b'74 81 1f'],
        #
        "string": " REF4 "
    },
    {
        "pattern": [b'36 74 81 1f'],
        #
        "string": " REF5 "
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
        "pattern": [b'01 00 00 00 73 74 61 72 74 00 ef 00'],
        # Start the script
        "string": " START_FILE "
    },
    {
        "pattern": [b'36 00 f1 00'],
        # End the script
        "string": "|n END_FILE"
    },
    {
        "pattern": [b'01 00 00 00 00 00 00 00 00 00 00'],
        # Often between sequences after START_FILE
        "string": "|n HEADER"
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
    # Convert bytecode to a hex representation with space-separated bytes
    # hex_representation = ' '.join(f'{byte:02x}' for byte in bytecode)
    for byte in bytecode:
        print(byte)
    quit(1)


    # Replace '|n' with new lines if present in bytecode (assuming |n is part of the bytecode string)
    formatted_bytecode = bytecode.replace('|n', '\n')

    return formatted_bytecode

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
            f.write(formatted_bytecode)



# Example usage
file_bytecode_dict = process_files()

# Call the function to replace patterns
modified_files_dict = replace_bytecode_patterns(file_bytecode_dict, patterns)

# Write the modified files to the new directory
write_modified_files(modified_files_dict)

# Example of how you can print the modified dictionary
for file_path, modified_bytecode in modified_files_dict.items():
    print(f"File: {file_path}, Modified Bytecode: {modified_bytecode}")
