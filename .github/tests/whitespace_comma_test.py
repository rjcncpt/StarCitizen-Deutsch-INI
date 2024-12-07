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
            print("Test FAILED!")
            exit(1)
        else:
            print("There are no whitespaces before a comma.")
            print("Test PASSED!")

    except FileNotFoundError:
        print(f"File \"{file_path}\" was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
