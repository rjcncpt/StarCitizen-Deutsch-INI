@echo off
setlocal EnableDelayedExpansion

REM Schritt 1: Öffne den Ordner-Auswahldialog
echo ###########################################################################
echo #                                                                         #
echo #               ERSTINSTALLATION / STAR CITIZEN IN DEUTSCH                #
echo #                                                                         #
echo #         Diese Datei dient nur zur Erstellung der Ordnerstruktur         #
echo #            und laedt nur die Uebersetzung fuer LIVE herunter.           #
echo #                                                                         #
echo #                Um unsere Uebersetzung zu aktualisieren,                 #
echo #       lies dir bitte die Installationsanweisungen auf GitHub durch.     #
echo #                                                                         #
echo #           https://github.com/rjcncpt/StarCitizen-Deutsch-INI            #
echo #                                                                         #
echo ###########################################################################
echo.
echo.
echo Suche das Star Citizen Verzeichnis und oeffne den LIVE Ordner.
echo Danach wird die uebersetzung heruntergeladen.
echo.
echo Standard: C:\Program Files (x86)\Roberts Space Industries\StarCitizen\LIVE\.
echo.
set "zielordner="
for /f "tokens=* delims=" %%a in ('powershell -Command "& {Add-Type -AssemblyName System.Windows.Forms; $f = New-Object System.Windows.Forms.FolderBrowserDialog; $f.Description = 'Suche das Star Citizen Verzeichnis'; $f.RootFolder = 'MyComputer'; if($f.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK){$f.SelectedPath} else {'NULL'}}"') do set "zielordner=%%a"

REM Überprüfe, ob ein Zielordner ausgewählt wurde
if not defined zielordner (
    echo Kein Star Citizen Verzeichnis. Die Installation wird beendet.
    exit /b
)

REM Schritt 2: Erstelle Ordnerstruktur
set "ordnerstruktur=%zielordner%\data\Localization\german_(germany)"
mkdir "!ordnerstruktur!" 2>nul

REM Schritt 3: Lade global.ini-Datei von GitHub herunter und kopiere sie
set "github_global=%ordnerstruktur%\global.ini"
powershell -Command "& { Invoke-WebRequest 'https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/global.ini' -OutFile '%github_global%' }"

REM Schritt 4: Ja/Nein-Abfrage für user.cfg-Datei
set "github_usercfg=https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/main/live/user.cfg"
set "ziel_usercfg=%zielordner%\user.cfg"

if exist "%ziel_usercfg%" (
    set "overwrite="
    set /p "overwrite=### Die Datei user.cfg existiert bereits im Zielordner. Soll die Datei ersetzt werden? (J/N): "
    set "overwrite=!overwrite:~0,1!"

    if /i "!overwrite!" neq "J" (
        echo Die Datei nicht ersetzt. Die Installation wird beendet.
        exit /b
    )
)

REM Lade user.cfg-Datei von GitHub herunter und kopiere sie
powershell -Command "& { Invoke-WebRequest '%github_usercfg%' -OutFile '%ziel_usercfg%' }"

echo Aufgaben abgeschlossen.
pause
