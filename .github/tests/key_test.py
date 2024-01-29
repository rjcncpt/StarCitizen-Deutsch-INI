import configparser


def keys_in_second_ini(first_file, second_file):
    # Parse the two ini files
    first_ini = configparser.ConfigParser()
    with open(first_file, 'r', encoding='UTF-8-SIG') as file:
        first_ini.read_string('[DEFAULT]\n' + file.read())

    second_ini = configparser.ConfigParser()
    with open(second_file, 'r', encoding='UTF-8-SIG') as file:
        second_ini.read_string('[DEFAULT]\n' + file.read())

    # Check that all keys in the first ini are present in the second
    for key in first_ini.defaults():
        if key not in second_ini.defaults():
            print(f"Key \"{key}\" missing from second ini.")
            return False
    return True


# Files to be checked
first_file = 'en/live/global.ini'
second_file = 'live/global.ini'

# Perform the check
if keys_in_second_ini(first_file, second_file):
    print('All keys are present.')
else:
    print('Some keys are missing.')
    exit(1)
