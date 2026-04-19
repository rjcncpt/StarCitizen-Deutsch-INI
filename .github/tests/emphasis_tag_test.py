import re

from helper import print_to_console, extract_keys_from_lines, get_argument_parser


def find_bad_lines(file_content: list[str], ignored_lines: list[str]) -> list[int]:
    """
    Find lines in the given file that have improperly used emphasis tags (<EMx> and </EMx>).

    Checks for unmatched, incorrectly nested, or malformed emphasis tags.

    :param file_content: A list of strings representing the contents of a file.
    :param ignored_lines: A list of keys to ignore when checking.
    :return: A list of line numbers that contain bad emphasis tags.
    """
    internal_bad_lines = []
    tag_pattern = re.compile(r"</?EM(\d+)>")

    for i, line in enumerate(file_content, start=1):
        # Extract key and check if it should be ignored
        current_key = line.split("=")[0]
        if current_key in ignored_lines:
            continue

        # Find all tags in the line
        tags = tag_pattern.findall(line)
        stack = []

        for tag in tag_pattern.finditer(line):
            tag_num = tag.group(1)
            if tag.group(0).startswith("<EM"):  # Opening tag
                stack.append(tag_num)
            elif tag.group(0).startswith("</EM"):  # Closing tag
                if not stack or stack[-1] != tag_num:
                    internal_bad_lines.append(i)
                    break
                stack.pop()

        # If stack is not empty, there are unclosed tags
        if stack:
            internal_bad_lines.append(i)

    return internal_bad_lines


if __name__ == "__main__":
    parser, args = get_argument_parser()

    ignored_lines = [
        "text_ui_tags_EM1_close,P",
        "text_ui_tags_EM1_open,P",
        "text_ui_tags_EM2_close,P",
        "text_ui_tags_EM2_open,P",
        "text_ui_tags_EM3_close,P",
        "text_ui_tags_EM3_open,P",
        "text_ui_tags_EM4_close,P",
        "text_ui_tags_EM4_open,P",
        "text_ui_tags_EM5_close,P",
        "text_ui_tags_EM5_open,P",
    ]

    file_path = "live/global.ini"

    try:
        with open(file_path, "r", encoding="UTF-8-SIG") as file:
            content = file.readlines()
        bad_lines = find_bad_lines(content, ignored_lines)
        if bad_lines:
            keys_of_bad_lines = extract_keys_from_lines(content, bad_lines)
            for index, line_number in enumerate(bad_lines):
                print_to_console(
                    "Emphasis Tag Test",
                    f"{keys_of_bad_lines[index]}: Improperly used emphasis tags detected.",
                    file_path,
                    line_number,
                    "error",
                )
            if args.fail_on_error:
                exit(1)
        else:
            print("All emphasis tags are properly used.")
            print("Test PASSED!")

    except FileNotFoundError:
        print_to_console(
            "Emphasis Tag Test",
            f'File "{file_path}" was not found.',
            file_path,
            0,
            "error",
        )
