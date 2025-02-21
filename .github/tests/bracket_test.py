import os
import re


def check_brackets(filename, excluded):
    """
    :param filename: The name of the file to check for bracket matching.
    :param excluded: A list of keys to exclude from checking.
    :return: None

    The check_brackets method reads the contents of the given file and checks for matching brackets. It skips the lines specified in the 'excluded' parameter. If any mismatched or unclosed
    * brackets are found, an error message is printed with the line number.

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
                    r"\d\.\)|\s[a-z]\)|:\)", "", line
                )  # This regex should filter all "1.)" "a)" and ":)" parts.

                bracket_stack = []
                for char in clean_line:
                    if char == "(":
                        bracket_stack.append(char)
                    elif char == ")":
                        try:
                            bracket_stack.pop()
                        except IndexError:
                            print(
                                f"::warning file={filename},line={line_number}:: {filename}:{line_number} / {current_key}: Extra closing bracket detected."
                            )
                            break

                if bracket_stack:
                    print(
                        f"::warning file={filename},line={line_number}:: {filename}:{line_number} / {current_key}: Open bracket is not closed."
                    )


if __name__ == "__main__":
    excluded_keys = [
        "ea_ui_player_count_bracket_left",
        "ea_ui_player_count_bracket_right",
        "input_key_keyboard_leftParenthesis,P",
        "input_key_keyboard_rightParenthesis,P",
        "hurston_intro_desc",  # Aufzählung
        "strawberry_A_datapad_notes",  # Emoji
    ]
    deu_live_file = "live/global.ini"
    deu_ptu_file = "ptu/global.ini"

    print()

    if os.path.exists(deu_live_file):
        print(f"Checking {deu_live_file}...")
        check_brackets(deu_live_file, excluded_keys)
    else:
        print(f"Skipping {deu_live_file}: File not found.")

    print()

    if os.path.exists(deu_ptu_file):
        print(f"Checking {deu_ptu_file}...")
        check_brackets(deu_ptu_file, excluded_keys)
    else:
        print(f"Skipping {deu_ptu_file}: File not found.")
