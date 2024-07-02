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


file_eng_live = ".github/en/live/global.ini"
file_deu_live = "live/global.ini"
file_eng_ptu = ".github/en/ptu/global.ini"
file_deu_ptu = "ptu/global.ini"

type_eng_live = get_type(file_eng_live)
type_deu_live = get_type(file_deu_live)
# type_eng_ptu = get_type(file_eng_ptu)
# type_deu_ptu = get_type(file_deu_ptu)

exit_code = 0

if type_eng_live["encoding"] != type_deu_live["encoding"]:
    print("The encoding between the LIVE INI files differs!")
    print(f"Encoding ENG: {type_eng_live['encoding']}")
    print(f"Encoding DEU: {type_deu_live['encoding']}")
    exit_code = 1
else:
    print("The encoding between the LIVE files matches.")

# if type_eng_ptu["encoding"] != type_deu_ptu["encoding"]:
#     print("The encoding between the PTU INI files differs!")
#     print(f"Encoding ENG: {type_eng_ptu['encoding']}")
#     print(f"Encoding DEU: {type_deu_ptu['encoding']}")
#     exit_code = 1
# else:
#     print("The encoding between the PTU files matches.")

exit(exit_code)
