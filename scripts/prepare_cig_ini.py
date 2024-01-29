#!/usr/bin/env python3
import codecs
import re
import os
import subprocess
import shutil

exe_path = 'unp4k/unp4k.exe'  # absolut or relativ path to the unp4k.exe
argument_data = 'C:/Program Files/Roberts Space Industries/StarCitizen/LIVE/Data.p4k'  # absolut or relativ path to the Data.p4k
argument_ini = 'Data/Localization/english/global.ini'  # filter argument for unp4k
data_path = 'Data'  # temporary directory that will be deleted at the end of the script
input_file_path = data_path + '/Localization/english/global.ini'  # relative path to the extracted global.ini
temp_file_path = 'global_temp.ini'  # temporary file that will be deleted at the end of the script
output_file_path = 'global.ini'  # path where the fixed global.ini will be saved

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
def run_exe_with_args(exe_path, args):
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
def replace_bytes_in_file(input_file_path, temp_file_path):
    with open(input_file_path, 'rb') as file:
        content = file.read()
    print(f"The file {input_file_path} has been read successfully.")

    replacement = re.sub(b'(?<!\xc2)\xa0', b'\xc2\xa0', content)
    print("The encoding of the file has been fixed successfully.")

    with open(temp_file_path, 'wb') as file:
        file.write(replacement)
    print(f"The file {temp_file_path} has been written successfully.")


# Replaces the given text parts
def replace_text(temp_file_path, output_file_path, replacements):
    with codecs.open(temp_file_path, 'r', 'utf-8-sig') as infile:
        original_text = infile.read()
    print(f"The file {temp_file_path} has been read successfully as UTF-8-BOM.")

    for old_text, new_text in replacements.items():
        original_text = original_text.replace(old_text, new_text)
    print("The variables have been fixed successfully.")

    with codecs.open(output_file_path, 'w', 'utf-8-sig') as outfile:
        outfile.write(original_text)
    print(f"The file {output_file_path} has been written successfully as UTF-8-BOM.")


# Deletes the temporary file
def delete_file(filepath):
    try:
        os.remove(filepath)
        print(f"The file {filepath} has been deleted successfully.")
    except FileNotFoundError:
        print(f"The file {filepath} does not exist.")
    except PermissionError:
        print(f"Permission denied for deleting the file {filepath}.")
    except Exception as e:
        print(f"An error occurred while deleting the file {filepath}: {str(e)}")


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


run_exe_with_args(exe_path, [argument_data, argument_ini])
replace_bytes_in_file(input_file_path, temp_file_path)
replace_text(temp_file_path, output_file_path, replacements)
delete_file(temp_file_path)
delete_dir(data_path)
