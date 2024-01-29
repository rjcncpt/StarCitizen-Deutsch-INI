#!/usr/bin/env python3
import codecs
import re
import subprocess
import shutil

# The following paths need to fit your setup
exe_path = 'unp4k/unp4k.exe'  # Absolut or relativ path to the unp4k.exe
argument_data = 'C:/Program Files/Roberts Space Industries/StarCitizen/LIVE/Data.p4k'  # Absolut or relativ path to the Data.p4k

# The following paths are internally used and do not need to be edited, but can be edited
data_path = 'Data'  # Temporary directory that will be deleted at the end of the script
input_file_path = data_path + '/Localization/english/global.ini'  # Relative path to the extracted global.ini. Also used als filter argument for unp4k.
output_file_path = 'global.ini'  # Path where the fixed global.ini will be saved

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
    command = [exe_path] + args
    try:
        subprocess.run(command, check=True)
        print(f"The executable {exe_path} has been started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"The executable {exe_path} failed to run. Error: {str(e)}")
    except FileNotFoundError:
        print(f"The executable {exe_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while running the executable {exe_path}: {str(e)}")


# Fixes the corrupted NBSP and writes the result in a temporary file
def fix_ini(input_file_path, output_file_path):
    with open(input_file_path, 'rb') as file:
        content = file.read()
    print(f"The file {input_file_path} has been read successfully.")

    replacement = re.sub(b'(?<!\xc2)\xa0', b'\xc2\xa0', content)
    print("The encoding of the file has been fixed successfully.")

    original_text = codecs.decode(replacement, 'UTF-8-SIG')
    print("The fixed file has been read successfully as UTF-8-BOM.")

    for old_text, new_text in replacements.items():
        original_text = original_text.replace(old_text, new_text)
    print("The variables have been fixed successfully.")

    with codecs.open(output_file_path, 'w', 'UTF-8-SIG') as outfile:
        outfile.write(original_text)
    print(f"The file {output_file_path} has been written successfully as UTF-8-BOM.")


def delete_dir(dir_path):
    try:
        shutil.rmtree(dir_path)
        print(f"The directory {dir_path} has been deleted successfully.")
    except FileNotFoundError:
        print(f"The directory {dir_path} does not exist.")
    except PermissionError:
        print(f"Permission denied for deleting the directory {dir_path}.")
    except OSError as e:
        print(f"Error: {e.filename} - {e.strerror}.")
    except Exception as e:
        print(f"An error occurred while deleting the directory {dir_path}: {str(e)}")


run_exe(exe_path, [argument_data, input_file_path])
fix_ini(input_file_path, output_file_path)
delete_dir(data_path)
