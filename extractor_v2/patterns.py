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
        "pattern": [b'00 00 00 0c 00 02 00 00 00 22 00 20 00 1e 00 08 00 00 00 0d 00 00 00 1e 00'],
        #
        "string": " SEQ4 "
    },
    {
        "pattern": [b'00 00 0c 00 02 00 00 00 22 00 20 00 1e 00 04 00 00 00 0d 00 00 00 1e'],
        #
        "string": " SEQ5 "
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
        "pattern": [b'00 00 1e 00 02 00 00'],
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
        "pattern": [b'03 00 05 00 00 00'],
        # BgOn, PlayCD, TextOn
        "string": "\nLOAD5 "
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

assets = [
    ########## Misc. ###################
    {
        "pattern": "SEQ2 <\\x00 CALL",
        #
        "string": '!w1000'
    },
    {
        "pattern": "SEQ2 \\xca\\x00 CALL",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 \\xcb\\x00 CALL",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 \\x01\\x00 CALL1",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 \\x01\\x00 CALL1",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 L\\x00 CALL1",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 N\\x00 CALL1 \\xae\\x03 CALL7",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 P\\x00 CALL1 r\\x03 CALL7",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 |x09\\x00 CALL1 \\xd0\\x02 CALL7",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 U\\x00 CALL1 Z\\x03 CALL7",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 U\\x00 CALL1 Z\\x03 CALL7",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 V\\x00 CALL1 ^\\x10 CALL7",
        #
        "string": ';unknown'
    },

    {
        "pattern": "SEQ2  \\x00\\x00\\x00",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 \\xff\\xff\\xff\\xff",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 \\xca\\x00 SEQ5 \\x00\\x04",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 \\xcb\\x00 CALL1 \\xb4\\x17 CALL7",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 [\\x00 CALL1  \\x00 CALL7",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 \\x00\\x00 SEQ5 \\x00\\x02 SEQ4 \\x00\\x00 CALL1",
        #
        "string": ';unknown'
    },
    {
        "pattern": "SEQ2 ^\\x00 CALL2",
        # G2SUBC, definitely a CG.
        "string": ';unknown IMPORTANT'
    },
    {
        "pattern": "SEQ2 _\\x00 CALL2",
        # G3SUBC, definitely a CG.
        "string": ';unknown IMPORTANT'
    },
    {
        "pattern": "SEQ2 \\\\\\x00 CALL2",
        # K04', definitely a CG.
        "string": ';unknown IMPORTANT'
    },
    {
        "pattern": "SEQ2 ]\\x00 CALL2",
        # S5C, definitely a CG.
        "string": ';unknown IMPORTANT'
    },

    ########## MUSIC ###################
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x01",
        #
        "string": 'waveloop "WAV/SE01.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x02",
        #
        "string": 'waveloop "WAV/SE02.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x03",
        #
        "string": 'waveloop "WAV/SE03.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x04",
        #
        "string": 'waveloop "WAV/SE04.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x05",
        #
        "string": 'waveloop "WAV/SE05.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x06",
        #
        "string": 'waveloop "WAV/SE06.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x07",
        #
        "string": 'waveloop "WAV/SE07.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x08",
        #
        "string": 'waveloop "WAV/SE08.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x09",
        #
        "string": 'waveloop "WAV/SE09.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x0a",
        #
        "string": 'waveloop "WAV/SE10.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x0b",
        #
        "string": 'waveloop "WAV/SE11.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x0c",
        #
        "string": 'waveloop "WAV/SE12.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x0d",
        #
        "string": 'waveloop "WAV/SE13.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x0e",
        #
        "string": 'waveloop "WAV/SE14.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x0f",
        #
        "string": 'waveloop "WAV/SE15.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x10",
        #
        "string": 'waveloop "WAV/SE16.WAV"'
    },

    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x11",
        #
        "string": 'waveloop "WAV/SE17.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x12",
        #
        "string": 'waveloop "WAV/SE18.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x13",
        #
        "string": 'waveloop "WAV/SE19.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x14",
        #
        "string": 'waveloop "WAV/SE20.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x15",
        #
        "string": 'waveloop "WAV/SE21.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x16",
        #
        "string": 'waveloop "WAV/SE22.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x17",
        #
        "string": 'waveloop "WAV/SE23.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x18",
        #
        "string": 'waveloop "WAV/SE24.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x19",
        #
        "string": 'waveloop "WAV/SE25.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x1a",
        #
        "string": 'waveloop "WAV/SE26.WAV"'
    },

    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x1b",
        #
        "string": 'waveloop "WAV/SE27.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x1c",
        #
        "string": 'waveloop "WAV/SE28.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x1d",
        #
        "string": 'waveloop "WAV/SE29.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x1e",
        #
        "string": 'waveloop "WAV/SE30.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x1f",
        #
        "string": 'waveloop "WAV/SE31.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x20",
        #
        "string": 'waveloop "WAV/SE32.WAV"'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 SEQ5 \\x00\\x21",
        #
        "string": 'waveloop "WAV/SE33.WAV"'
    },



    {
        "pattern": "LOAD2 SeStop",
        #
        "string": "wavestop"
    },
    {
        "pattern": "SEQ2 \\x02\\x00 CALL1",
        #
        "string": 'wavestop"'
    },


    ########## MUSIC ###################
    {
        "pattern": "SEQ2 \\x02\\x01",
        #
        "string": "play track02"
    },

    {
        "pattern": "SEQ2 \\x03\\x01",
        #
        "string": "play track03"
    },
    {
        "pattern": "SEQ2 \\x04\\x01",
        #
        "string": "play track04"
    },

    {
        "pattern": "SEQ2 \\x05\\x01",
        #
        "string": "play track05"
    },

    {
        "pattern": "SEQ2 \\x06\\x01",
        #
        "string": "play track06"
    },

    {
        "pattern": "SEQ2 \\x07\\x01",
        #
        "string": "play track07"
    },

    {
        "pattern": "SEQ2 \\x08\\x01",
        #
        "string": "play track08"
    },

    {
        "pattern": "SEQ2 |x09\\x01",
        #
        "string": "play track09"
    },
    {
        "pattern": "SEQ2 |x0a\\x01",
        #
        "string": "play track10"
    },
    {
        "pattern": "SEQ2 \\x0b\\x01",
        #
        "string": "play track11"
    },
    {
        "pattern": "SEQ2 \\x0c\\x01",
        #
        "string": "play track12"
    },
    {
        "pattern": "LOAD2 StopCD",
        #
        "string": "stop"
    },

    ## CGs
    {
        "pattern": "SEQ2 ,\\x01 CALL2",
        "string": 'bg "BMP/MENU/TITLE.BMP"'
    },
    {
        "pattern": "SEQ2 \\xc8\\x00",
        "string": 'bg "BMP/MISC/BLACK.BMP"'
    },
    {
        "pattern": "SEQ2 \\xc9\\x00",
        "string": 'bg "BMP/CG/CG73.BMP"'
    },
    {
        "pattern": "SEQ2 \\x00\\x00 CALL2",
        "string": 'bg "BMP/CG/CG01.BMP"\nmov %global_cg01,1'
    },
    {
        "pattern": "SEQ2 \\x01\\x00 CALL2",
        "string": 'bg "BMP/CG/CG02.BMP"\nmov %global_cg02,1'
    },
    {
        "pattern": "SEQ2 \\x02\\x00 CALL2",
        "string": 'bg "BMP/CG/CG03.BMP"\nmov %global_cg03,1'
    },
    {
        "pattern": "SEQ2 \\x03\\x00",
        "string": 'bg "BMP/CG/CG04.BMP"\nmov %global_cg04,1'
    },
    {
        "pattern": "SEQ2 \\x04\\x00",
        "string": 'bg "BMP/CG/CG05.BMP"\nmov %global_cg05,1'
    },
    {
        "pattern": "SEQ2 \\x05\\x00",
        "string": 'bg "BMP/CG/CG06.BMP"\nmov %global_cg06,1'
    },
    {
        "pattern": "SEQ2 \\x06\\x00",
        "string": 'bg "BMP/CG/CG07.BMP"\nmov %global_cg07,1'
    },
    {
        "pattern": "SEQ2 \\x07\\x00",
        "string": 'bg "BMP/CG/CG08.BMP"\nmov %global_cg08,1'
    },
    {
        "pattern": "SEQ2 \\x08\\x00",
        "string": 'bg "BMP/CG/CG09.BMP"\nmov %global_cg09,1'
    },
    {
        "pattern": "SEQ2 \\x09\\x00",
        "string": 'bg "BMP/CG/CG10.BMP"\nmov %global_cg10,1'
    },
    {
        "pattern": "SEQ2 |x0a\\x00",
        "string": 'bg "BMP/CG/CG11.BMP"\nmov %global_cg11,1'
    },
    {
        "pattern": "SEQ2 \\x0b\\x00",
        "string": 'bg "BMP/CG/CG12.BMP"\nmov %global_cg12,1'
    },
    {
        "pattern": "SEQ2 \\x0c\\x00",
        "string": 'bg "BMP/CG/CG13.BMP"\nmov %global_cg13,1'
    },
    {
        "pattern": "SEQ2 \\x0d\\x00",
        "string": 'bg "BMP/CG/CG14.BMP"\nmov %global_cg14,1'
    },
    {
        "pattern": "SEQ2 \\x0e\\x00",
        "string": 'bg "BMP/CG/CG15.BMP"\nmov %global_cg15,1'
    },
    {
        "pattern": "SEQ2 \\x0f\\x00",
        "string": 'bg "BMP/CG/CG16.BMP"\nmov %global_cg16,1'
    },
    {
        "pattern": "SEQ2 \\x10\\x00",
        "string": 'bg "BMP/CG/CG17.BMP"\nmov %global_cg17,1'
    },
    {
        "pattern": "SEQ2 \\x11\\x00",
        "string": 'bg "BMP/CG/CG18.BMP"\nmov %global_cg18,1'
    },
    {
        "pattern": "SEQ2 \\x12\\x00",
        "string": 'bg "BMP/CG/CG19.BMP"\nmov %global_cg19,1'
    },
    {
        "pattern": "SEQ2 \\x13\\x00",
        "string": 'bg "BMP/CG/CG20.BMP"\nmov %global_cg20,1'
    },
    {
        "pattern": "SEQ2 \\x14\\x00",
        "string": 'bg "BMP/CG/CG21.BMP"\nmov %global_cg21,1'
    },
    {
        "pattern": "SEQ2 \\x15\\x00",
        "string": 'bg "BMP/CG/CG22.BMP"\nmov %global_cg22,1'
    },
    {
        "pattern": "SEQ2 \\x16\\x00",
        "string": 'bg "BMP/CG/CG23.BMP"\nmov %global_cg23,1'
    },
    {
        "pattern": "SEQ2 \\x17\\x00",
        "string": 'bg "BMP/CG/CG24.BMP"\nmov %global_cg24,1'
    },
    {
        "pattern": "SEQ2 \\x18\\x00",
        "string": 'bg "BMP/CG/CG25.BMP"\nmov %global_cg25,1'
    },
    {
        "pattern": "SEQ2 \\x19\\x00",
        "string": 'bg "BMP/CG/CG26.BMP"\nmov %global_cg26,1'
    },
    {
        "pattern": "SEQ2 \\x1a\\x00",
        "string": 'bg "BMP/CG/CG27.BMP"\nmov %global_cg27,1'
    },
    {
        "pattern": "SEQ2 \\x1b\\x00",
        "string": 'bg "BMP/CG/CG28.BMP"\nmov %global_cg28,1'
    },
    {
        "pattern": "SEQ2 \\x1c\\x00",
        "string": 'bg "BMP/CG/CG29.BMP"\nmov %global_cg29,1'
    },
    {
        "pattern": "SEQ2 \\x1d\\x00",
        "string": 'bg "BMP/CG/CG30.BMP"\nmov %global_cg30,1'
    },
    {
        "pattern": "SEQ2 \\x1e\\x00",
        "string": 'bg "BMP/CG/CG31.BMP"\nmov %global_cg31,1'
    },
    {
        "pattern": "SEQ2  REF7 \\x00",
        # \x1f was already converted during extraction, oops.
        "string": 'bg "BMP/CG/CG32.BMP"\nmov %global_cg32,1'
    },
    {
        "pattern": "SEQ2 \\x20\\x00",
        "string": 'bg "BMP/CG/CG33.BMP"\nmov %global_cg33,1'
    },
    {
        "pattern": "SEQ2 !\\x00",
        "string": 'bg "BMP/CG/CG34.BMP"\nmov %global_cg34,1'
    },
    {
        "pattern": 'SEQ2 "\\x00',
        "string": 'bg "BMP/CG/CG35.BMP"\nmov %global_cg35,1'
    },
    {
        "pattern": "SEQ2 #\\x00",
        "string": 'bg "BMP/CG/CG36.BMP"\nmov %global_cg36,1'
    },
    {
        "pattern": "SEQ2 $\\x00",
        "string": 'bg "BMP/CG/CG37.BMP"\nmov %global_cg37,1'
    },
    {
        "pattern": "SEQ2 %\\x00",
        "string": 'bg "BMP/CG/CG38.BMP"\nmov %global_cg38,1'
    },
    {
        "pattern": "SEQ2 &\\x00",
        "string": 'bg "BMP/CG/CG39.BMP"\nmov %global_cg39,1'
    },
    {
        "pattern": "SEQ2 '\\x00",
        "string": 'bg "BMP/CG/CG40.BMP"\nmov %global_cg40,1'
    },
    {
        "pattern": "SEQ2 (\\x00",
        "string": 'bg "BMP/CG/CG41.BMP"\nmov %global_cg41,1'
    },
    {
        "pattern": "SEQ2 )\\x00",
        "string": 'bg "BMP/CG/CG42.BMP"\nmov %global_cg42,1'
    },
    {
        "pattern": "SEQ2 *\\x00",
        "string": 'bg "BMP/CG/CG43.BMP"\nmov %global_cg43,1'
    },
    {
        "pattern": "SEQ2 +\\x00",
        "string": 'bg "BMP/CG/CG44.BMP"\nmov %global_cg44,1'
    },
    {
        "pattern": "SEQ2 ,\\x00",
        "string": 'bg "BMP/CG/CG45.BMP"\nmov %global_cg45,1'
    },
    {
        "pattern": "SEQ2 -\\x00",
        "string": 'bg "BMP/CG/CG46.BMP"\nmov %global_cg46,1'
    },
    {
        "pattern": "SEQ2 .\\x00",
        "string": 'bg "BMP/CG/CG47.BMP"\nmov %global_cg47,1'
    },
    {
        "pattern": "SEQ2 /\\x00",
        "string": 'bg "BMP/CG/CG48.BMP"\nmov %global_cg48,1'
    },
    {
        "pattern": "SEQ2 0\\x00",
        "string": 'bg "BMP/CG/CG49.BMP"\nmov %global_cg49,1'
    },
    {
        "pattern": "SEQ2 1\\x00",
        "string": 'bg "BMP/CG/CG50.BMP"\nmov %global_cg50,1'
    },
    {
        "pattern": "SEQ2 2\\x00",
        "string": 'bg "BMP/CG/CG51.BMP"\nmov %global_cg51,1'
    },
    {
        "pattern": "SEQ2 3\\x00",
        "string": 'bg "BMP/CG/CG52.BMP"\nmov %global_cg52,1'
    },
    {
        "pattern": "SEQ2 4\\x00",
        "string": 'bg "BMP/CG/CG53.BMP"\nmov %global_cg53,1'
    },
    {
        "pattern": "SEQ2 5\\x00",
        "string": 'bg "BMP/CG/CG54.BMP"\nmov %global_cg54,1'
    },
    {
        "pattern": "SEQ2 6\\x00",
        "string": 'bg "BMP/CG/CG55.BMP"\nmov %global_cg55,1'
    },
    {
        "pattern": "SEQ2 7\\x00",
        "string": 'bg "BMP/CG/CG56.BMP"\nmov %global_cg56,1'
    },
    {
        "pattern": "SEQ2 8\\x00",
        "string": 'bg "BMP/CG/CG57.BMP"\nmov %global_cg57,1'
    },
    {
        "pattern": "SEQ2 9\\x00",
        "string": 'bg "BMP/CG/CG58.BMP"\nmov %global_cg58,1'
    },
    {
        "pattern": "SEQ2 :\\x00",
        "string": 'bg "BMP/CG/CG59.BMP"\nmov %global_cg59,1'
    },
    {
        "pattern": "SEQ2 ;\\x00",
        "string": 'bg "BMP/CG/CG60.BMP"\nmov %global_cg60,1'
    },
    {
        "pattern": "SEQ2 <\\x00",
        "string": 'bg "BMP/CG/CG61.BMP"\nmov %global_cg61,1'
    },
    {
        "pattern": "SEQ2 =\\x00",
        "string": 'bg "BMP/CG/CG62.BMP"\nmov %global_cg62,1'
    },
    {
        "pattern": "SEQ2 >\\x00",
        "string": 'bg "BMP/CG/CG63.BMP"\nmov %global_cg63,1'
    },
    {
        "pattern": "SEQ2 ?\\x00",
        "string": 'bg "BMP/CG/CG64.BMP"\nmov %global_cg64,1'
    },
    {
        "pattern": "SEQ2 @\\x00",
        "string": 'bg "BMP/CG/CG65.BMP"\nmov %global_cg65,1'
    },
    {
        "pattern": "SEQ2 A\\x00",
        "string": 'bg "BMP/CG/CG66.BMP"\nmov %global_cg66,1'
    },
    {
        "pattern": "SEQ2 B\\x00",
        "string": 'bg "BMP/CG/CG67.BMP"\nmov %global_cg67,1'
    },
    {
        "pattern": "SEQ2 C\\x00",
        "string": 'bg "BMP/CG/CG68.BMP"\nmov %global_cg68,1'
    },
    {
        "pattern": "SEQ2 D\\x00",
        "string": 'bg "BMP/CG/CG69.BMP"\nmov %global_cg69,1'
    },
    {
        "pattern": "SEQ2 E\\x00",
        "string": 'bg "BMP/CG/CG70.BMP"\nmov %global_cg70,1'
    },
    {
        "pattern": "SEQ2 F\\x00",
        "string": 'bg "BMP/CG/CG71.BMP"\nmov %global_cg71,1'
    },
    {
        "pattern": "SEQ2 G\\x00",
        "string": 'bg "BMP/CG/CG72.BMP"\nmov %global_cg72,1'
    },
    {
        "pattern": "SEQ2 H\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG01.BMP"\nmov %global_cg74,1'
    },
    {
        "pattern": "SEQ2 I\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG02.BMP"\nmov %global_cg75,1'
    },
    {
        "pattern": "SEQ2 J\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG03.BMP"\nmov %global_cg76,1'
    },
    {
        "pattern": "SEQ2 K\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG04.BMP"\nmov %global_cg77,1'
    },
    {
        "pattern": "SEQ2 H\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG01.BMP"\nmov %global_cg74,1'
    },
    {
        "pattern": "SEQ2 I\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG02.BMP"\nmov %global_cg75,1'
    },
    {
        "pattern": "SEQ2 J\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG03.BMP"\nmov %global_cg76,1'
    },
    {
        "pattern": "SEQ2 K\\x00",
        "string": 'bg "BMP/HCG/HCG04.BMP"\nmov %global_cg77,1'
    },
    {
        "pattern": "SEQ2 L\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG05.BMP"\nmov %global_cg78,1'
    },
    {
        "pattern": "SEQ2 M\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG06.BMP"\nmov %global_cg79,1'
    },
    {
        "pattern": "SEQ2 N\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG07.BMP"\nmov %global_cg80,1'
    },
    {
        "pattern": "SEQ2 O\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG08.BMP"\nmov %global_cg81,1'
    },
    {
        "pattern": "SEQ2 P\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG09.BMP"\nmov %global_cg82,1'
    },
    {
        "pattern": "SEQ2 Q\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG10.BMP"\nmov %global_cg83,1'
    },
    {
        "pattern": "SEQ2 R\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG11.BMP"\nmov %global_cg84,1'
    },
    {
        "pattern": "SEQ2 S\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG12.BMP"\nmov %global_cg85,1'
    },
    {
        "pattern": "SEQ2 T\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG13.BMP"\nmov %global_cg86,1'
    },
    {
        "pattern": "SEQ2 U\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG14.BMP"\nmov %global_cg87,1'
    },
    {
        "pattern": "SEQ2 V\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG15.BMP"\nmov %global_cg88,1'
    },
    {
        "pattern": "SEQ2 W\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG16.BMP"\nmov %global_cg89,1'
    },
    {
        "pattern": "SEQ2 X\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG17.BMP"\nmov %global_cg90,1'
    },
    {
        "pattern": "SEQ2 Y\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG18.BMP"\nmov %global_cg91,1'
    },
    {
        "pattern": "SEQ2 Z\\x00 CALL2",
        "string": 'bg "BMP/HCG/HCG19.BMP"\nmov %global_cg92,1'
    },


    ## Warning Labels, unsucesssfull match.
    {
        "pattern": "SEQ2",
        #
        "string": "WARNING: UNMATCHED ASSET"
    },

]