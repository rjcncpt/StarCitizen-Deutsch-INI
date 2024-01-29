import configparser


def keys_in_second_ini(first_file, second_file):
    """
    :param first_file: The path to the first ini file.
    :param second_file: The path to the second ini file.
    :return: True if all keys in the first ini file are present in the second ini file, False otherwise.
    """
    # Parse the two ini files
    first_ini = configparser.ConfigParser()
    with open(first_file, "r", encoding="UTF-8-SIG") as file:
        first_ini.read_string("[DEFAULT]\n" + file.read())

    second_ini = configparser.ConfigParser()
    with open(second_file, "r", encoding="UTF-8-SIG") as file:
        second_ini.read_string("[DEFAULT]\n" + file.read())

    # Check that all keys in the first ini are present in the second
    for key in first_ini.defaults():
        if key not in second_ini.defaults():
            print(f"Key \"{key}\" missing from {second_file}.")
            return False
    return True


# Files to be checked
eng_live_file = "en/live/global.ini"
ger_live_file = "live/global.ini"
eng_ptu_file = "en/ptu/global.ini"
ger_ptu_file = "ptu/global.ini"

# Perform the check
if keys_in_second_ini(eng_live_file, ger_live_file):
    print("All keys in LIVE are present.")
elif keys_in_second_ini(eng_ptu_file, ger_ptu_file):
    print("All keys in PTU are present.")
else:
    print("Some keys are missing.")
    exit(1)
