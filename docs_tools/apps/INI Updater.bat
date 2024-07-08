@echo off

rem URLs für die INI-Dateien (LIVE und PTU)
set "url1=https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/ptu/global.ini"
set "url2=https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/global.ini"

rem PFAD ZUR STAR CITIZEN INSTALLATION (LIVE und PTU)
set "path1=C:\Program Files\Roberts Space Industries\StarCitizen\PTU\data\Localization\german_(germany)"
set "path2=C:\Program Files\Roberts Space Industries\StarCitizen\LIVE\data\Localization\german_(germany)"

echo Herunterladen der INI-Datei von %url1% nach %path1%...
curl -o "%path1%\global.ini" %url1%
echo.
echo Download abgeschlossen - LIVE.
echo.
echo.
echo Herunterladen der INI-Datei von %url2% nach %path2%...
curl -o "%path2%\global.ini" %url2%
echo.
echo Download abgeschlossen - PTU.

rem PFAD ZUM RSI LAUNCHER
start "RSI Launcher" "C:\Program Files\Roberts Space Industries\RSI Launcher\RSI Launcher.exe"

timeout /t 5
