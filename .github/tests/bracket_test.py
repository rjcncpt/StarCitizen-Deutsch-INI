import re


def check_brackets(filename):
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Checks if all opened brackets are closed in the same line
            if re.search(r'\([^\)]*$', line):
                if line_number != 44749 or line_number != 46617:
                    print(f"Line {line_number}: Open bracket is not closed in the same line.")


if __name__ == "__main__":
    deu_live_file = "live/global.ini"
    deu_ptu_file = "ptu/global.ini"
    print("Checking {}...".format(deu_live_file))
    check_brackets(deu_live_file)
    print("Checking {}...".format(deu_ptu_file))
    check_brackets(deu_ptu_file)
