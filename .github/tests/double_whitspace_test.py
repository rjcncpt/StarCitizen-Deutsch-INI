from helper import print_to_console, extract_keys_from_lines, get_argument_parser


def find_bad_lines(file_content: list[str], ignored_lines: list[str]) -> list[int]:
    """
    Find lines in the given file that have double whitespaces (except indentation after
    \n which represents indentation of embedded newlines).

    :param file_content: A list of strings representing the contents of a file.
    :param ignored_lines: A list of keys to ignore when checking.
    :return: A list of line numbers that contain bad whitespaces.
    """
    internal_bad_lines = []
    for i, line in enumerate(file_content, start=1):
        # Extract key and check if it should be ignored
        current_key = line.split("=")[0]
        if current_key in ignored_lines:
            continue

        # Check for any multiple consecutive spaces within text
        # Split by \n to check each logical line separately
        # Allow spaces after \n (indentation of newlines)
        for part in line.split("\\n"):
            stripped_part = part.lstrip()
            if "  " in stripped_part:
                internal_bad_lines.append(i)
                break

    return internal_bad_lines


if __name__ == "__main__":
    parser, args = get_argument_parser()

    ignored_lines = [
        "test_special_chars",
        "cockpit_screen_loading",
        "ui_hacking_terminal_command_move_desc",
        "ui_hacking_terminal_command_move_invalid_arg_",
        "ui_hacking_terminal_command_swap_desc",
    ]

    file_path = "live/global.ini"

    try:
        with open(file_path, "r", encoding="UTF-8-SIG") as file:
            content = file.readlines()
        bad_lines = find_bad_lines(content, ignored_lines)
        if bad_lines:
            keys_of_bad_lines = extract_keys_from_lines(content, bad_lines)
            for index, line_number in enumerate(bad_lines):
                print_to_console(
                    "Double Whitespace Test",
                    f"{keys_of_bad_lines[index]}: Multiple consecutive whitespaces detected.",
                    file_path,
                    line_number,
                    "error",
                )
            if args.fail_on_error:
                exit(1)
        else:
            print("There are no multiple consecutive whitespaces.")
            print("Test PASSED!")

    except FileNotFoundError:
        print_to_console(
            "Double Whitespace Test",
            f'File "{file_path}" was not found.',
            file_path,
            0,
            "error",
        )
        if args.fail_on_error:
            exit(1)
    except Exception as e:
        print_to_console(
            "Double Whitespace Test", f"An error occurred: {e}", file_path, 0, "error"
        )
        if args.fail_on_error:
            exit(1)
