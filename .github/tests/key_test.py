from configparser import ConfigParser, DuplicateOptionError
from configparser import Error as configparserError
from helper import print_to_console, get_argument_parser


def parse_error(file_path: str, error: configparserError) -> None:
    """
    Parse a ConfigParser error and print a formatted error message.

    :param file_path: Path to a (ini) file (just for better output).
    :param error: The error thrown by the ConfigParser.
    :return: None
    """
    if type(error) is DuplicateOptionError:
        print_to_console(
            "Duplicate Key Error",
            f"{error.args[1]}: Key exisitert bereits.",
            file_path,
            error.args[3] - 1,
            "error",
        )
    else:
        print_to_console(
            "Ini Read Error",
            f"Fehler in '{file_path}': '{error.message}'",
            file_path,
            0,
            "error",
        )


def test_duplicate_keys() -> bool:
    """
    Test that there are no duplicate keys in the ini files.

    Checks both English and German INI files for duplicate keys.
    If duplicates are found, prints error messages and returns False.

    :param: None
    :return: True if test passed, False if duplicates were found.
    """
    files_to_check = [
        ".github/en/live/global.ini",
        "live/global.ini",
    ]

    for file in files_to_check:
        try:
            with open(file, "r", encoding="UTF-8-SIG") as f:
                content = f.read()
                parser = ConfigParser(
                    allow_no_value=True, delimiters=("="), strict=True
                )
                parser.read_string("[DEFAULT]\n" + content)
        except configparserError as e:
            parse_error(file, e)
            return False
    return True


def keys_in_second_ini(first_file: str, second_file: str) -> bool:
    """
    Check if all keys from the first ini file are present in the second ini file.

    Parses both files and verifies that every key from the first file exists in the second.

    :param first_file: The path to the first ini file.
    :param second_file: The path to the second ini file.
    :return: True if all keys in the first ini file are present in the second ini file, False otherwise.
    """
    # Parse the two ini files
    try:
        first_ini = ConfigParser(allow_no_value=True, delimiters=("="), strict=False)
        with open(first_file, "r", encoding="UTF-8-SIG") as file:
            first_ini.read_string("[DEFAULT]\n" + file.read())
    except configparserError as e:
        parse_error(first_file, e)

    try:
        second_ini = ConfigParser(allow_no_value=True, delimiters=("="), strict=False)
        with open(second_file, "r", encoding="UTF-8-SIG") as file:
            second_ini.read_string("[DEFAULT]\n" + file.read())
    except configparserError as e:
        parse_error(second_file, e)

    # Check that all keys in the first ini are present in the second
    for key in first_ini.defaults():
        if key not in second_ini.defaults():
            print_to_console(
                "Key Missing",
                f"Key '{key}' missing from {second_file}.",
                second_file,
                0,
                "error",
            )
            return False
    return True


if __name__ == "__main__":
    parser, args = get_argument_parser()

    # Files to be checked
    eng_live_file = ".github/en/live/global.ini"
    deu_live_file = "live/global.ini"

    has_errors = False

    # Perform the check
    if keys_in_second_ini(eng_live_file, deu_live_file):
        print("All keys in LIVE are present.")
    else:
        has_errors = True

    # Perform duplicate key check
    if test_duplicate_keys():
        print("No duplicate keys found.")
    else:
        has_errors = True

    if has_errors and args.fail_on_error:
        exit(1)

    if not has_errors:
        print("Test PASSED!")
