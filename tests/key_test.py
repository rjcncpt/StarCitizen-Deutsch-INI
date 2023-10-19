from configparser import ConfigParser
import json


def addLine(filename, line):
    with open(filename, encoding="utf_8_sig", mode="r+") as file:
        file_data = file.read()
        file.seek(0, 0)
        file.write(line + ("\n") + file_data)


def removeFirstLine(filename):
    with open(filename, encoding="utf_8_sig", mode="r+") as file:
        lines = file.readlines()
        file.seek(0, 0)
        file.truncate()
        file.writelines(lines[1:])


line = "[DEFAULT]"
file_data = ""

addLine(filename="global.ini", line=line)
addLine(filename="en/global.ini", line=line)

config_eng = ConfigParser(
    allow_no_value=True, comment_prefixes=None, delimiters=("="), interpolation=None
)
config_ger = ConfigParser(
    allow_no_value=True, comment_prefixes=None, delimiters=("="), interpolation=None
)
config_eng.read("en/global.ini", "utf_8_sig")
config_eng_section = config_eng["DEFAULT"]

config_ger.read("global.ini", "utf_8_sig")
config_ger_section = config_ger["DEFAULT"]

not_found_keys = {}

line = 1
for key in config_eng_section.keys():
    value = config_ger_section.get(key)
    if value == None:
        not_found_keys[line] = key
    line += 1

removeFirstLine("global.ini")
removeFirstLine("en/global.ini")

if len(not_found_keys):
    print(json.dumps(not_found_keys, indent=4))
    exit(1)
