import argparse

from helper import print_to_console, extract_keys_from_lines


def find_bad_lines(file_content):
    """
    Find lines in the given file that have a comma with a space before it.

    :param file_content: A list of strings representing the contents of a file.
    :return: A list of line numbers that contain a comma with a space before it.
    """
    internal_bad_lines = []

    for i, line in enumerate(file_content, start=1):
        if " ," in line:
            # Ignore CIG's special char test line
            if not line.startswith("test_special_chars"):
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

    try:
        with open(file_path, "r", encoding="UTF-8-SIG") as file:
            content = file.readlines()
        bad_lines = find_bad_lines(content)
        if bad_lines:
            keys = extract_keys_from_lines(content, bad_lines)

            for index, line_number in enumerate(bad_lines):
                print_to_console(
                    "Whitespace Comma Test",
                    f"{keys[index]}: Whitespace before comma detected.",
                    file_path,
                    line_number,
                    "error",
                )

            if args.fail_on_error:
                exit(1)
        else:
            print("There are no whitespaces before a comma.")
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
            "An error occurred", f"An error occurred: {e}", file_path, 0, "error"
        )
        if args.fail_on_error:
            exit(1)
