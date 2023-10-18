from configparser import ConfigParser


def addLine(file, line):
    file_data = file.read()
    file.seek(0, 0)
    file.write(line + ("\n") + file_data)


def removeFirst(file):
    lines = file.readlines()
    file.seek(0, 0)
    file.truncate()
    file.writelines(lines[1:])


line = "[DEFAULT]"
file_data = ""
with open("global.ini", encoding="utf_8_sig", mode="r+") as file:
    addLine(file=file, line=line)
with open("en/global.ini", encoding="utf_8_sig", mode="r+") as file:
    addLine(file=file, line=line)

config_eng = ConfigParser(
    allow_no_value=True, comment_prefixes=(";"), delimiters=("="), interpolation=None
)
config_ger = ConfigParser(
    allow_no_value=True, comment_prefixes=(";"), delimiters=("="), interpolation=None
)
config_eng.read("en/global.ini", "utf_8_sig")
config_eng_section = config_eng["DEFAULT"]

config_ger.read("global.ini", "utf_8_sig")
config_ger_section = config_ger["DEFAULT"]

not_found_keys = []

for key in config_eng_section.keys():
    value = config_ger_section.get(key)
    if value == None:
        not_found_keys.append(key)


with open("global.ini", encoding="utf_8_sig", mode="r+") as file:
    removeFirst(file=file)
with open("en/global.ini", encoding="utf_8_sig", mode="r+") as file:
    removeFirst(file=file)

if len(not_found_keys):
    print(not_found_keys)
    exit(1)
