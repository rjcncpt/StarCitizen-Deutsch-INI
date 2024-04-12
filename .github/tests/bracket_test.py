import re


def check_brackets(filename, excluded):
    """
    :param filename: The name of the file to check for bracket matching.
    :param excluded: A list of line numbers to exclude from checking.
    :return: None

    The check_brackets method reads the contents of the given file and checks for matching brackets. It skips the lines specified in the 'excluded' parameter. If any mismatched or unclosed
    * brackets are found, an error message is printed with the line number.

    Example usage:

    check_brackets('file.txt', [3, 5, 7])

    This will check the contents of 'file.txt' for bracket matching, excluding lines 3, 5, and 7.
    """
    with open(filename, 'r', encoding="UTF-8-SIG") as file:
        for line_number, line in enumerate(file, start=1):
            if line_number not in excluded:
                # Remove enumerations and smileys
                clean_line = re.sub(r'\d\.\)|\s[a-z]\)|:\)', '', line)  # This regex should filter all "1.)" "a)" and ":)" parts.

                bracket_stack = []
                for char in clean_line:
                    if char == '(':
                        bracket_stack.append(char)
                    elif char == ')':
                        try:
                            bracket_stack.pop()
                        except IndexError:
                            print(f"Line {line_number}: Extra closing bracket detected.")
                            break

                if bracket_stack:
                    print(f"Line {line_number}: Open bracket is not closed.")


if __name__ == "__main__":
    excluded_lines_live = [41119, 44802, 44803, 46672, 46709, 46152]
    excluded_lines_ptu = [41610, 45442, 45443, 47387, 47424, 46865]
    deu_live_file = "live/global.ini"
    deu_ptu_file = "ptu/global.ini"
    print()
    print(f"Checking {deu_live_file}...")
    check_brackets(deu_live_file, excluded_lines_live)
    print()
    print(f"Checking {deu_ptu_file}...")
    check_brackets(deu_ptu_file, excluded_lines_ptu)
