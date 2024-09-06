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
        "string": "\nLOAD9 "
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
    # {
    #     "pattern": [b'5C 70 5C 6E'],
    #     # Start the script
    #     "string": "@\n"
    # },
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

def process_files(input_dir="2.modified_files"):
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


def reverse_replace_patterns(bytecode, patterns):
    for pattern in sorted(patterns, key=lambda p: len(p["string"]), reverse=True):
        # Decode the string to utf-8 and replace it with the corresponding bytecode pattern
        bytecode = bytecode.replace(pattern["string"].strip("\n").encode('utf-8'), bytes.fromhex(pattern["pattern"][0].decode('utf-8').replace(' ', '')))
    return bytecode.replace(b"\\\\", b"\\")


def hex_string_to_bytes(bytecode):
    # Use a regular expression to find \xNN patterns
    pattern = r'\\x([0-9a-fA-F]{2})'

    # Function to convert matched hex code to actual byte value
    def hex_to_byte(match):
        hex_value = match.group(1)  # Extract the hex digits
        return bytes([int(hex_value, 16)])  # Convert hex to byte

    # Use re.sub with the pattern and replacement function
    result = re.sub(pattern, lambda m: hex_to_byte(m).decode('latin1'), bytecode.decode('latin1'))

    return result.encode('latin1')

def reverse_strings(bytecode):
    string_code = str(bytecode)[2:-1]
    return hex_string_to_bytes(string_code)
def write_reversed_files(file_bytecode_dict, output_dir="3.new_files"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_path, bytecode in file_bytecode_dict.items():
        # Create the corresponding path in the output directory
        relative_path = os.path.relpath(file_path, "2.modified_files")
        output_path = os.path.join(output_dir, relative_path)

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Write the bytecode back to the file in binary mode
        with open(output_path, "wb") as f:
            bytecode = bytecode.replace(b'OLD_PN', b'\\p\\n').replace(b'OLD_NEWLINE', b'\n').replace(b'OLD_CAR', b'\r')\
                .replace(b'OLD_TAB', b'\t').replace(b'OLD_E', b'\\e')
            f.write(bytecode.replace(b"\r\n", b""))

file_bytecode_dict = process_files()

# Apply the reverse replacement for each file's bytecode
for file_path, bytecode in file_bytecode_dict.items():
    reversed_bytecode = reverse_replace_patterns(bytecode, patterns)
    hexstring_sanitized_bytecode = hex_string_to_bytes(reversed_bytecode)
    file_bytecode_dict[file_path] = hexstring_sanitized_bytecode

write_reversed_files(file_bytecode_dict)
#
# # Example of how you can print the modified dictionary
# for file_path, modified_bytecode in file_bytecode_dict.items():
#     print(f"File: {file_path}, Modified Bytecode: {modified_bytecode}")

