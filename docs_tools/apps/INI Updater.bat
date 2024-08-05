@echo off
setlocal

REM PFAD ZUM SPIELVERZEICHNIS ANGEBEN
set "BASE_PATH=E:\Roberts Space Industries\StarCitizen"

REM PFAD ZUM RSI LAUNCHER ANGEBEN
set "LAUNCHER_PATH=E:\Roberts Space Industries\RSI Launcher\RSI Launcher.exe"




REM ==================================================
REM = AB HIER NICHTS VERÄNDERN!
REM ==================================================
echo.
echo.
echo.
echo.
echo.
echo.
echo #################################################
echo   STAR CITIZEN DEUTSCHE SPRACHDATEI DOWNLOADER
echo                  (LIVE UND PTU)
echo #################################################
echo.
echo Starte die Ordnererstellung und den Download...
echo.

REM LIVE
echo Erstelle die LIVE-Ordnerstruktur...
if not exist "%BASE_PATH%\LIVE\data\Localization\german_(germany)" (
    mkdir "%BASE_PATH%\LIVE\data\Localization"
    mkdir "%BASE_PATH%\LIVE\data\Localization\german_(germany)"
    echo LIVE-Ordnerstruktur wurde erstellt.
) else (
    echo LIVE-Ordnerstruktur existiert bereits.
)

echo.
echo Lade die LIVE-Dateien herunter...
powershell -Command "Invoke-WebRequest -Uri 'https://www.fwkart.de/live-ini' -OutFile '%BASE_PATH%\LIVE\data\Localization\german_(germany)\global.ini'" && echo LIVE global.ini erfolgreich heruntergeladen. || echo Fehler beim Herunterladen von LIVE global.ini.
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/user.cfg' -OutFile '%BASE_PATH%\LIVE\user.cfg'" && echo LIVE user.cfg erfolgreich heruntergeladen. || echo Fehler beim Herunterladen von LIVE user.cfg.

echo.
REM PTU
if exist "%BASE_PATH%\PTU" (
    echo Erstelle die PTU-Ordnerstruktur...
    if not exist "%BASE_PATH%\PTU\data\Localization\german_(germany)" (
        mkdir "%BASE_PATH%\PTU\data\Localization"
        mkdir "%BASE_PATH%\PTU\data\Localization\german_(germany)"
        echo PTU-Ordnerstruktur wurde erstellt.
    ) else (
        echo PTU-Ordnerstruktur existiert bereits.
    )
    echo.
    echo Lade die PTU-Dateien herunter...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.fwkart.de/ptu-ini' -OutFile '%BASE_PATH%\PTU\data\Localization\german_(germany)\global.ini'" && echo PTU global.ini erfolgreich heruntergeladen. || echo Fehler beim Herunterladen von PTU global.ini.
    powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/user.cfg' -OutFile '%BASE_PATH%\PTU\user.cfg'" && echo PTU user.cfg erfolgreich heruntergeladen. || echo Fehler beim Herunterladen von PTU user.cfg.
) else (
    echo PTU-Ordner nicht gefunden. Keine PTU-Daten heruntergeladen.
)

REM Starte den RSI Launcher, falls er noch nicht läuft
echo.
tasklist /nh /fi "imagename eq rsi launcher.exe" | find /i "rsi launcher.exe" > nul || (
    echo RSI Launcher wird gestartet...
    start "" "%LAUNCHER_PATH%"
)

echo.
echo Alle Aufgaben abgeschlossen.
