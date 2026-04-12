import argparse

severities = {
    "error": "::error",
    "warning": "::warning",
    "notice": "::notice",
}


def print_to_console(
    title: str, message: str, file: str, line_number: int, severity: str
) -> None:
    """
    Print a message to the console in GitHub Actions or VS Code format.

    Formats the output based on context: GitHub Actions annotation format or VS Code format.

    :param title: The title of the message.
    :param message: The message to print to the console.
    :param file: The name of the file that the message is related to.
    :param line_number: The line number that the message is related to.
    :param severity: The severity of the message. Must be one of: "error", "warning", "notice".
    :return: None
    """
    parser, args = get_argument_parser()
    if args.github:
        print(
            f"{severities[severity]} title={title},file={file},line={line_number}:: {message}"
        )
    else:
        print(f"{file}:{line_number} | {message}")


def extract_keys_from_lines(
    file_content: list[str], line_numbers: list[int]
) -> list[str]:
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


def get_argument_parser() -> tuple[argparse.ArgumentParser, argparse.Namespace]:
    """
    Create and return a standardized argument parser for all scripts.

    :return: A tuple containing the parser and parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fail-on-error",
        action="store_true",
        help="Exit with code 1 if errors are found",
    )
    parser.add_argument(
        "--github",
        action="store_true",
        help="Use GitHub Actions annotation format for console output",
    )

    args, unknown = parser.parse_known_args()
    return parser, args
