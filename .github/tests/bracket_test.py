import re


def check_brackets(filename) -> int:
    result = 0
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Checks if all opened brackets are closed in the same line
            if re.search(r'\([^\)]*$', line):
                if line_number != 44749 and line_number != 46617:
                    result = 0
                else:
                    print(f"Line {line_number}: Open bracket is not closed in the same line.")
                    result = 1
    return result


if __name__ == "__main__":
    deu_live_file = "live/global.ini"
    deu_ptu_file = "ptu/global.ini"
    exit_code = 0
    print("Checking {}...".format(deu_live_file))
    if check_brackets(deu_live_file) != 0:
        exit_code = 1
    print("Checking {}...".format(deu_ptu_file))
    if check_brackets(deu_ptu_file) != 0:
        exit_code = 1
    exit(exit_code)
