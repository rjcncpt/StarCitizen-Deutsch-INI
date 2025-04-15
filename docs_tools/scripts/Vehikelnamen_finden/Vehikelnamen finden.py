##################################################################################################################################################
# Dieses Python Script hilft dabei, die richtigen Artikel für Vehikel zu finden.                                                                 #
# In unserer Übersetzung sind Schiffe und Gravlev Vehikel weiblich und Fahrzeuge männlich.                                                       #
##################################################################################################################################################
# Speichere die "Vehikelnamen finden.py" und "Vehikelnamen finden_prefixes.txt" ab.                                                              #
# Starte das Python Script und suche nach der global.ini Datei.                                                                                  #
# Die "Vehikelnamen finden_prefixes.txt" Datei beinhaltet bereits alle geprüften Zeilen die beim erneuten Scan nicht mehr berücksichtigt werden. #
# Nach dem Scan wird eine "Vehikelnamen finden_global.html" Datei erstellt mit allen neuen Zeilen in denen Vehikelnamen vorkommen.               #
# Möchtest du neu beginnen, lösche die "Vehikelnamen finden_prefixes.txt" Datei.                                                                 #
##################################################################################################################################################


import re
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from datetime import datetime
import html
from tqdm import tqdm

# Liste aller bekannten Vehikelnamen (Stand: 15. April 2025)
vehicles = [
    "100i",
    "125a",
    "135c",
    "300i",
    "315p",
    "325a",
    "350r",
    "400i",
    "600i",
    "85X",
    "890 Jump",
    "A1",
    "A2",
    "Argo Cargo",
    "Arrastra",
    "Arrow",
    "Aurora",
    "Avenger",
    "Ballista",
    "Banu Defender",
    "Bengal",
    "Blade",
    "Buccaneer",
    "C1",
    "C2",
    "Carrack",
    "Caterpillar",
    "Centurion",
    "Constellation",
    "Corsair",
    "Crucible",
    "Cutlass",
    "Cutter",
    "Cyclone",
    "Dragonfly",
    "Driller",
    "E1 Spirit",
    "Eclipse",
    "Endeavor",
    "Expanse",
    "F7A",
    "F7C",
    "F7C-M",
    "F7C-R",
    "F8A Lightning",
    "F8C Lightning",
    "Freelancer",
    "G12",
    "G12a",
    "G12r",
    "Galaxy",
    "Genesis Starliner",
    "Gladiator",
    "Gladius",
    "Glaive",
    "Greycat PTV",
    "Hammerhead",
    "Harvester",
    "Hawk",
    "Herald",
    "Hull",
    "Hurricane",
    "Idris-M",
    "Idris-P",
    "Inferno",
    "Ion",
    "Javelin",
    "Khartu-al",
    "Kingship",
    "Kraken",
    "Kraken Privateer",
    "Legionnaire",
    "Liberator",
    "Lynx",
    "M2 Hercules",
    "M50",
    "Mantis",
    "Merchantman",
    "Mercury Star Runner",
    "MOLE",
    "MPUV",
    "Mustang",
    "Nautilus",
    "Nomad",
    "Nova",
    "Nox",
    "Odyssey",
    "Orion",
    "P-52",
    "P-72",
    "Pegasus",
    "Perseus",
    "Pioneer",
    "Pisces",
    "C8",
    "C8X",
    "Polaris",
    "Prospector",
    "Prowler",
    "Qhire Khartu",
    "RAFT",
    "Railen",
    "Ranger CV",
    "Ranger RC",
    "Ranger TR",
    "Razor",
    "Reclaimer",
    "Redeemer",
    "Reliant",
    "Retaliator",
    "ROC",
    "ROC-DS",
    "Sabre",
    "San’tok.yāi",
    "Scorpius",
    "Scythe",
    "Spartan",
    "SRV",
    "Starfarer",
    "Starfarer Gemini",
    "Storm",
    "Syulen",
    "Talon",
    "Terrapin",
    "Ursa",
    "Vanguard",
    "Void",
    "Vulcan",
    "Vulture",
    "X1",
    "X1 Force",
    "X1 Velocity",
    "Zeus",
    "Valkyrie",
    "Mule",
    "STV",
    "Cleaver",
    "Driller",
    "Harvester",
    "Kingship",
]

# Regex-Pattern vorbereiten
vehicle_patterns = [(v, re.compile(rf'\b{re.escape(v)}\b')) for v in vehicles]

# Funktion zum Laden der gespeicherten Präfixe
def load_prefixes():
    prefixes = set()
    prefix_file = Path("Vehikelnamen finden_prefixes.txt")
    if prefix_file.exists():
        with open(prefix_file, "r", encoding="utf-8") as f:
            prefixes.update(line.strip() for line in f if line.strip())
    return prefixes

# Funktion zum Speichern eines neuen Präfixes
def save_prefix(prefix):
    with open("Vehikelnamen finden_prefixes.txt", "a", encoding="utf-8") as f:
        f.write(prefix + "\n")

# GUI für Datei öffnen
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="INI-Datei auswählen", filetypes=[("INI files", "*.ini"), ("All files", "*.*")])

if not file_path:
    print("Keine Datei ausgewählt.")
    exit()

# HTML-Vorlage mit Bootstrap (wie im Original, unverändert)
html_template = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gefundene Zeilen mit Vehikelnamen</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{
            background-color: #f8f9fa;
        }}
        .vehicle-name {{
            font-weight: bold;
            color: #0d6efd;
        }}
        .card,
        .mb20 {{
            margin-bottom: 1rem;
        }}
    </style>
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-2">Gefundene Zeilen mit Vehikelnamen</h1>
        <p class="mb20">Erstellt am: {}<br>Gefundene Zeilen: {}</p>
        <div id="results">
            {}
        </div>
        <div class="footer">
            <p>Erstellt von rjcncpt | Deutsche Star Citizen Übersetzung</p>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

found_count = 0
existing_prefixes = load_prefixes()
results_html = ""

# Zähle die Gesamtzahl der Zeilen für die Fortschrittsleiste
with open(file_path, "r", encoding="utf-8") as file:
    total_lines = sum(1 for _ in file)

# Verarbeite die Datei mit angepasster Fortschrittsleiste
with open(file_path, "r", encoding="utf-8") as file:
    for line in tqdm(file, total=total_lines, desc="Verarbeite Datei", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}'):
        line = line.strip()
        # Extrahiere Präfix
        prefix = line.split("=", 1)[0].strip() if "=" in line else line
        # Überspringe bereits geprüfte Präfixe
        if prefix in existing_prefixes:
            continue

        matches = [(v, m) for v, pattern in vehicle_patterns if (m := pattern.search(line))]
        if matches:
            # Erstelle HTML für die Zeile
            formatted_line = ""
            pos = 0
            for v, match in sorted(matches, key=lambda m: m[1].start()):
                if match.start() > pos:
                    formatted_line += html.escape(line[pos:match.start()])
                formatted_line += f'<span class="vehicle-name">{html.escape(line[match.start():match.end()])}</span>'
                pos = match.end()
            if pos < len(line):
                formatted_line += html.escape(line[pos:])
            results_html += f'<div class="card"><div class="card-body">{formatted_line}</div></div>'
            found_count += 1
            save_prefix(prefix)

# Aktuelles Datum für den Header
current_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

# Speichern als HTML im Skriptverzeichnis
script_dir = Path(__file__).parent
output_path = script_dir / f"Vehikelnamen finden_{Path(file_path).stem}.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template.format(current_date, found_count, results_html))

print(f"\n{found_count} neue Zeilen verarbeitet und gespeichert in: {output_path}")
