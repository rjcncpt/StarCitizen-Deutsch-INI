import argparse
import re

from helper import print_to_console, extract_keys_from_lines


def find_bad_lines(file_content: list[str], excluded_keys: list[str]) -> list[int]:
    """
    Find lines in the given file where a lowercase n appears before a capital letter
    without a preceding backslash, only in the value part of INI entries.

    :param file_content: A list of strings representing the contents of a file.
    :param excluded_keys: A list of keys to ignore while checking.
    :return: A list of line numbers that contain the invalid pattern.
    """
    internal_bad_lines = []
    invalid_pattern = re.compile(r" (?<!\\)n[A-Z]")

    for i, line in enumerate(file_content, start=1):
        key = line.split("=", 1)[0].strip()
        if key in excluded_keys:
            continue

        value = line.split("=", 1)[1] if "=" in line else line
        if invalid_pattern.search(value):
            internal_bad_lines.append(i)

    return internal_bad_lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fail-on-error",
        action="store_true",
        help="Exit with code 1 if errors are found",
    )
    args, unknown = parser.parse_known_args()

    file_path = "live/global.ini"
    excluded_keys = ["item_DescFlair_Poster_nVidia"]

    try:
        with open(file_path, "r", encoding="UTF-8-SIG") as file:
            content = file.readlines()

        bad_lines = find_bad_lines(content, excluded_keys)
        if bad_lines:
            keys = extract_keys_from_lines(content, bad_lines)
            for index, line_number in enumerate(bad_lines):
                print_to_console(
                    "N Character Escaping Test",
                    f"{keys[index]}: Unescaped 'n' before a capital letter detected",
                    file_path,
                    line_number,
                    "error",
                )
            if args.fail_on_error:
                exit(1)
        else:
            print("There are no unescaped 'n' characters before a capital letter.")
            print("Test PASSED!")

    except FileNotFoundError:
        print_to_console(
            "N Character Escaping Test",
            f'File "{file_path}" was not found.',
            file_path,
            0,
            "error",
        )
        if args.fail_on_error:
            exit(1)
    except Exception as e:
        print_to_console(
            "N Character Escaping Test",
            f"An error occurred: {e}",
            file_path,
            0,
            "error",
        )
        if args.fail_on_error:
            exit(1)
