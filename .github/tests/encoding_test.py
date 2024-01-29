import os
import chardet


def get_type(file):
    """
    Determines the character encoding of a file.

    :param file: Path to the file to be analyzed.
    :type file: str
    :return: Dictionary containing information about the character encoding.
             The dictionary has keys "encoding", "confidence", and "language".
             The "encoding" key represents the character encoding,
             the "confidence" key represents the confidence level of the detection,
             and the "language" key represents the detected language.
    :rtype: dict
    """
    _bytes = min(32, os.path.getsize(file))
    raw = open(file, "rb").read(_bytes)
    return chardet.detect(raw)


filename_eng = "en/live/global.ini"
filename_ger = "live/global.ini"

type_eng = get_type(filename_eng)
type_ger = get_type(filename_ger)

if type_ger != type_eng:
    print(f"Enc. eng: {type_eng["encoding"]}\nEnc. ger: {type_ger["encoding"]}")
    exit(1)
