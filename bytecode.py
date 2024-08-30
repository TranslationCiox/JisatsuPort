import codecs
import os
#SET_5\x1e\x02\x00\x003B_02 \x1e\x02\x00\x005  \x1e\x00\x00\x00\x00\r\x00\x00
patterns = [
    {
        "pattern": [b'\x00', b'\x1f', b'\xb6\x01', b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5'],
        # Used after loading FOB files and SCE calls and some long bytecode chains which might also contain something.
        "action": " SCENARIO_END\n"
    },
    {
        "pattern": [b'\x00', b'\x0c', b'\x02', b'\x00', b'\x00', b'"', b'\x1f'],
        # Used after EVERY block of dialogue EVEN dialogue choice blocks.
        "action": " CALL1 "
    },
    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5', b'\x1f'],
        # Used in EVERY sequence with commands like e.g. NormalFadeIn
        "action": " CALL2 "
    },

    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'\x1f'],
        # Used in EVERY SCExx_xxx command.
        "action": " CALL3 "
    },
    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5'],
        # Used in EVERY sequence with commands like e.g. NormalFadeIn
        "action": " REF_END1 "
    },
    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00'],
        # Used in EVERY SCExx_xxx command.
        "action": " REF_END2 "
    },
    {
        "pattern": [b'\x00', b'\x0c', b'\x02', b'\x00', b'\x00', b'"'],
        # Used in EVERY SCExx_xxx command.
        "action": " REF_END3 "
    },
    {
        "pattern": [b'\xef', b'!', b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00', b'\x1e'],
        # Used in EVERY SCExx_xxx command.
        "action": "\nSEQ1 "
    },
    {
        "pattern": [b'\x00', b'\r', b'\x02', b'\x1e'],
        # Used in EVERY SCExx_xxx command.
        "action": " SEQ2 "
    },

    {
        "pattern": [b'\x00', b'\x0c', b'\x00', b'\x00', b'\x00', b'\x00', b'"'],
        # Used in EVERY SCExx_xxx command.
        "action": " SEQ3 "
    },
    {
        "pattern": [b' ', b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00', b',', b'\x02'],
        # Used in EVERY SCExx_xxx command.
        "action": "\nSEQ4 "
    },
    {
        "pattern": [b' ', b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00', b'\x1e'],
        # Used in EVERY SCExx_xxx command.
        "action": "\nSEQ5 "
    },
    {
        "pattern": [b' ', b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00'],
        # Used in EVERY SCExx_xxx command.
        "action": "\nSEQ6"
    },
    {
        "pattern": [b'\x03', b'\x02', b'\x00', b'\x00'],
        # BgOn, PlayCD, TextOn
        "action": "\nLOAD2 "
    },
    {
        "pattern": [b'\x03', b'\x03', b'\x00', b'\x00'],
        # Before SCExx_xxx calls. E.g. SCE001_002
        "action": "\nLOAD3 "
    },
    {
        "pattern": [b'\x03', b'\x04', b'\x00', b'\x00'],
        # BgAutoFadeIn, GetLastTxtID
        "action": "\nLOAD4 "
    },
    {
        "pattern": [b'\x03', b'\x05', b'\x00', b'\x00'],
        # TextWindowOffDirect, 0.Fob, InitGameFlagBuffer
        "action": "\nLOAD5 "
    },
    {
        "pattern": [b'\x03', b'\x06', b'\x00', b'\x00'],
        # Data.Fob
        "action": "\nLOAD6 "
    },
    {
        "pattern": [b'\x03', b'\x07', b'\x00', b'\x00'],
        # TextFunc.Fob
        "action": "\nLOAD8 "
    },
    {
        "pattern": [b'\x03', b'\x08', b'\x00', b'\x00'],
        # Scenario files e.g. 029C.Fob
        "action": "\nLOAD8 "
    },
    {
        "pattern": [b'\x03', b'\n', b'\x00', b'\x00'],
        # Scenario files e.g. 029C.Fob
        "action": "\nLOAD9 "
    },
    {
        "pattern": [b'\x03', b'\t', b'\x00', b'\x00'],
        # Scenario files e.g. 029C.Fob
        "action": "\nLOAD0 "
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
        # Seems to load files.
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
                line = line.replace("\\e\\o", "\nCHOICE\n")
                line = line.replace("\\E\\z", "\nENDCHOICE\n")
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
#     "pattern": [b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00', b',', b'\x02'],
#     # Seems to be used for 3 byte data.
#     "action": "\nVAR_3B "
# },
# {
#     "pattern": [b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00'],
#     # Seems to be used for 2 byte data. Not addresses but numbers.
#     "action": "\nVAR_2B"
# },
# {
#     "pattern": [b'\x00', b'\x0c', b'\x00', b'\x00', b'\x00', b'\x00', b'"'],
#     "action": " SEQ06 "
# },
# {
#     "pattern": [b'\x02', b'\x00', b'\x00', b'5', b'\x03', b'\x03', b'\x00', b'\x00'],
#     # Used before SCExxx_xxx scenario calls. Scenario indicators in the scenarios.
#     "action": "\nS_STR "
# },
# {
#     "pattern": [b'\x02', b'\x00', b'\x00', b'5', b' '],
#     # Used at the end of certain commands like StopCD, WaitTime, SeStop
#     "action": "C_END "
# },
# {
#     "pattern": [b'\x00', b'\x0c', b'\x02', b'\x00', b'\x00', b'"'],
#     # Used after VAR01 and the bytecode after it. Maybe to set it?
#     "action": " SET01 "
# },
# {
#     "pattern": [b'\x02', b'\x00', b'\x00', b'\x03', b'\x02', b'\x00', b'\x00'],
#     # Often times used before commands
#     "action": "\nCMD01 "
# },
# {
#     "pattern": [b'\x02', b'\x00', b'\x00', b'\x03', b'\x04', b'\x00', b'\x00'],
#     # Used before BgNormalFadeIn
#     "action": "\nCMD02 "
# },
# {
#     "pattern": [b'\x8c\x01', b'\x00', b'\r', b'\x02'],
#     # Used after the VAR01 for Text it seems. Might be the dialoguebox?
#     "action": "TXT1"
# },
# {
#     "pattern": [b'\x02', b'\x00', b'\x00', b'\xef', b'!'],
#     # Used after SCExxx_xxx scenario calls.
#     "action": "S_END"
# },
# {
#     "pattern": [b'\x02', b'\x00', b'\x00', b'"'],
#     "action": "\nSEQ05 "
# },
# {
#     "pattern": [b'\x02', b'\x00', b'\x00', b'5'],
#     # Used a lot before 4 Byte addresses. Might be the address for 4 Byte data
#     "action": "\nADDRES_4B "
# },

# {
#     "pattern": [b'\x03', b'\x06', b'\x00', b'\x00'],
#     # Used before files
#     "action": "FILE1 "
# },
# {
#     "pattern": [b'\x03', b'\x07', b'\x00', b'\x00'],
#     # Used before calling TextFunc.FOB
#     "action": "FILE2 "
# },
# {
#     "pattern": [b'\xb6\x01', b'\x00'],
#     # Used in SCENARIOROOT to end each scenario. Probably set with "CMD01 start COMMAND_TO_BYTECODE3 SCENARIO_start."
#     "action": "SCENARIO_START"
# },
#
# {
#     "pattern": [b'j', b'\x00', b'\x00'],
#     # Seems to be related to choices in the game. Scenario flags.
#     "action": "SFLAG"
# },
#
# {
#     "pattern": [b'\x03', b'\x03', b'\x00', b'\x00'],
#     # Used before SePlayEx, TextClose, WaitTime
#     "action": "\nCMD03 "
# },
# {
#     "pattern": [b'\x03', b'\x05', b'\x00', b'\x00'],
#     # Used before TextWindowOffDirect, InitGameFlagBuffer
#     "action": "\nCMD04 "
# },
# {
#     "pattern": [b'\x03', b'\x08', b'\x00', b'\x00'],
#     # Used before Scenario load calls
#     "action": "SCEN_LOAD "
# },
# {
#     "pattern": [b'\x00', b'\x0c'],
#     "action": " SEQ15 "
# },
# {
#     "pattern": [b'\xde\x02', b'\x00'],
#     # Like a series of bytecode used to get the last choice due to
#     # "CMD02 GetLastTxtID COMMAND_TO_BYTECODE1 GET_TEXTID C_END"
#     "action": "GET_TEXTID"
# },

# {
#     "pattern": [b'\x1e'],
#     # Likely a  delimiter (group)
#     "action": " "
# },
# {
#     "pattern": [b'\x1f'],
#     # Likely a delimiter (record)
#     "action": " "
# },

# {
#     "pattern": [b'\x00', b'\x00', b'\x00', b'\x00'],
#     # Script file have lots of 0 padding around functions. This is to make those files clearer.
#     "action": "\n"
# },
# {
#     "pattern": [b'\x02', b'\x00', b'\x00', b'5', b'6', b'\xf1', b'\x00'],
#     # End the script
#     "action": "\nF_END"
# },