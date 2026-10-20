import re

from helper import print_to_console, extract_keys_from_lines, get_argument_parser


def find_bad_lines(file_content: list[str], excluded_keys: list[str]) -> list[int]:
    """
    Find lines where a number is immediately followed by a percent sign.

    :param file_content: A list of strings representing the contents of a file.
    :param excluded_keys: A list of keys to ignore when checking.
    :return: A list of line numbers containing a number followed directly by "%".
    """
    bad_lines = []

    for line_number, line in enumerate(file_content, start=1):
        if line.startswith("#") or "=" not in line:
            continue

        current_key, value = line.split("=", 1)
        if current_key in excluded_keys:
            continue
        if re.search(r"\d%", value):
            bad_lines.append(line_number)

    return bad_lines


if __name__ == "__main__":
    parser, args = get_argument_parser()

    excluded_keys = [
        "dfm_ui_Minutes_unit_Seconds_To_Respawn",
    ]
    file_path = "live/global.ini"

    try:
        with open(file_path, "r", encoding="UTF-8-SIG") as file:
            content = file.readlines()
        bad_lines = find_bad_lines(content, excluded_keys)
        if bad_lines:
            keys_of_bad_lines = extract_keys_from_lines(content, bad_lines)
            for index, line_number in enumerate(bad_lines):
                print_to_console(
                    "Percent Test",
                    f"{keys_of_bad_lines[index]}: Number immediately followed by percent sign detected.",
                    file_path,
                    line_number,
                    "error",
                )
            print(
                f"\nFound {len(bad_lines)} line(s) with a number immediately followed by a percent sign."
            )
            if args.fail_on_error:
                exit(1)
        else:
            print("There are no numbers immediately followed by a percent sign.")
            print("Test PASSED!")

    except FileNotFoundError:
        print_to_console(
            "File not found",
            f'File "{file_path}" was not found.',
            file_path,
            0,
            "error",
        )
        if args.fail_on_error:
            exit(1)
    except Exception as e:
        print_to_console(
            "Percent Test", f"An error occurred: {e}", file_path, 0, "error"
        )
        if args.fail_on_error:
            exit(1)
