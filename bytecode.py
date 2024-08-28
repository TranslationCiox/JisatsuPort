import codecs
import os

patterns = [
    {
        "pattern": [b'\x06', b'\x0b', b'\x0c', b'\x02', b'"', b'2', b'\xca\x17'], # (at the end of BMP loads)
        "action": " #Load BMP"
    },
    {
        "pattern": [b'\x1e', b'\x02', b'\xc4', b'2', b'\xb6\x0b', b'\x1f', b'\xfe', b'\x1e', b'\x02'], # (at the end of WAV loads)
        "action": " #Load WAV"
    },
    {
        "pattern": [b'\x01', b'start', b'\xef', b'i\x01C'],  # Start the script
        "action": "START\n"
    },
    {
        "pattern": [b'\x03', b'\x02'],  # Goes before commands
        "action": "\r\nCMD1 "
    },
    {
        "pattern": [b'\x03', b'\x03'],  # Goes before SCE Calls
        "action": "\r\nSCEN "
    },
    {
        "pattern": [b'\x03', b'\x04'],  # Goes before certain calls (Textbox, BGFADEIN)
        "action": "\r\nCMD2 "
    },
    {
        "pattern": [b'\x03', b'\x05'],  # Seems to LOAD WAV and BMP files
        "action": "\nLOAD "
    },
    {
        "pattern": [b'\x03', b'\x06'],  # Seems to LOAD script FOB calls
        "action": "\nFOBT "
    },
    {
        "pattern": [b'\x03', b'\x07'],  # Seems to LOAD TextFunc.FOB.
        "action": "\nWHAT "
    },
    {
        "pattern": [b'\x03', b'\x08'],  # Seems to LOAD Scenario FOB files.
        "action": "\nFOBO "
    },
    {
        "pattern": [b'\x1e'],  # Likely a  delimiter (group)
        "action": " "
    },
    {
        "pattern": [b'\x1f'],  # Likely a delimiter (record)
        "action": " "
    },
    {
        "pattern": [b'\x81\x1f'],  # Might be a command terminator
        "action": " RUNF "
    },
    {
        "pattern": [b'\r'], #Seems to be related to flags. Both to set, and read them.
        "action": "FLAG"
    },
]

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

# Function to process and save extracted text
def save_text(lines, output_path):
    with codecs.open(output_path, "w", "utf-8") as f:
        line_counter = 0
        while line_counter < len(lines):
            line = lines[line_counter]

            if line.decode("932", errors='ignore')[0:2] == "\e":
                line = line.decode("932", errors='ignore')
                line = line.replace("\\e\\o", "\nCHOICE\n")
                line = line.replace("\\E\\z", "\nENDCHOICE\n")
                line = line.replace("\\e", "\n \n")
                line = line.replace("\\p\\n", "@\n")
                line = line.replace("\\w\\n\\z", "\\\n")
                f.write(line + "\r\n")
            else:
                matched = False
                for pattern in patterns:
                    # Check if current segment of lines matches the pattern
                    pattern_length = len(pattern["pattern"])
                    if lines[line_counter:line_counter + pattern_length] == pattern["pattern"]:
                        # Use the action field directly to insert the desired text
                        f.write(pattern["action"])
                        line_counter += pattern_length - 1  # Skip the matched pattern length minus one since we'll increment after the match
                        matched = True
                        break

                if not matched:
                    f.write(str(line)[2:-1])

            line_counter += 1

# Main processing loop
def process_files(input_dir="scripts", output_dir="scripts_txts"):
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
            # print(f"Processed {output_path}")
        counter += 1
        # if counter == 2:
        #     quit(1)



# Run the processing function
process_files(input_dir="scenario", output_dir="scenario_txts")
process_files(input_dir="scripts", output_dir="scripts_txts")