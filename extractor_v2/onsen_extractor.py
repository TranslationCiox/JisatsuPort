import os
from patterns import assets
import re


def repair_and_decode_shift_jis(input_string):
    fixed_string = re.sub(r'\|x', r'\\x', input_string)  # Fix `|x` to `\x`


    repaired_string = ''
    i = 0
    while i < len(fixed_string):
        if fixed_string[i:i + 2] == '\\x':

            repaired_string += fixed_string[i:i + 4]
            i += 4
        else:

            repaired_string += f'\\x{ord(fixed_string[i]):02x}'
            i += 1

    byte_string = bytes.fromhex(re.sub(r'\\x', '', repaired_string))


    decoded_string = byte_string.decode('shift_jis')  # Ignore invalid chars

    return decoded_string


def sound_line_convert(input_string):
    pattern = r'SE\d{2}'
    pattern2 = r'\\a6,\d+,\d+,\d+,'

    # Replace the matched pattern by appending a newline after it
    input_string = re.sub(pattern2, lambda m: m.group() + '\n', input_string)

    # Extract the identifier (e.g., SE01, SE02)
    identifier = re.search(pattern, input_string).group()

    # Check if it indicates loop or single play
    if "ループ再生" in input_string:
        # Loop format
        output = f"waveloop \"WAV/{identifier}.WAV\"\n;{input_string}"
    elif "１回再生" in input_string:
        # Non-loop format
        output = f"wave \"WAV/{identifier}.WAV\"\n;{input_string}"
    elif "停止" in input_string:
        output = f"wavestop\n;{input_string}"
    else:
        # Handle unknown format (optional)
        print("COULDN'T FIND SOUND DURATION.")
        output = f";{input_string}\n/* Unknown format */"

    return output

def process_files(input_dir="2.modified_files/scenario"):
    file_dict = {}

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if not file.endswith(".FOB"):
                continue

            file_path = os.path.join(root, file)
            with open(file_path) as f:
                data = f.read()
            file_dict[file_path[26:-4]] = data.splitlines()

    return file_dict

def process_blocks(file_dictionary, assets):
    scenario_counter = 1
    choice_counter = 0
    onsen_total = []
    for scenario in file_dictionary:
        onsen_code = []
        onsen_code.append(";/////////////////////////////////////////////////")
        onsen_code.append("; Scenario " + str(scenario))
        onsen_code.append(";/////////////////////////////////////////////////")
        onsen_code.append("*" + str(scenario))
        text = file_dictionary[scenario]
        j_text_toggle = False
        for line in text:
            #check the line against the pattern list. If the beginning of the line corresponds with the pattern
            # list, append the string from the pattern list to onsen_code.
            # Check if the line starts with a known pattern in the assets list
            for asset in assets:
                if line.startswith(asset["pattern"]):
                    onsen_code.append(asset["string"])
                    if asset["string"] == "WARNING: UNMATCHED ASSET":
                        print(asset["string"])
                        print(scenario)
                        print(line)
                        quit(1)
                    break

            if j_text_toggle:
                if line == "END_JAPANESE" or line == "END_JAPANESE_CHOICE":
                    onsen_code[-1] = onsen_code[-1] + " \\"
                    j_text_toggle = False
                    onsen_code.append(";---------------------------------------------")
                else:
                    line = line.replace(" @", "\\x5c\\x70")
                    line = repair_and_decode_shift_jis(line)
                    print(line)
                    line = line.replace("\\n\\n", "br\nbr\n")
                    if line[:2] == "\\n":
                        line = "br\n" + line[2:]
                    if "/*▲S" in line:
                        line = sound_line_convert(line)
                    line = line.replace("\\\\a4", ";\\\\a4")
                    # line = line.replace("\\n", "\n")
                    line = line.replace("\\\\p", "@")
                    line = line.replace("\\p", "@")
                    line = line.replace("−−", "`−−`")

                    onsen_code.append(line)

            if line == "START_JAPANESE" or line == "START_JAPANESE_CHOICE":
                j_text_toggle = True
        onsen_code.append("mov %scenario_flag," + str(scenario_counter))
        onsen_code.append("goto *scenario_tree")
        scenario_counter += 1
        onsen_total.append(onsen_code)
        for i in onsen_code:
            print(i)
        if scenario_counter == 4:
            quit(1)
    # with open("output.txt", "w") as file:
    #     # Write the lines to the file
    #     for segment in onsen_total:
    #         for segment_line in segment:
    #             file.writelines(segment_line)


file_dict = process_files()

process_blocks(file_dict, assets)
