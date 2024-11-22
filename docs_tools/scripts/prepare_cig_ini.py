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
#input_file_path = data_path + "/Localization/german_(germany)/global.ini"  # Relative path to the extracted global.ini. Also used als filter argument for unp4k.
output_file_path = "global.ini"  # Path where the fixed global.ini will be saved

# Define your replacements here
replacements = {
    "Oxygen_Screen_ ErrorButtonMessage=": "Oxygen_Screen_ErrorButtonMessage=",
    "Tut03_Part01_Obj01b_ToStation =": "Tut03_Part01_Obj01b_ToStation=",
    "seachbody_obj_short_02a=": "searchbody_obj_short_02a=",
    "shop_ui_transactionResult_04 _InvalidPlayerInventoryId=": "shop_ui_transactionResult_04_InvalidPlayerInventoryId=",
    "shop_ui_transactionResult_05 _InventoryContainerRequestFail=": "shop_ui_transactionResult_05_InventoryContainerRequestFail=",
    "shop_ui_transactionResult_06 _InventoryItemFail=": "shop_ui_transactionResult_06_InventoryItemFail=",
    "vehicl_DescMISC_Hull_B": "vehicle_DescMISC_Hull_B",
    "Event_ShipTItle_TheGladius": "Event_ShipTitle_TheGladius",
    "~(Contractor": "~mission(Contractor",
    "~misssion(Item)": "~mission(Item)",
    "~mission (description)": "~mission(description)",
    "~mission (title)": "~mission(title)",
    "~mission (item)": "~mission(item)"
}

prefixes = [
    "mtps_UGF_eliminateall_allies_desc_intro=",
    "mtps_UGF_eliminateall_allies_desc_rehire=",
    "mtps_UGF_eliminateall_desc_001=",
    "mtps_UGF_eliminateall_nocivs_desc_001=",
    "mtps_basesweep_desc_01=",
    "mtps_bounty_desc_ERT=",
    "mtps_bounty_desc_HRT=",
    "mtps_bounty_desc_LRT=",
    "mtps_bounty_desc_MRT=",
    "mtps_bounty_desc_VHRT=",
    "mtps_bounty_desc_VLRT=",
    "mtps_bounty_desc_intro=",
    "mtps_bounty_desc_rehire=",
    "mtps_bounty_fps_UGF_bountyonly_desc_001=",
    "mtps_bounty_fps_UGF_desc_001=",
    "mtps_bounty_fps_UGF_nocivs_desc_001=",
    "mtps_bounty_fps_desc_001=",
    "mtps_bounty_fps_desc_first_001=",
    "mtps_bounty_fps_desc_rehire_001=",
    # Weitere Präfixe hier hinzufügen
]

def remove_first_mission_key(lines, prefixes):
    # Entfernt das erste Vorkommen von ~mission(Location|Address) für Zeilen, die mit bestimmten Präfixen beginnen.
    modified_lines = []
    for line in lines:
        for prefix in prefixes:
            if line.startswith(prefix):
                # Nur das erste Vorkommen von ~mission(Location|Address) entfernen
                line = re.sub(r'~mission\(Location\|Address\)', '', line, count=1)
                break  # Präfix gefunden, weitere nicht prüfen
        modified_lines.append(line)
    return modified_lines


def run_exe(exe_path, args):
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


def fix_ini(input_file_path, output_file_path):
    try:
        with open(input_file_path, "rb") as file:
            content = file.read()

        replacement = re.sub(b"(?<!\xc2)\xa0", b"\xc2\xa0", content)
        original_text = codecs.decode(replacement, "UTF-8-SIG")
        for old_text, new_text in replacements.items():
            original_text = original_text.replace(old_text, new_text)

        lines = original_text.splitlines()
        lines = remove_first_mission_key(lines, prefixes)  # Anwenden der neuen Funktion

        with codecs.open(output_file_path, "w", "UTF-8-SIG") as outfile:
            outfile.write("\n".join(lines))

        logging.info("Successfully fixed variables and wrote file as UTF-8-BOM to %s", output_file_path)

        move_frontend_pu_version_to_top(output_file_path)

    except Exception as e:
        logging.error("An error occurred while fixing the INI file: %s", str(e))


def move_frontend_pu_version_to_top(file_path):
# Verschiebt die Frontend_PU_Version Zeile an den Anfang und entfernt diese an der Ursprungsposition
    try:
        with codecs.open(file_path, 'r', 'utf-8-sig') as infile:
            lines = infile.readlines()

        frontend_line = None
        new_lines = []

        for index, line in enumerate(lines):
            if line.strip().startswith("Frontend_PU_Version="):
                frontend_line = lines.pop(index)
                break

        if frontend_line:
            new_lines.insert(0, frontend_line)

            with codecs.open(file_path, 'w', 'utf-8-sig') as outfile:
                outfile.write("".join(new_lines + lines))
        else:
            logging.warning("Line 'Frontend_PU_Version=' not found in %s", file_path)

    except Exception as e:
        logging.error("An error occurred while moving 'Frontend_PU_Version=' to the top: %s", str(e))


def delete_dir(dir_path):
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


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

run_exe(exe_path, [argument_data, input_file_path])
fix_ini(input_file_path, output_file_path)
delete_dir(data_path)
