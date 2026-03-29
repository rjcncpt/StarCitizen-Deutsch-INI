from helper import print_to_console


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
    file_path = "live/global.ini"

    try:
        with open(file_path, "r", encoding="UTF-8-SIG") as file:
            content = file.readlines()
        bad_lines = find_bad_lines(content)
        if bad_lines:
            print("Following lines need to be checked:")
            print(bad_lines)
            print_to_console(
                "Whitespace Comma Test",
                f"Test FAILED! Lines: {bad_lines}",
                file_path,
                0,
                "error",
            )
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
    except Exception as e:
        print_to_console(
            "An error occurred", f"An error occurred: {e}", file_path, 0, "error"
        )
