from helper import print_to_console, extract_keys_from_lines


def find_bad_lines(file_content):
    """
    Find lines in the given file that have double whitespaces around commas or full stops.

    :param file_content: A list of strings representing the contents of a file.
    :return: A list of line numbers that contain double whitespaces around commas or full stops.
    """
    internal_bad_lines = []
    for i, line in enumerate(file_content, start=1):
        false_patterns = ["  .", ".  ", "  ,", ",  "]
        if any(x in line for x in false_patterns):
            # Ignore CIG's special char test line
            if not line.startswith("test_special_chars"):
                internal_bad_lines.append(i)

    return internal_bad_lines


if __name__ == "__main__":
    file_path = "live/global.ini"

    try:
        with open(file_path, "r", encoding="UTF-8-SIG") as file:
            content = file.readlines()
        bad_lines = find_bad_lines(content)
        if bad_lines:
            print("Double Whitespace Test FAILED!")
            print("Following lines need to be checked:")
            keys_of_bad_lines = extract_keys_from_lines(content, bad_lines)
            for index, line_number in enumerate(bad_lines):
                print_to_console(
                    "Double Whitespace Test",
                    f"Text contains double whitespace: {keys_of_bad_lines[index]}",
                    file_path,
                    line_number,
                    "error",
                )
            exit(1)
        else:
            print("There are no double whitespaces.")
            print("Test PASSED!")

    except FileNotFoundError:
        print_to_console(
            "Double Whitespace Test",
            f'File "{file_path}" was not found.',
            file_path,
            0,
            "error",
        )
    except Exception as e:
        print_to_console(
            "Double Whitespace Test", f"An error occurred: {e}", file_path, 0, "error"
        )
