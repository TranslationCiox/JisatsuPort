import codecs
import os

def parse_bytecode(data):
    list_bytecodes = []
    # Split the data on null bytes (0x00)
    elements = data.split(b'\x00')

    # Initialize list to hold parsed elements
    parsed_elements = []

    for element in elements:
        if element:
            list_bytecodes.append(element)

    return list_bytecodes



# def extract_text(data):
#     offset = 0
#     lines = []
#
#     while True:
#         x = data.find(b"\e", offset)
#         if x == -1:
#             break
#
#         text = b''
#         while data[x] != 0:
#             text += bytes([data[x]])
#             x += 1
#
#         lines.append(text.decode("932", errors='ignore'))
#         offset = x + 1
#
#     return lines


# Function to process and save extracted text
def save_text(lines, output_path):
    with codecs.open(output_path, "w", "utf-8") as f:
        for line in lines:

            if line.decode("932", errors='ignore')[0:2] == "\e":
                line = line.decode("932", errors='ignore')
                line = line.replace("\\e", "")
                line = line.replace("\\z", "")
                line = line.replace("\\p", "@")
                line = line.replace("\\w", "\\")
                line = line.replace("\\n", "\n")
                f.write(line + "\r\n")
            else:
                f.write(str(line)[2:-1] + "\r\n")

# Main processing loop
def process_files(input_dir="files", output_dir="txts"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    counter = 0
    for fs in os.listdir(input_dir):
        if not fs.endswith(".FOB"):
            continue

        with open(os.path.join(input_dir, fs), "rb") as f:
            data = f.read()

        list_bytes = parse_bytecode(data)


        # lines = extract(data, start_codes)

        if list_bytes:

            output_path = os.path.join(output_dir, fs.replace(".FOB", ".txt"))
            save_text(list_bytes, output_path)
            print(f"Processed {output_path}")
        counter += 1
        # if counter == 2:
        #     quit(1)



# Run the processing function
process_files()
