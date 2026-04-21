import os

import chardet
from helper import print_to_console, get_argument_parser


def get_type(file: str) -> dict:
    """
    Determine the character encoding of a file.

    Reads the first 32 bytes of the file and uses chardet library to detect encoding.

    :param file: Path to the file to be analyzed.
    :return: Dictionary containing encoding detection info with keys "encoding", "confidence", and "language".
    """
    _bytes = min(32, os.path.getsize(file))
    raw = open(file, "rb").read(_bytes)
    return chardet.detect(raw)


if __name__ == "__main__":
    parser, args = get_argument_parser()

    file_eng_live = ".github/en/live/global.ini"
    file_deu_live = "live/global.ini"
    file_eng_ptu = ".github/en/ptu/global.ini"
    file_deu_ptu = "ptu/global.ini"

    type_eng_live = get_type(file_eng_live)
    type_deu_live = get_type(file_deu_live)

    exit_code = 0

    if type_eng_live["encoding"] != type_deu_live["encoding"]:
        print_to_console(
            "Encoding Mismatch",
            "The encoding between the english and german INI files differs!\n"
            f"Encoding ENG: {type_eng_live['encoding']}\n"
            f"Encoding DEU: {type_deu_live['encoding']}",
            file_deu_live,
            0,
            "error",
        )
        if args.fail_on_error:
            exit_code = 1
    else:
        print("The encoding between the LIVE files matches.\nTest PASSED!")

    exit(exit_code)
