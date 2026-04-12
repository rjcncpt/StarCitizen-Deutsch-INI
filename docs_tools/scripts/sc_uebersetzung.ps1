# Star Citizen Deutsch INI - Download-Skript

# Änderungen an diesem Skript können zu unerwartetem Verhalten führen. Bitte ändere nur die nachfolgenden Variablen. Alle Änderungen erfolgen auf eigene Gefahr.

# Konstanten (nicht ändern!)
$DownloadUrlNormal = "https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/refs/heads/main/live/global.ini"  # URL der global.ini von github, die heruntergeladen werden soll
$DownloadUrlVoll = "https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/refs/heads/main/live/full/global.ini"  # URL der global.ini von github, die heruntergeladen werden soll

# Anpassbare Variablen (Ändere diese entsprechend deiner Bedürfnisse)
$LivePath = "C:\Program Files\Roberts Space Industries\StarCitizen\LIVE" # Vollständiger Pfad, zum LIVE-Ordner
$LauncherPath = "C:\Program Files\Roberts Space Industries\RSI Launcher\RSI Launcher.exe" # Pfad zum RSI Launcher
$DownloadUrl = $DownloadUrlNormal # Hier kann zwischen $DownloadUrlNormal und $DownloadUrlVoll gewechselt werden
$Hotfix = $false # Wenn $true, wird die global.ini auch im hotfix-Ordner gespeichert, damit sie auch für den Hotfix-Patch verfügbar ist. Ansonsten wird sie nur im LIVE-Ordner gespeichert.
$LauncherStarten = $true # Wenn $true, wird der RSI Launcher nach dem Download automatisch gestartet.

# Skript zum Herunterladen der Datei
$Host.UI.RawUI.WindowTitle = "SCDL - Alternative"

try {
    Write-Host "Starte Download von $DownloadUrl..."
    Invoke-WebRequest -Uri $DownloadUrl -OutFile "$LivePath\data\Localization\german_(germany)\global.ini" -UseBasicParsing
    Write-Host "Download abgeschlossen. Datei gespeichert unter: $LivePath\data\Localization\german_(germany)\global.ini"
} catch {
    Write-Error "Fehler beim Herunterladen: $_"
    # Kurze Pause um Ausgabe nachzuvollziehen
    Start-Sleep -Seconds 5
    exit 1
}

if ($Hotfix) {
    try {
        Write-Host "Kopiere Datei in den Hotfix-Ordner..."
        Copy-Item -Path "$LivePath\data\Localization\german_(germany)\global.ini" -Destination "$LivePath\..\HOTFIX\data\Localization\german_(germany)\global.ini"
        Write-Host "Datei erfolgreich kopiert."
    } catch {
        Write-Error "Fehler beim Kopieren der Datei: $_"
        # Kurze Pause um Ausgabe nachzuvollziehen
        Start-Sleep -Seconds 5
        exit 1
    }
}

# RSI Launcher öffnen
if ($LauncherStarten) {
    try {
        Write-Host "Starte RSI Launcher: $LauncherPath"
        Start-Process -FilePath $LauncherPath
        Write-Host "RSI Launcher erfolgreich gestartet."
    } catch {
        Write-Error "Fehler beim Starten des RSI Launcher: $_"
        # Kurze Pause um Ausgabe nachzuvollziehen
        Start-Sleep -Seconds 5
        exit 1
    }
}

