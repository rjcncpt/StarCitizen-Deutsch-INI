#!/usr/bin/env python3
import codecs
import re
import subprocess
import shutil
import logging

# The following paths need to fit your setup
exe_path = "unp4k/unp4k.exe"  # Path to the unp4k.exe
argument_data = "C:/Program Files/Roberts Space Industries/StarCitizen/EPTU/Data.p4k"  # Path to the Data.p4k

# The following paths are internally used and do not need to be edited, but can be edited
data_path = "Data"  # Temporary directory used by unp4k, that will be deleted at the end of the script
input_file_path = data_path + "/Localization/english/global.ini"  # Relative path to the extracted global.ini. Also used als filter argument for unp4k.
output_file_path = "global.ini"  # Path where the fixed global.ini will be saved

# Define your replacements here
replacements = {
    "Oxygen_Screen_ ErrorButtonMessage=": "Oxygen_Screen_ErrorButtonMessage=",
    "Tut03_Part01_Obj01b_ToStation =": "Tut03_Part01_Obj01b_ToStation=",
    "ea_ui_matchmaking_error_CanceledByService =": "ea_ui_matchmaking_error_CanceledByService=",
    "seachbody_obj_short_02a=": "searchbody_obj_short_02a=",
    "shop_ui_transactionResult_04 _InvalidPlayerInventoryId=": "shop_ui_transactionResult_04_InvalidPlayerInventoryId=",
    "shop_ui_transactionResult_05 _InventoryContainerRequestFail=": "shop_ui_transactionResult_05_InventoryContainerRequestFail=",
    "shop_ui_transactionResult_06 _InventoryItemFail=": "shop_ui_transactionResult_06_InventoryItemFail=",
    "~(Contractor": "~mission(Contractor",
    "~misssion(Item)": "~mission(Item)",
    "~mission (description)": "~mission(description)",
    "~mission (title)": "~mission(title)",
    "~mission (item)": "~mission(item)"
}


# Runs an exe file with the given arguments
def run_exe(exe_path, args):
    """
    Run the specified executable with the given arguments.

    :param exe_path: The path to the executable to be run.
    :type exe_path: str
    :param args: The arguments to be passed to the executable.
    :type args: List[str]
    :return: None
    :rtype: None
    """
    command = [exe_path] + args
    try:
        subprocess.run(command, check=True)
        logging.info("The executable %s has been started successfully.", exe_path)
    except subprocess.CalledProcessError as e:
        logging.error("The executable %s failed to run. Error: %s ", exe_path, str(e))
    except FileNotFoundError:
        logging.error("The executable %s does not exist.", exe_path)
    except Exception as e:
        logging.error("An error occurred while running the executable %s: %s", exe_path, str(e))


# Fixes the corrupted NBSP and writes the result in a temporary file
def fix_ini(input_file_path, output_file_path):
    """
    Fixes an INI file by replacing specific characters and writing the fixed content to a new file.

    :param input_file_path: The path to the input INI file.
    :param output_file_path: The path to the output fixed INI file.
    :return: None

    The method reads the content of the input INI file, replaces specific characters, and writes the fixed content to the output file. It also logs the success or failure of the operation
    *.

    Example usage:

    fix_ini("input.ini", "output.ini")
    """
    try:
        with open(input_file_path, "rb") as file:
            content = file.read()

        replacement = re.sub(b"(?<!\xc2)\xa0", b"\xc2\xa0", content)
        original_text = codecs.decode(replacement, "UTF-8-SIG")
        for old_text, new_text in replacements.items():
            original_text = original_text.replace(old_text, new_text)

        with codecs.open(output_file_path, "w", "UTF-8-SIG") as outfile:
            outfile.write(original_text)

        logging.info("Successfully fixed variables and wrote file as UTF-8-BOM to %s", output_file_path)

    except Exception as e:
        logging.error("An error occurred while fixing the INI file: %s", str(e))


def delete_dir(dir_path):
    """
    Deletes a directory specified by `dir_path`.

    :param dir_path: The path of the directory to be deleted.
    :return: None

    This method attempts to delete the directory specified by `dir_path`.
    If the directory is deleted successfully, an info log is generated.
    If the directory does not exist, an error log is generated.
    If there is a permission error while deleting the directory, an error log is generated.
    If any other error occurs, an error log is generated with the error message.
    """
    try:
        shutil.rmtree(dir_path)
        logging.info("The directory %s has been deleted successfully.", dir_path)
    except FileNotFoundError:
        logging.error("The directory %s does not exist.", dir_path)
    except PermissionError:
        logging.error("Permission denied for deleting the directory %s.", dir_path)
    except OSError as e:
        logging.error("Error: %s - %s", e.filename, e.strerror)
    except Exception as e:
        logging.error("An error occurred while deleting the directory %s: %s", dir_path, str(e))


run_exe(exe_path, [argument_data, input_file_path])
fix_ini(input_file_path, output_file_path)
delete_dir(data_path)
