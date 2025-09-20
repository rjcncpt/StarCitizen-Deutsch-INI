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
