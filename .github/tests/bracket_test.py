import re


def check_brackets(filename):
    """
    :param filename: The name of the file to be checked for balanced brackets.
    :return: None

    This method checks if the brackets in a given file are balanced. It reads through each line of the file, strips any enumerations and smileys, and then checks if the brackets are balanced.

    If a line contains an extra closing bracket that is not matched with an opening bracket, it will print a message indicating the line number and the issue.

    If a line has an open bracket that is not closed, it will also print a message indicating the line number and the issue.

    Note: The method does not return any value. It directly prints the error messages.

    Example usage:
    check_brackets("example.txt")
    """
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number != 44749 and line_number != 44750 and line_number != 46617 and line_number != 46654:
                # Remove enumerations and smileys
                clean_line = re.sub(r'\d\.*\)|\s[a-z]\)|:\)', '', line)

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
    deu_live_file = "live/global.ini"
    deu_ptu_file = "ptu/global.ini"
    print("")
    print("Checking {}...".format(deu_live_file))
    check_brackets(deu_live_file)
    print("")
    print("Checking {}...".format(deu_ptu_file))
    check_brackets(deu_ptu_file)
