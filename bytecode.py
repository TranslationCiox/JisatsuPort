import codecs
import os
#SET_5\x1e\x02\x00\x003B_02 \x1e\x02\x00\x005  \x1e\x00\x00\x00\x00\r\x00\x00
patterns = [
    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'\x1f', b'\xb6\x01', b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5', b'\x1f', b'j', b'\x00',
                    b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'\x1f', b'\xde\x02', b'\x00',
                    b'\x1e', b'\x02', b'\x00', b'\x00', b'5', b' ', b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r',
                    b'\x00', b'\x00'],
        # Seems to be a decent indicator of a choice being present.
        "action": " CHOICE_END"
    },

    {
        "pattern": [b'\x1f', b'\xb6\x01', b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5', b'\x1f', b'j', b'\x00', b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'\x1f', b'\xde\x02', b'\x00',
                    b'\x1e', b'\x02', b'\x00', b'\x00', b'5', b' ', b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00'],
        # Seems to be a decent indicator of a choice being present.
        "action": "CHOICE"
    },

    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'\x1f', b'\xb6\x01', b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5'],
        # Used after loading FOB files and SCE calls and some long bytecode chains which might also contain something.
        "action": " SCENARIO_END\n"
    },

    {
        "pattern": [b'\x00', b'\x0c', b'\x02', b'\x00', b'\x00', b'"', b'\x1f'],
        # Used after EVERY block of dialogue EVEN dialogue choice blocks.
        "action": "\nSEQ02 "
    },

    {
        "pattern": [b'\x00', b'\x0c', b'\x02', b'\x00', b'\x00', b'"'],
        # Used after EVERY block of dialogue EVEN dialogue choice blocks.
        "action": " SEQ01\n"
    },
    {
        "pattern": [b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00', b'\x1f'],
        # Used after EVERY block of dialogue EVEN dialogue choice blocks.
        "action": "DIALOGUE_END "
    },

    {
        "pattern": [b'\xef', b'!', b'\x1e', b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00', b'\x1e',
                    b'\x8c\x01', b'\x00', b'\r', b'\x02', b'\x1e'],
        # Used after certain commands, often time background or textbox related
        "action": "\nDIALOGUE_1 "
    },

    {
        "pattern": [b'\x00', b'\x0c', b'\x00', b'\x00', b'\x00', b'\x00', b'"', b'\x03'],
        # Used after certain commands, often time background or textbox related
        "action": " DIALOGUE_2 "
    },

    {
        "pattern": [b'\x1f', b'\xb6\x01', b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5'],
        # Used after every SCENARIO in SCENARIOROOT
        "action": "SCENARIO "
    },

    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5', b'\x1f'],
        # Used in EVERY sequence with commands like e.g. NormalFadeIn
        "action": " SEQ05 "
    },

    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'5'],
        # Used in EVERY sequence with commands like e.g. NormalFadeIn
        "action": " OP_CMD "
    },

    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00', b'\x1f'],
        # Used in EVERY SCExx_xxx command.
        "action": " SEQ03 "
    },

    {
        "pattern": [b'\x00', b'\x1e', b'\x02', b'\x00', b'\x00'],
        # Used in EVERY SCExx_xxx command.
        "action": " SCE_CMD "
    },
    # {
    #     "pattern": [b'J', b'\x00', b'\x00'],
    #     # Used after SetGamemode
    #     "action": " SET_GAMEMODE "
    # },

    {
        "pattern": [b'\x1f', b'j', b'\x00', b'\x00'],
        # Used after 5 is used.
        "action": "SET_5"
    },
    # {
    #     "pattern": [b'\x1f', None, b'\x00', b'\x00'],
    #     #
    #     "action": "4B_05"
    # },
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
        "action": "LOAD5 "
    },
    {
        "pattern": [b'\x03', b'\x06', b'\x00', b'\x00'],
        # Data.Fob
        "action": "\nLOAD6 "
    },
    {
        "pattern": [b'\x03', b'\x07', b'\x00', b'\x00'],
        # TextFunc.Fob
        "action": "LOAD7 "
    },
    {
        "pattern": [b'\x03', b'\x08', b'\x00', b'\x00'],
        # Scenario files e.g. 029C.Fob
        "action": "\nLOAD8 "
    },

    # {
    #     "pattern": [b'\x03', None, b'\x00', b'\x00'],
    #     # Before files, commands, and SCExx_xxx calls.
    #     "action": "\n4B_03 "
    # },

    # {
    #     "pattern": [b'\x00', None, b'\x00', b'\x00'],
    #     # Used before
    #     "action": "\n4B_02 "
    # },

    {
        "pattern": [b'\x1f', b'\xB6', b'\x01', b'\x00'],
        #
        "action": "\n4B_01 "
    },

    ########################### 4 Bytes (wildcard) ###########################
    # {
    #     "pattern": [b'\x1e', None, b'\x00', b'\x00'],
    #     # Used before a 4B_02 or 4B_03
    #     "action": "\n4B_04 "
    # },
    # {
    #     "pattern": [b'\r', b'\x02', b'\x1e', None],
    #     #
    #     "action": "\n4B_06"
    # },
    ########################### 3 Bytes ###########################
    {
        "pattern": [b'\x1f', b'\xb6\x01', b'\x00'],
        #
        "action": "3B_01 "
    },
    {
        "pattern": [b'\x1f', b'\xde\x02', b'\x00'],
        #
        "action": "3B_02 "
    },
    {
        "pattern": [b'\x1e', b'\x8c\x01', b'\x00'],
        #
        "action": "3B_03 "
    },

    ########################### 2 Bytes ###########################

    {
        "pattern": [b'\xef', b'!'],
        #
        "action": "2B_01 "
    },
    {
        "pattern": [b',', b'\x02'],
        #
        "action": "\n2B_02 "
    },

    ########################### 1 Byte ###########################

    {
        "pattern": [b'\x81\x1f'],
        #
        "action": " OP01 "
    },
    {
        "pattern": [b'v\x81\x1f'],
        #
        "action": " OP02 "
    },
    {
        "pattern": [b'sv\x81\x1f'],
        # Seems to load files.
        "action": " OP03 "
    },
    {
        "pattern": [b't\x81\x1f'],
        #
        "action": " OP04 "
    },
    {
        "pattern": [b'6t\x81\x1f'],
        #
        "action": " OP05 "
    },
    {
        "pattern": [b'5'],
        #
        "action": "5 "
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