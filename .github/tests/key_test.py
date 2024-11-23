from configparser import ConfigParser, Error as configparserError, DuplicateOptionError
import sys


def parse_error(file_path: str, error: configparserError):
    """
    Parses an error and generates an error message. Stops the execution with error.

    :param file_path: Path to a (ini) file (just for better output)
    :param error: The error thrown by the ConfigParser
    """
    if type(error) == DuplicateOptionError:
        sys.exit(
            f"Fehler in '{file_path}': Der Key '{error.args[1]}' in Zeile {error.args[3]-1} exisitert bereits."
        )
    else:
        sys.exit(f"Fehler in '{file_path}': '{error.message}'")


def keys_in_second_ini(first_file, second_file):
    """
    :param first_file: The path to the first ini file.
    :param second_file: The path to the second ini file.
    :return: True if all keys in the first ini file are present in the second ini file, False otherwise.
    """
    # Parse the two ini files
    try:
        first_ini = ConfigParser(allow_no_value=True, delimiters=("="))
        with open(first_file, "r", encoding="UTF-8-SIG") as file:
            first_ini.read_string("[DEFAULT]\n" + file.read())
    except configparserError as e:
        parse_error(first_file, e)

    try:
        second_ini = ConfigParser(allow_no_value=True, delimiters=("="))
        with open(second_file, "r", encoding="UTF-8-SIG") as file:
            second_ini.read_string("[DEFAULT]\n" + file.read())
    except configparserError as e:
        parse_error(second_file, e)

    # Check that all keys in the first ini are present in the second
    for key in first_ini.defaults():
        if key not in second_ini.defaults():
            print(f"Key '{key}' missing from {second_file}.")
            return False
    return True


# Files to be checked
eng_live_file = ".github/en/live/global.ini"
deu_live_file = "live/global.ini"
# eng_ptu_file = ".github/en/ptu/global.ini"
# deu_ptu_file = "ptu/global.ini"

exit_code = 0

# Perform the check
if keys_in_second_ini(eng_live_file, deu_live_file):
    print("All keys in LIVE are present.")
else:
    print("Some keys in LIVE are missing.")
    exit_code = 1

# if keys_in_second_ini(eng_ptu_file, deu_ptu_file):
#     print("All keys in PTU are present.")
# else:
#     print("Some keys in PTU are missing.")
#     exit_code = 1

exit(exit_code)
