#!/usr/bin/env python3
import codecs
import re
import os


def replace_bytes_in_file(input_file_path, temp_file_path):
    with open(input_file_path, 'rb') as file:
        content = file.read()

    replacement = re.sub(b'(?<!\xc2)\xa0', b'\xc2\xa0', content)

    with open(temp_file_path, 'wb') as file:
        file.write(replacement)


def replace_text(temp_file_path, output_file_path, replacements):
    with codecs.open(temp_file_path, 'r', 'utf-8-sig') as infile:
        original_text = infile.read()

    for old_text, new_text in replacements.items():
        original_text = original_text.replace(old_text, new_text)

    with codecs.open(output_file_path, 'w', 'utf-8-sig') as outfile:
        outfile.write(original_text)


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


input_file_path = 'global_original.ini'
temp_file_path = 'global_temp.ini'
output_file_path = 'global_fixed.ini'

replace_bytes_in_file(input_file_path, temp_file_path)
replace_text(temp_file_path, output_file_path, replacements)
delete_file(temp_file_path)
