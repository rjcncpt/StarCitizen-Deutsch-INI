@echo off
REM PFAD ZUM SPIELVERZEICHNIS ANGEBEN
set "BASE_PATH=E:\Roberts Space Industries\StarCitizen"

REM Prüfe, ob der PTU-Ordner existiert
if exist "%BASE_PATH%\PTU\" (
    echo Erstelle die Ordnerstrukturen und lade alle Daten herunter.
    
    REM NICHTS ÄNDERN! Erstelle die Ordnerstrukturen
    mkdir "%BASE_PATH%\LIVE\data\Localization"
    mkdir "%BASE_PATH%\PTU\data\Localization"
    mkdir "%BASE_PATH%\LIVE"
    mkdir "%BASE_PATH%\PTU"

    REM NICHTS ÄNDERN! Lade die Dateien herunter
    powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/global.ini' -OutFile '%BASE_PATH%\LIVE\data\Localization\global.ini'"
    powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/ptu/global.ini' -OutFile '%BASE_PATH%\PTU\data\Localization\global.ini'"
    powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/user.cfg' -OutFile '%BASE_PATH%\LIVE\user.cfg'"
    powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/user.cfg' -OutFile '%BASE_PATH%\PTU\user.cfg'"

) else (
    echo PTU-Ordner nicht vorhanden. Lade nur die LIVE-Daten herunter.
    
    REM NICHTS ÄNDERN! Erstelle die Ordnerstrukturen
    mkdir "%BASE_PATH%\LIVE\data\Localization"

    REM NICHTS ÄNDERN! Lade die Dateien herunter
    powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/global.ini' -OutFile '%BASE_PATH%\LIVE\data\Localization\global.ini'"
    powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/user.cfg' -OutFile '%BASE_PATH%\LIVE\user.cfg'"
)

echo Download abgeschlossen!

REM PFAD ZUM RSI LAUNCHER ANGEBEN
start "" "E:\Roberts Space Industries\RSI Launcher\RSI Launcher.exe"

timeout /t 5
