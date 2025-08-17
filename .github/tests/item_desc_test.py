import os
from bracket_test import print_to_console
import re


def is_item_desc(current_key: str, value: str) -> bool:
    if "item_Desc_".lower() in current_key.lower():
        return True
    else:
        return False


def extract_desc_info(filename: str, excluded_keys: list) -> dict[str, dict[str, str]]:
    return_dict = {}

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith("#") or not line.strip():
            continue
        current_key, value = line.split("=", 1)
        if current_key in excluded_keys:
            continue
        if not is_item_desc(current_key, value):
            continue
        # Value is probably a armor -> Check if all information is present
        item_dict = {}

        item_dict["Typ (En)"] = re.match(r".*Item Type: (.+?)\\n", value)
        item_dict["Schadensreduktion"] = re.match(
            r".*Damage Reduction: (.+?)\\n", value
        )
        item_dict["Temperaturbereich"] = re.match(r".*Temp. Rating: (.+?)\\n", value)
        item_dict["Strahlenschutz"] = re.match(
            r".*Radiation Protection: (.+?)\\n", value
        )
        item_dict["Dekontaminationsrate"] = re.match(
            r".*Radiation Scrub Rate: (.+?)\\n", value
        )
        # item_dict["Tragekapazität"] = re.match(r".*Carrying Capacity: (.+?)\\n", value)

        for key in item_dict.keys():
            if item_dict[key]:
                item_dict[key] = item_dict[key].group(1).strip()
                if key == "Typ (En)" and current_key.find("_helmet_") != -1:
                    item_dict[key] = item_dict[key].replace("Armor", "Helmet")
            else:
                item_dict[key] = None

        return_dict[current_key] = item_dict
    return return_dict


def check_armor_desc(filename: str, eng_desc: dict[str, str], excluded_keys: list):
    """
    Check the armor description file for specific keys and validate their content.
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line_number, line in enumerate(lines, start=1):
        if line.startswith("#") or not line.strip():
            continue
        current_key, value = line.split("=", 1)
        if current_key in excluded_keys:
            continue
        if not is_item_desc(current_key, value):
            continue
        # Value is probably a armor -> Check if all information is present
        missing_fields = []
        if eng_desc.get(current_key) is None:
            print_to_console(
                f"{filename}:{line_number} / {current_key}: No English description found.",
                filename,
                line_number,
                "error",
            )
            continue
        for field in eng_desc[current_key]:
            if eng_desc[current_key][field] is not None:
                if (
                    eng_desc[current_key][field].lower().replace(".", ",")
                    not in value.lower().replace(".", ",")
                ):
                    missing_fields.append(field)

        if missing_fields:
            expected_fields = {
                k: v
                for k, v in eng_desc[current_key].items()
                if v is not None and k in missing_fields
            }
            print_to_console(
                f"{filename}:{line_number} / {current_key}: Missing information: {missing_fields}. Expected: {expected_fields}",
                filename,
                line_number,
                "error",
            )


if __name__ == "__main__":
    excluded_keys = [
        "item_Desc_cds_medium_armor_01_Shared",  # Forgotten ° character
    ]
    en_live_file = ".github/en/live/global.ini"
    deu_live_file = "live/global.ini"

    if os.path.exists(en_live_file):
        print(f"Extracting English descriptions from {en_live_file}...")
        eng_desc = extract_desc_info(en_live_file, excluded_keys)

        if os.path.exists(deu_live_file):
            print(f"Checking {deu_live_file}...")
            check_armor_desc(deu_live_file, eng_desc, excluded_keys)
        else:
            print_to_console(
                f"Skipping {deu_live_file}: File not found.",
                deu_live_file,
                0,
                "warning",
            )
    else:
        print_to_console(
            f"Skipping {en_live_file}: File not found.", en_live_file, 0, "warning"
        )
