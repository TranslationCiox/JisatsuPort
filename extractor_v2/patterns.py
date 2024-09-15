patterns = [
    {
        "pattern": [b'27'],
        # End the script
        "string": "|x27"
    },
    {
        "pattern": [b'0A'],
        # End the script
        "string": "|x0a"
    },
    {
        "pattern": [b'00 00 00 5c 65 5c 6f'],
        #
        "string": "\nSTART_JAPANESE_CHOICE\n"
    },
    {
        "pattern": [b'5C 45 5C 7a 00 00 00 00'],
        #
        "string": "\nEND_JAPANESE_CHOICE"
    },
    {
        "pattern": [b'5C 77 5C 6E 5C 7A'],
        #
        "string": "\nEND_JAPANESE\n"
    },
    # {
    #     "pattern": [b'5C 7A'],
    #     #
    #     "string": "\nEND_JAPANESE\n"
    # },
    {
        "pattern": [b'00 00 00 5c 65'],
        #
        "string": "\nSTART_JAPANESE\n"
    },
    {
        "pattern": [b'00 00 0c 00 02 00 00 00 22 00 1f 00'],
        #
        "string": " CALL1 "
    },
    {
        "pattern": [b'00 00 0c 00 02 00 00 00 22 00'],
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
        "pattern": [b'ef 00 21 00 1e 00 00 00 00 00 0d 00 00 00 1e 00 8c 01 00 00 0d 00 02 00 1e 00'],
        #
        "string": "\nSEQ1 "
    },
    {
        "pattern": [b'00 1e 00 00 00 00 00 0d 00 00 00 1e 00'],
        #
        "string": "\nSEQ2 "
    },
    {
        "pattern": [b'20 00 1e 00 00 00 00 00 0d 00 00 00 1f 00'],
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
        "pattern": [b'03 00 08 00 00 00'],
        # BgOn, PlayCD, TextOn
        "string": "\nLOAD8 "
    },
    # {
    #     "pattern": [b'03 00 4F 00 00 00'],
    #     # BgOn, PlayCD, TextOn
    #     "string": "\nLOAD9 "
    # },
    {
        "pattern": [b'03 00 61 00 00 00'],
        # BgOn, PlayCD, TextOn
        "string": "\nLOAD10 "
    },

    ########################### 1 Byte ###########################
    {
        "pattern": [b'00 73 76 81 1f'],
        #
        "string": " REF1 "
    },
    {
        "pattern": [b'00 76 81 1f 00'],
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
        "pattern": [b'00 81 1f 00'],
        #
        "string": " REF5 "
    },
    {
        "pattern": [b'00 1f 00'],
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
        "pattern": [b'00 00 01 00 00 00 00 00 00 00 00 00 00 00'],
        # Often between sequences after START_FILE
        "string": "\nHEADER "
    },
    # PROCESSING CODES. DO NOT DELETE.
    {
        "pattern": [b'5C 70 5C 6E'],
        # End the script
        "string": " @\n"
    },
    {
        "pattern": [b'5C 6E'],
        # End the script
        "string": "|x5c|x6e"
    },
    {
        "pattern": [b'0D'],
        # End the script
        "string": "|0d"
    },
    {
        "pattern": [b'09'],
        # End the script
        "string": "|x09"
    },
    {
        "pattern": [b'5C 65'],
        # End the script
        "string": "|x5c|x65"
    },

]