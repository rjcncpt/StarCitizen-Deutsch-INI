import re


def check_brackets_balance(line):
    count_open = 0
    count_close = 0
    pattern = r'[a-zA-Z0-9]\.\)'

    for char in line:
        if char == '(':
            count_open += 1
        elif char == ')' and not re.search(pattern, char):
            if re.search(pattern, char):
                count_close += 1

    return count_open == count_close


def find_unbalanced_lines(file_content):
    unbalanced_lines_result = []

    for i, line in enumerate(file_content, start=1):
        if not check_brackets_balance(line):
            unbalanced_lines_result.append(i)

    return unbalanced_lines_result


if __name__ == "__main__":
    deu_live_file = "live/global.ini"
    deu_ptu_file = "ptu/global.ini"
    error_code = 0

    try:
        with open(deu_live_file, 'r', encoding='UTF-8-SIG') as file:
            content = file.readlines()
        
        unbalanced_lines = find_unbalanced_lines(content)

        if not unbalanced_lines:
            print(f"All opened brackets are closed in file {deu_live_file}")
            error_code = 0
        else:
            print(f"The following lines have a mismatching number of opened and closed brackets in file {deu_live_file}:")
            print(unbalanced_lines)
            error_code = 1

    except FileNotFoundError:
        print(f"File not found: {deu_live_file}")
    except Exception as e:
        print(f"An error occured: {e}")

    try:
        with open(deu_ptu_file, 'r', encoding='UTF-8-SIG') as file:
            content = file.readlines()

        unbalanced_lines = find_unbalanced_lines(content)

        if not unbalanced_lines:
            print(f"All opened brackets are closed in file {deu_ptu_file}")
            error_code = 0
        else:
            print(f"The following lines have a mismatching number of opened and closed brackets in file {deu_ptu_file}:")
            print(unbalanced_lines)
            error_code = 1

    except FileNotFoundError:
        print(f"File not found: {deu_ptu_file}")
    except Exception as e:
        print(f"An error occured: {e}")

    exit(error_code)
