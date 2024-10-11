from patterns import assets
import subprocess
import re
import os

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

    try:
        decoded_string = byte_string.decode('shift_jis')  # Ignore invalid chars
    except:
        print("COULD NOT DECODE STRING")
        print(byte_string.decode('shift_jis', errors="ignore"))
        print(quit(1))
    return decoded_string


def sound_line_convert(input_string):
    pattern = r'SE\d{2}'
    pattern2 = r'\\a6,\d+,\d+,\d+,'

    # Replace the matched pattern by appending a newline after it
    input_string = re.sub(pattern2, lambda m: m.group() + '\n', input_string)

    # Extract the identifier (e.g., SE01, SE02)
    try:
        identifier = re.search(pattern, input_string).group()
    except:
        return f"wavestop\n{input_string}"
    # Check if it indicates loop or single play
    if "ループ再生" in input_string:
        # Loop format
        output = f"waveloop \"WAV/{identifier}.WAV\"\n{input_string}"
    elif "１回再生" in input_string:
        # Non-loop format
        output = f"wave \"WAV/{identifier}.WAV\"\n{input_string}"
    elif "停止" in input_string:
        output = f"wavestop\n{input_string}"
    else:
        # Handle unknown format
        print("COULDN'T FIND SOUND DURATION.")
        output = f";{input_string}\n;/* Unknown format */"

    return output

def cg_line_convert(input_string):
    # Check if it is a HCG or CG
    if "HCG" in input_string or "hcg" in input_string:
        cg_pattern = r"HCG(\d{2})"
        matches = re.findall(cg_pattern, input_string, re.IGNORECASE)
        output = f"BG \"BMP/HCG/{matches[0]}.BMP\"\n;{input_string}"
    elif "CG" in input_string or "cg" in input_string:
        cg_pattern = r"CG(\d{2})"
        matches = re.findall(cg_pattern, input_string, re.IGNORECASE)
        output = f"BG \"BMP/HCG/{matches[0]}.BMP\"\n;{input_string}"
    else:
        # Handle unknown format (optional)
        print("COULDN'T FIND CG.")
        print(input_string)
        output = f";{input_string}\n/* Unknown format */"
    # print("ORIGINAL STRING")
    # print(input_string)
    # print("OUTPUT STRING")
    # print(output)
    # print("\n")
    return output

def decode_asset_code(input_string):
    # Check if it is a HCG or CG
    pattern = r'(([^,]*,){4})'
    # Replace the matched pattern with itself followed by a newline
    output = re.sub(pattern, r'\1\n', input_string)
    input(input_string)
    print(output)
    # output = output.replace("/*", "\n;/*")


    # if "a0" in input_string:
    #     cg_pattern = r"HCG(\d{2})"
    #     matches = re.findall(cg_pattern, input_string, re.IGNORECASE)
    #     output = f"BG \"BMP/HCG/{matches[0]}.BMP\"\n;{input_string}"

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
    with open("4.new_script\\01.txt", "w", encoding="shift-jis") as f:
        pass  # This opens the file in write mode and immediately closes it, clearing the contents.

    scenario_counter = 1
    choice_counter = 1
    onsen_total = []
    for scenario in file_dictionary:
        print("CONVERTING SCENARIO " + str(scenario))
        if scenario_counter == 200:
            break
        onsen_code = []
        onsen_code.append(";/////////////////////////////////////////////////")
        onsen_code.append("; Scenario " + str(scenario))
        onsen_code.append(";/////////////////////////////////////////////////")
        onsen_code.append("*" + str(scenario))
        text = file_dictionary[scenario]
        j_text_toggle = False
        j_choice_toggle = False
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
                if line == "END_JAPANESE" or line == "END_JAPANESE2"or line == "END_JAPANESE3":
                    onsen_code[-1] = onsen_code[-1] + " \\"
                    j_text_toggle = False
                    onsen_code.append(";---------------------------------------------")
                else:
                    line = line.replace(" @", "\\x5c\\x70")
                    line = repair_and_decode_shift_jis(line)
                    line = line.replace("\\n\\n", "br\nbr\n")
                    if line[:2] == "\\n":
                        line = "br\n" + line[2:]
                    # if "/*▲S" in line:
                    #     line = sound_line_convert(line)
                    # if "HCG" in line or "CG" in line or "cg" in line or "hcg" in line:
                    #     line = cg_line_convert(line)
                    if "a" in line:
                        line = decode_asset_code(line)
                    line = line.replace("/*", "\n;/*")
                    line = line.replace("\\\\a4", "\nbr\n;\\\\a4")
                    line = line.replace("\\n", "\n")
                    line = line.replace("\\\\p", "@")
                    line = line.replace("\\p", "@")
                    line = line.replace("−−", "――")
                    line = line.replace("\\", "")

                    # line = line.replace("a6,0,0,0,", "a6,0,0,0,\n")
                    # line = line.replace("a6,-2,0,0,", "a6,-2,0,0,\n")
                    onsen_code.append(line)
            if j_choice_toggle:
                if "END_JAPANESE_CHOICE" in line:
                    j_choice_toggle = False
                    onsen_code.append(";---------------------------------------------")
                    choice_counter += 1

                else:
                    line = repair_and_decode_shift_jis(line)
                    choice_count = int(line[-2])
                    for i in range(choice_count):
                        line = line.replace("\\n", '",*choice' + str(choice_counter) + "_" + str(i) + ',"', 1)
                    line = line.replace(',"\\', "\n;\\")
                    for i in range(choice_count):
                        line = line + "\n*choice" + str(choice_counter) + "_" + str(i)
                        line = line + "\nmov ?choices[" + str(choice_counter) + "]," + str(i)
                        line = line + "\ngoto " "*choice" + str(choice_counter) + "_end"
                    line = line + "\n*choice" + str(choice_counter) + "_end"
                    onsen_code[-1] = onsen_code[-1] + '"' + line
            if line == "START_JAPANESE":
                j_text_toggle = True
            if line == "START_JAPANESE_CHOICE":
                j_choice_toggle = True
                onsen_code.append("select ")
        onsen_code.append("mov %scenario_flag," + str(scenario_counter))
        onsen_code.append("goto *scenario_tree")
        scenario_counter += 1
        onsen_total.append(onsen_code)

        # Write the current scenario to the file in Shift-JIS encoding
        with open("4.new_script\\01.txt", "a", encoding="shift-jis") as f:
            for line in onsen_code:
                f.write(line + "\n")

        # for i in onsen_code:
        #     print(i)




file_dict = process_files()

process_blocks(file_dict, assets)

source_path = r"D:\git_projects\JisatsuPort\extractor_v2\4.new_script"
destination_path = r"D:\eien\VNs\Duke\Jisatsu\Project Files (jisatsu)\jisatsu_eien\gamedata"


# Step 4. Port the finished script file to the game directory.
command_to_run = f'robocopy "{source_path}" "{destination_path}" 01.txt /Z /FFT /XO /NP /TEE /LOG:synclog.txt'
subprocess.run(command_to_run, shell=True)