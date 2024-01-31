import re


def check_brackets(filename) -> int:
    result = 0

    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number == 44749 or line_number == 44750:
                break
            # Remove enumerations and smileys
            clean_line = re.sub(r'\d\.\)|\s[a-z]\)|:\)', '', line)

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
                result = 1

    return result


if __name__ == "__main__":
    deu_live_file = "live/global.ini"
    deu_ptu_file = "ptu/global.ini"
    exit_code = 0
    print("")
    print("Checking {}...".format(deu_live_file))
    if check_brackets(deu_live_file) != 0:
        exit_code = 1
    print("")
    print("Checking {}...".format(deu_ptu_file))
    if check_brackets(deu_ptu_file) != 0:
        exit_code = 1
    exit(exit_code)
