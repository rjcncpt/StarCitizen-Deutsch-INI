import sys

severities = {
    "error": "::error",
    "warning": "::warning",
    "notice": "::notice",
}


def print_to_console(title, message, file, line_number, severity):
    """
    :param message: The message to print to the console.
    :param file: The name of the file that the message is related to.
    :param line_number: The line number that the message is related to.
    :param severity: The severity of the message. Must be one of the following: "error", "warning", "notice".
    :return: None

    The print_to_console method prints a message to the console in the format that GitHub Actions expects for annotations. This method is used to print error messages for bracket mismatches.

    Example usage:

    print_to_console("Extra closing bracket detected.", "file.txt", 5, "error")

    This will print the message "Extra closing bracket detected." for the file "file.txt" on line 5 with an error severity.
    """
    if len(sys.argv) > 1 and "github" in sys.argv[1]:
        print(
            f"{severities[severity]} title={title},file={file},line={line_number}:: {message}"
        )
    else:
        print(f"{message}")


def extract_keys_from_lines(file_content, line_numbers):
    """
    Extract keys from specific lines in the file content.

    This function scans specified lines in the provided file content to identify and extract keys.
    A key is considered to be the part before the '=' character in a line.

    :param file_content: A list of strings, where each string represents a line from the file.
    :param line_numbers: A list of integers, where each integer is a line number from which to extract a key.
                         Line numbers are 1-based, meaning the first line is line number 1.
    :return: A list of strings representing the keys extracted from the specified lines.
             If a line does not have an '=', no key is extracted from that line.
    """
    keys = []
    # Iterate through the given line numbers
    for line_number in line_numbers:
        line_number = line_number - 1
        # Ensure the line number is within range
        if 0 <= line_number < len(file_content) - 1:
            line = file_content[line_number].strip()
            if "=" in line:
                # Extract the key from the line
                key, _ = line.split("=", 1)
                keys.append(key.strip())

    return keys
