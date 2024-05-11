@echo off
set "url=https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/full/global.ini"



rem PFAD ZUR STAR CITIZEN INSTALLATION
set "path1=E:\Roberts Space Industries\StarCitizen\LIVE\data\Localization\german_(germany)"

echo Herunterladen der INI-Datei von %url%...
curl -o "%path1%\global.ini" %url%

echo Download abgeschlossen.


rem PFAD ZUM RSI LAUNCHER
start "RSI Launcher" 	"E:\Roberts Space Industries\RSI Launcher\RSI Launcher.exe"
