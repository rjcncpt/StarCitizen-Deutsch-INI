import os
import re
import sys

severities = {
    "error": "::error",
    "warning": "::warning",
    "notice": "::notice",
}


def print_to_console(message, file, line_number, severity):
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
            f"{severities[severity]} title=Bracket Test,file={file},line={line_number}:: {message}"
        )
    else:
        print(f"{message}")


def check_brackets(filename, excluded):
    """
    :param filename: The name of the file to check for bracket matching.
    :param excluded: A list of keys to exclude from checking.
    :return: None

    The check_brackets method reads the contents of the given file and checks for matching brackets. It skips the lines which beginn with keys specified in the 'excluded' parameter. If any mismatched or unclosed brackets are found, an error message is printed with the line number.

    Example usage:

    check_brackets('file.txt', [3, 5, 7])

    This will check the contents of 'file.txt' for bracket matching, excluding lines 3, 5, and 7.
    """
    with open(filename, "r", encoding="UTF-8-SIG") as file:
        for line_number, line in enumerate(file, start=1):
            current_key = line.split("=")[0]
            if current_key not in excluded:
                # Remove enumerations and smileys
                clean_line = re.sub(
                    r"\d\.\)|\s[a-z]\)|:\)|;\)", "", line
                )  # This regex should filter all "1.)" "a)" ";)" and ":)" parts.

                bracket_stack = []
                for char in clean_line:
                    if char == "(":
                        bracket_stack.append(char)
                    elif char == ")":
                        try:
                            bracket_stack.pop()
                        except IndexError:
                            print_to_console(
                                f"{filename}:{line_number} / {current_key}: Extra closing bracket detected.",
                                filename,
                                line_number,
                                "error",
                            )
                            break

                if bracket_stack:
                    print_to_console(
                        f"{filename}:{line_number} / {current_key}: Open bracket is not closed.",
                        filename,
                        line_number,
                        "error",
                    )


if __name__ == "__main__":
    excluded_keys = [
        "ea_ui_player_count_bracket_left",
        "ea_ui_player_count_bracket_right",
        "input_key_keyboard_leftParenthesis,P",
        "input_key_keyboard_rightParenthesis,P",
        "hurston_intro_desc",
        "item_Descbehr_glauncher_ballistic_01_shin",
        "item_Descbehr_glauncher_ballistic_01_mat01",
        "item_Descbehr_glauncher_ballistic_01_imp01",
        "item_Descbehr_glauncher_ballistic_01_cen01",
        "item_Descbehr_glauncher_ballistic_01_black01",
        "item_Descbehr_glauncher_ballistic_01",
        "hathor_laser_datapad_008_text",  # Aufzählung
    ]
    deu_live_file = "live/global.ini"
    deu_ptu_file = "ptu/global.ini"

    print()

    if os.path.exists(deu_live_file):
        print(f"Checking {deu_live_file}...")
        check_brackets(deu_live_file, excluded_keys)
    else:
        print_to_console(
            f"Skipping {deu_live_file}: File not found.", deu_live_file, 0, "warning"
        )

    print()

    if os.path.exists(deu_ptu_file):
        print(f"Checking {deu_ptu_file}...")
        check_brackets(deu_ptu_file, excluded_keys)
    else:
        print_to_console(
            f"Skipping {deu_ptu_file}: File not found.", deu_ptu_file, 0, "warning"
        )
