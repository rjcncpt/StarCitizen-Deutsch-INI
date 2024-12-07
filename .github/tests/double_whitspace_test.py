def find_bad_lines(file_content):
    """
    Find lines in the given file that have double whitespaces around commas or full stops.

    :param file_content: A list of strings representing the contents of a file.
    :return: A list of line numbers that contain double whitespaces around commas or full stops.
    """
    internal_bad_lines = []
    for i, line in enumerate(file_content, start=1):
        false_patterns = ["  .", ".  ", "  ,", ",  "]
        if any(x in line for x in false_patterns):
            # Ignore CIG's special char test line
            if not line.startswith("test_special_chars"):
                internal_bad_lines.append(i)

    return internal_bad_lines

def extract_keys_from_lines(file_content, line_numbers):
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
            if '=' in line:
                # Extract the key from the line
                key, _ = line.split('=', 1)
                keys.append(key.strip())

    return keys

if __name__ == "__main__":
    file_path = "live/global.ini"

    try:
        with open(file_path, "r", encoding="UTF-8-SIG") as file:
            content = file.readlines()
        bad_lines = find_bad_lines(content)
        if bad_lines:
            print("Following lines need to be checked:")
            keys_of_bad_lines = extract_keys_from_lines(content, bad_lines)
            print(bad_lines)
            for string in keys_of_bad_lines:
                print(string)
            print("Test FAILED!")
            exit(1)
        else:
            print("There are no double whitespaces.")
            print("Test PASSED!")

    except FileNotFoundError:
        print(f"File \"{file_path}\" was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")