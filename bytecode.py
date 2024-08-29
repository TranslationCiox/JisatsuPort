import codecs
import os

patterns = [

    {
        "pattern": [b'\x01', b'\x00', b'\x00', b'start', b'\xef', b'i\x01C'],
        # Start the script
        "action": "F_SRT\n"
    },
    {
        "pattern": [b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00', b',', b'\x02'],
        # Seems to be used for 3 byte data.
        "action": "\nVAR_3B "
    },
    {
        "pattern": [b'\x00', b'\x00', b'\x00', b'\x00', b'\r', b'\x00', b'\x00'],
        # Seems to be used for 2 byte data. Not addresses but numbers.
        "action": "\nVAR_2B"
    },
    {
        "pattern": [b'\x00', b'\x0c', b'\x00', b'\x00', b'\x00', b'\x00', b'"'],
        "action": " SEQ06 "
    },
    {
        "pattern": [b'\x02', b'\x00', b'\x00', b'5', b'6', b'\xf1', b'\x00'],
        # End the script
        "action": "\nF_END"
    },
    {
        "pattern": [b'\x02', b'\x00', b'\x00', b'5', b'\x03', b'\x03', b'\x00', b'\x00'],
        # Used before SCExxx_xxx scenario calls. Scenario indicators in the scenarios.
        "action": "\nS_STR "
    },
    {
        "pattern": [b'\x02', b'\x00', b'\x00', b'5', b' '],
        # Used at the end of certain commands like StopCD, WaitTime, SeStop
        "action": "C_END "
    },
    {
        "pattern": [b'\x00', b'\x0c', b'\x02', b'\x00', b'\x00', b'"'],
        # Used after VAR01 and the bytecode after it. Maybe to set it?
        "action": " SET01 "
    },
    {
        "pattern": [b'\x02', b'\x00', b'\x00', b'\x03', b'\x02', b'\x00', b'\x00'],
        # Often times used before commands
        "action": "\nCMD01 "
    },
    {
        "pattern": [b'\x02', b'\x00', b'\x00', b'\x03', b'\x04', b'\x00', b'\x00'],
        # Used before BgNormalFadeIn
        "action": "\nCMD02 "
    },
    {
        "pattern": [b'\x8c\x01', b'\x00', b'\r', b'\x02'],
        # Used after the VAR01 for Text it seems. Might be the dialoguebox?
        "action": "TXT1"
    },
    {
        "pattern": [b'\x02', b'\x00', b'\x00', b'\xef', b'!'],
        # Used after SCExxx_xxx scenario calls.
        "action": "S_END"
    },
    {
        "pattern": [b'\x02', b'\x00', b'\x00', b'"'],
        "action": "\nSEQ05 "
    },
    {
        "pattern": [b'\x02', b'\x00', b'\x00', b'5'],
        # Used a lot before 4 Byte addresses. Might be the address for 4 Byte data
        "action": "\nADDRES_4B "
    },
    {
        "pattern": [b'\x02', b'\x00', b'\x00'],
        # Might be some kind of new line operator?
        "action": "\n"
    },
    {
        "pattern": [b'\x03', b'\x06', b'\x00', b'\x00'],
        # Used before files
        "action": "FILE1 "
    },
    {
        "pattern": [b'\x03', b'\x07', b'\x00', b'\x00'],
        # Used before calling TextFunc.FOB
        "action": "FILE2 "
    },
    {
        "pattern": [b'\xb6\x01', b'\x00'],
        # Used in SCENARIOROOT to end each scenario. Probably set with "CMD01 start COMMAND_TO_BYTECODE3 SCENARIO_start."
        "action": "SCENARIO_START"
    },

    {
        "pattern": [b'j', b'\x00', b'\x00'],
        # Seems to be related to choices in the game. Scenario flags.
        "action": "SFLAG"
    },

    {
        "pattern": [b'\x03', b'\x03', b'\x00', b'\x00'],
        # Used before SePlayEx, TextClose, WaitTime
        "action": "\nCMD03 "
    },
    {
        "pattern": [b'\x03', b'\x05', b'\x00', b'\x00'],
        # Used before TextWindowOffDirect, InitGameFlagBuffer
        "action": "\nCMD04 "
    },
    {
        "pattern": [b'\x03', b'\x08', b'\x00', b'\x00'],
        # Used before Scenario load calls
        "action": "\nSCEN_LOAD "
    },
    {
        "pattern": [b'\x00', b'\x0c'],
        "action": " SEQ15 "
    },
    {
        "pattern": [b'\xde\x02', b'\x00'],
        # Like a series of bytecode used to get the last choice due to
        # "CMD02 GetLastTxtID COMMAND_TO_BYTECODE1 GET_TEXTID C_END"
        "action": "GET_TEXTID"
    },

    {
        "pattern": [b'\x81\x1f'],
        "action": " COMMAND_TO_BYTECODE1 "
    },
    {
        "pattern": [b'v\x81\x1f'],
        "action": " COMMAND_TO_BYTECODE2 "
    },
    {
        "pattern": [b'sv\x81\x1f'],
        "action": " COMMAND_TO_BYTECODE3 "
    },
    {
        "pattern": [b't\x81\x1f'],
        "action": " COMMAND_TO_BYTECODE4 "
    },
    {
        "pattern": [b'6t\x81\x1f'],
        "action": " COMMAND_TO_BYTECODE5 "
    },
    {
        "pattern": [b'\x1e'],
        # Likely a  delimiter (group)
        "action": " "
    },
    {
        "pattern": [b'\x1f'],
        # Likely a delimiter (record)
        "action": " "
    },
    {
        "pattern": [b'2'],
        # Likely a delimiter (record)
        "action": " and "
    },
]

patterns_zeroless = [
    {
        "pattern": [b'\r', b'\x1e', b'\x8c\x01', b'\r', b'\x02', b'\x1e'],
        # Some kind of variable, that gets assigned a value before a dialogue fragment?
        "action": "TEXT1 "
    },
    {
        "pattern": [b'\x0c', b'"', b'\x03'],
        # Seems to be related to TEXT1
        "action": " TEXT2 "
    },
    {
        "pattern": [b'\x02', b'\x1f', b'\xde\x02', b'\x1e', b'\x02', b'5', b' ', b'\x1e', b'\r', b',', b'\x02'],
        # (at the end of scenario files which require a FLAG)
        "action": "REQUIRE_SCENARIO_FLAG "
    },
    {
        "pattern": [b'\x06', b'\x0b', b'\x0c', b'\x02', b'"', b'2'],
        # (at the end of BMP loads in CG)
        "action": "BMP_FLAGS "
    },
    {
        "pattern": [b'\x02', b'\xc4', b'2', b'\xb6\x0b', b'\x1f', b'\xfe', b'\x1e'],
        # (at the end of WAV loads)
        "action": "WAV_FLAGS"
    },
    {
        "pattern": [b'\x02', b'\x03', b'\x05'],
        # Seems to LOAD WAV files
        "action": "\nWAVL "
    },

    {
        "pattern": [b'\x02', b'\x1f', b'\xb6\x01', b'\x1e', b'\x02', b'5'],
        # (Used a lot in SCENARIOROOT)
        "action": "SCENARIO_FLAGS "
    },
    {
        "pattern": [b'\02', b'\x1f', b'\xde\x02', b'\x1e', b'\x02', b'5'],
        # (Used a lot in SCENARIOROOT)
        "action": "CHOICE_FLAG_REQUIRED"
    },
    {
        "pattern": [b'\x01', b'start', b'\xef', b'i\x01C'],
        # Start the script
        "action": "START_SCRIPT\n"
    },
    {
        "pattern": [b'6', b'\xf1'],
        # Seems to END the script
        "action": "\nEND_SCRIPT"
    },
    {
        "pattern": [b'v\x81\x1f'],
        # Seems to indicate a var for commands
        "action": " VAR1 "
    },
    {
        "pattern": [b'sv\x81\x1f'],
        # Seems to indicate a var for commands
        "action": " VAR2"
    },
    {
        "pattern": [b'\x02', b'\x03', b'\x02'],
        # seems to apply something.
        "action": "APPlY_2 "
    },
    {
        "pattern": [b'\x02', b'\x03', b'\x03'],
        # seems to apply something.
        "action": "APPLY_3 "
    },
    {
        "pattern": [b'\x03', b'\x03'],
        # Goes before SCE Calls
        "action": "\nINIT_TEXT "
    },
    {
        "pattern": [b'\x03', b'\x04'],
        # Goes before certain calls (Textbox, BGFADEIN)
        "action": " APPLY_4 "
    },
    {
        "pattern": [b'\x03', b'\x05'],
        # Seems to LOAD WAV and BMP files
        "action": "\nCMD5 "
    },
    {
        "pattern": [b'\x03', b'\x06'],
        # Seems to LOAD script FOB calls, sometimes other things.
        "action": " APPLY_FILE "
    },
    {
        "pattern": [b'\x03', b'\x07'],
        # Seems to LOAD TextFunc.FOB, sometimes other things
        "action": " APPLY_FILE "
    },
    {
        "pattern": [b'\x03', b'\x08'],
        # Seems to LOAD Scenario FOB files.
        "action": "\nCMD8 "
    },
    {
        "pattern": [b'\x03', b'\t'],
        # Seems to load HEROINE and 085AC Scenario FOB files.
        "action": "\nHERO "
    },
    {
        "pattern": [b'\x03', b'\n'],
        # Seems to load SCE204SEL Scenario FOB files.
        "action": "\nS204 "
    },
    {
        "pattern": [b'\x1e', b'\x02', b'5'],
        # Seems to END command statements.
        "action": " END"
    },
    {
        "pattern": [b'\x02', b'\xef', b'!'],
        # Seems to END CSCEXX_XXX statements.
        "action": "SCE_TEXT"
    },
    {
        "pattern": [b'\x1f', b'j'],
        # Seems to indicate if a SCENARIO has a choice (flag).
        "action": "CHOICE_PRESENT"
    },
    {
        "pattern": [b'\x81\x1f'],
        # Might be a command terminator
        "action": " RUNF "
    },
    {
        "pattern": [b'\r', b',', b'\x02'],
        # Some kind of COMMAND
        "action": "FLG3 "
    },
    {
        "pattern": [b'\r', b'\x02'],
        # Some kind of COMMAND.
        "action": " SET_VAR2"
    },
    {
        "pattern": [b'\r'],
        # Some kind of COMMAND
        "action": "\nINIT"
    },
    {
        "pattern": [b'\x02', b'"'],
        # Seems to be related to FLG1
        "action": " SET_VAR1"
    },

    {
        "pattern": [b'\x1f', b' ', b'\x1e'],
        # Likely some kind of NULL?
        "action": " NULL "
    },

    {
        "pattern": [b'\x1e'],
        # Likely a  delimiter (group)
        "action": " "
    },
    {
        "pattern": [b'\x1f'],
        # Likely a delimiter (record)
        "action": " "
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