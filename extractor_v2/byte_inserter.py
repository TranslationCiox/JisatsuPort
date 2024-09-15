import os
import re
from patterns import patterns

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
            bytecode = bytecode
            f.write(bytecode.replace(b"\r\n", b""))

file_bytecode_dict = process_files()


def split_bytecode(bytecode):
    delimiter1 = b'\r\nSTART_JAPANESE\r\n'
    delimiter2 = b'\r\nEND_JAPANESE\r\n'
    chunks = bytecode.split(delimiter1)
    final_chunks = []
    for chunk in chunks:
        # Split the chunk by the second delimiter
        subchunks = chunk.split(delimiter2)

        # Extend the final_chunks list with the non-empty subchunks
        final_chunks.extend([subchunk for subchunk in subchunks if subchunk])

    for chunk in final_chunks[1::2]:
        chunk = chunk.replace(b' PROCESSING_PN', b'\x5c\x70\x5c\x6e')
        print(chunk)
        chunk.decode('932')
    print(chunks)
    quit(1)
    return chunks

# Apply the reverse replacement for each file's bytecode
for file_path, bytecode in file_bytecode_dict.items():
    bytecode = split_bytecode(bytecode)
    reversed_bytecode = reverse_replace_patterns(bytecode, patterns)
    hexstring_sanitized_bytecode = hex_string_to_bytes(reversed_bytecode)
    file_bytecode_dict[file_path] = hexstring_sanitized_bytecode

write_reversed_files(file_bytecode_dict)
#
# # Example of how you can print the modified dictionary
# for file_path, modified_bytecode in file_bytecode_dict.items():
#     print(f"File: {file_path}, Modified Bytecode: {modified_bytecode}")
import subprocess
subprocess.run("sync_pack_run.bat", shell=True)