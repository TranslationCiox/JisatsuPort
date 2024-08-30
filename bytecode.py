import codecs
import os
#SET_5\x1e\x02\x00\x003B_02 \x1e\x02\x00\x005  \x1e\x00\x00\x00\x00\r\x00\x00
patterns = [
    {
        "pattern": [b'\x00', b'\x0c', b'\x02',          b'\x00', b'\x00', b'"', b'\x1f'],
        #
        "action": " CALL1 "
    },
    {
        "pattern": [b'\x00', b'\x0c', b'\x02',          b'\x00', b'\x00', b'"'],
        #
        "action": " CALL2 "
    },
    {
        "pattern": [b'\x00', b'\x0c', b'\x00', b'\x00', b'\x00', b'\x00', b'"'],
        #
        "action": " CALL3 "
    },
    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5', b'\x1f'],
        #
        "action": " CALL4 "
    },
    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5'],
        #
        "action": " CALL5 "
    },
    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'\x1f'],
        #
        "action": " CALL6 "
    },
    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00'],
        #
        "action": " CALL7"
    },
    {
        "pattern": [b'\xef', b'!', b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00', b'\x1e'],
        #
        "action": "\nSEQ1 "
    },
    {
        "pattern": [b' ',          b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00', b'\x1e'],
        #
        "action": "\nSEQ2 "
    },
    {
        "pattern": [b' ',          b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00'],
        #
        "action": "\nSEQ3"
    },
    {
        "pattern": [                                                   b'\x00', b'\r',          b'\x02', b'\x1e'],
        #
        "action": " SEQ4 "
    },
    {
        "pattern": [b'\x03', None, b'\x00', b'\x00'],
        # BgOn, PlayCD, TextOn
        "action": "\nLOAD "
    },

    ########################### 1 Byte ###########################

    {
        "pattern": [b'\x81\x1f'],
        #
        "action": " REF1 "
    },
    {
        "pattern": [b'v\x81\x1f'],
        #
        "action": " REF2 "
    },
    {
        "pattern": [b'sv\x81\x1f'],
        #
        "action": " REF3 "
    },
    {
        "pattern": [b't\x81\x1f'],
        #
        "action": " REF4 "
    },
    {
        "pattern": [b'6t\x81\x1f'],
        #
        "action": " REF5 "
    },
    {
        "pattern": [b'\x00', b'\x1f'],
        #
        "action": " REF6 "
    },
    {
        "pattern": [b'\x1f'],
        #
        "action": " REF7 "
    },
    {
        "pattern": [b',', b'\x02'],
        #
        "action": " CHOICE "
    },

    ########################### Special ###########################
    {
        "pattern": [b'\x01', b'\x00', b'\x00', b'start', b'\xef', b'i\x01C'],
        # Start the script
        "action": "START_FILE\n"
    },
    {
        "pattern": [b'6', b'\xf1', b'\x00'],
        # End the script
        "action": "\nEND_FILE"
    },
]

def parse_bytecode(data):
    list_bytecodes = []
    # Split the data on null bytes (0x00)
    elements = data.split(b'\x00')
    for element in elements:
        if element:
            list_bytecodes.append(element)
        else:
            list_bytecodes.append(b'\x00')

    return list_bytecodes

def match_pattern(line_segment, pattern):
    """Matches a line segment with a pattern, allowing wildcards."""
    if len(line_segment) != len(pattern):
        return False

    for i in range(len(pattern)):
        if pattern[i] is not None and line_segment[i] != pattern[i]:
            return False

    return True

# Function to process and save extracted text
def save_text(lines, output_path):
    with codecs.open(output_path, "w", "utf-8") as f:
        line_counter = 0
        while line_counter < len(lines):
            line = lines[line_counter]

            if line.decode("932", errors='ignore')[0:2] == "\e":
                line = line.decode("932", errors='ignore')
                line = line.replace("\\e\\o", "\nDIALOGUE_CHOICE_START\n")
                line = line.replace("\\E\\z", "\nDIALOGUE_CHOICE_END\n")
                line = line.replace("\\e", "\n \n")
                line = line.replace("\\p\\n", "@\n")
                line = line.replace("\\w\\n\\z", "\\\n")
                f.write(line + "\r\n")
            else:
                matched = False
                for pattern in patterns:
                    pattern_length = len(pattern["pattern"])
                    if match_pattern(lines[line_counter:line_counter + pattern_length], pattern["pattern"]):
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

        if list_bytes:
            output_path = os.path.join(output_dir, fs.replace(".FOB", ".txt"))
            save_text(list_bytes, output_path)
        counter += 1


# Run the processing function
process_files(input_dir="scenario", output_dir="scenario_txts")
process_files(input_dir="scripts", output_dir="scripts_txts")

# {
#     "pattern": [b'\x03', b'\x03', b'\x00', b'\x00'],
#     # Before SCExx_xxx calls. E.g. SCE001_002
#     "action": "\nLOAD3 "
# },
# {
#     "pattern": [b'\x03', b'\x04', b'\x00', b'\x00'],
#     # BgAutoFadeIn, GetLastTxtID
#     "action": "\nLOAD4 "
# },
# {
#     "pattern": [b'\x03', b'\x05', b'\x00', b'\x00'],
#     # TextWindowOffDirect, 0.Fob, InitGameFlagBuffer
#     "action": "\nLOAD5 "
# },
# {
#     "pattern": [b'\x03', b'\x06', b'\x00', b'\x00'],
#     # Data.Fob
#     "action": "\nLOAD6 "
# },
# {
#     "pattern": [b'\x03', b'\x07', b'\x00', b'\x00'],
#     # TextFunc.Fob
#     "action": "\nLOAD8 "
# },
# {
#     "pattern": [b'\x03', b'\x08', b'\x00', b'\x00'],
#     #
#     "action": "\nLOAD8 "
# },
# {
#     "pattern": [b'\x03', b'\n', b'\x00', b'\x00'],
#     #
#     "action": "\nLOAD9 "
# },
# {
#     "pattern": [b'\x03', b'\t', b'\x00', b'\x00'],
#     #
#     "action": "\nLOAD0 "
# },