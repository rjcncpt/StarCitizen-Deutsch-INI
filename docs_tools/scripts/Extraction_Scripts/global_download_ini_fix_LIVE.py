import codecs
import re
import subprocess
import shutil
import logging

# The following paths need to fit your setup
exe_path =              "unp4k.exe"  # Path to the unp4k.exe
argument_data =         "E:/Roberts Space Industries/StarCitizen/LIVE/Data.p4k"  # Path to the Data.p4k
build_manifest_path =   "E:/Roberts Space Industries/StarCitizen/LIVE/build_manifest.id"  # Path to the build_manifest.id file
output_file_path =      "../global.ini"  # Path where the fixed global.ini will be saved

# The following paths are internally used and do not need to be edited, but can be edited
data_path = "Data"  # Temporary directory used by unp4k, that will be deleted at the end of the script
input_file_path = data_path + "/Localization/english/global.ini"  # Relative path to the extracted global.ini. Also used als filter argument for unp4k.

# Define your replacements here
replacements = {
    "Oxygen_Screen_ ErrorButtonMessage=": "Oxygen_Screen_ErrorButtonMessage=",
    "Tut03_Part01_Obj01b_ToStation =": "Tut03_Part01_Obj01b_ToStation=",
    "seachbody_obj_short_02a=": "searchbody_obj_short_02a=",
    "shop_ui_transactionResult_04 _InvalidPlayerInventoryId=": "shop_ui_transactionResult_04_InvalidPlayerInventoryId=",
    "shop_ui_transactionResult_05 _InventoryContainerRequestFail=": "shop_ui_transactionResult_05_InventoryContainerRequestFail=",
    "shop_ui_transactionResult_06 _InventoryItemFail=": "shop_ui_transactionResult_06_InventoryItemFail=",
    "~(Contractor": "~mission(Contractor",
    "~misssion(Item)": "~mission(Item)",
    "~mission (description)": "~mission(description)",
    "~mission (title)": "~mission(title)",
    "~mission (item)": "~mission(item)",
    "vehicl_DescMISC_Hull_B": "vehicle_DescMISC_Hull_B",
    " (Pickup1|Address)": " ~mission(Pickup1|Address)",
    "Event_ShipTItle_TheGladius": "Event_ShipTitle_TheGladius"
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
    modified_lines = []
    for line in lines:
        for prefix in prefixes:
            if line.startswith(prefix):
                line = re.sub(r'~mission\(Location\|Address\)', '', line, count=1)
                break
        modified_lines.append(line)
    return modified_lines

def extract_build_number(manifest_path):
    try:
        with open(manifest_path, 'r', encoding='utf-8') as file:
            content = file.read()

        branch_match = re.search(r'"Branch":\s*"(.*?)"', content)
        change_num_match = re.search(r'"RequestedP4ChangeNum":\s*"(\d+)"', content)

        if branch_match and change_num_match:
            branch = branch_match.group(1).split('-')[-1]  # Extract the version, e.g., 4.0.0
            change_num = change_num_match.group(1)
            return f"{branch} LIVE.{change_num}"
        else:
            logging.error("Branch or Change Number not found in build_manifest.id")
            return None
    except Exception as e:
        logging.error("Error while extracting build number: %s", str(e))
        return None

def move_frontend_pu_version_to_top(temp_file_path):
    try:
        with codecs.open(temp_file_path, 'r', 'utf-8-sig') as infile:
            lines = infile.readlines()

        frontend_line = None
        new_lines = []

        # First, try to find 'Frontend_PU_Version,P='
        for index, line in enumerate(lines):
            if line.strip().startswith("Frontend_PU_Version,P="):
                frontend_line = lines.pop(index)
                break

        # If not found, try to find 'Frontend_PU_Version='
        if not frontend_line:
            for index, line in enumerate(lines):
                if line.strip().startswith("Frontend_PU_Version="):
                    frontend_line = lines.pop(index)
                    break

        # Move the found line to the top, if found
        if frontend_line:
            new_lines.insert(0, frontend_line)

        with codecs.open(temp_file_path, 'w', 'utf-8-sig') as outfile:
            outfile.write("".join(new_lines + lines))

        logging.info("Moved 'Frontend_PU_Version' to the top in %s", temp_file_path)

    except Exception as e:
        logging.error("An error occurred while moving 'Frontend_PU_Version' to the top: %s", str(e))

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
        lines = remove_first_mission_key(lines, prefixes)

        with codecs.open(output_file_path, "w", "UTF-8-SIG") as outfile:
            outfile.write("\n".join(lines))

        logging.info("Successfully fixed variables and wrote file as UTF-8-BOM to %s", output_file_path)

        move_frontend_pu_version_to_top(output_file_path)

    except Exception as e:
        logging.error("An error occurred while fixing the INI file: %s", str(e))

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
build_number = extract_build_number(build_manifest_path)
if build_number:
    output_file_path = f"../{build_number}.ini"
    fix_ini(input_file_path, output_file_path)
delete_dir(data_path)