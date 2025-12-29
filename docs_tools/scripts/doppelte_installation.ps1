# Konsolenfenster-Titel setzen
$Host.UI.RawUI.WindowTitle = "SCDL - Fehlersuche"

# Suchmuster für die gesuchten Pfade
$SuchmusterData = "StarCitizen\LIVE\Data.p4k"
$SuchmusterLauncher = "StarCitizen\LIVE\StarCitizen_Launcher.exe"

# Zu ignorierende Verzeichnisse für schnellere Suche
$ExcludedFolders = @('$Recycle.Bin', 'Windows', 'ProgramData', 'AppData', 'System Volume Information')

# Gesamtzeitmessung starten
$Startzeit = Get-Date

# Alle Laufwerke ermitteln
$Laufwerke = Get-PSDrive -PSProvider FileSystem | Where-Object { $_.Root -match "^[A-Z]:" }
$LaufwerkCount = $Laufwerke.Count
$LaufwerkIndex = 0

# ==== ERSTER SUCHLAUF: Star Citizen Verzeichnisse ====
Write-Host "`nSuche nach Star Citizen Verzeichnissen`n" -ForegroundColor Cyan
$GefundeneVerzeichnisse = @()
$LeereInstallationen = @()

foreach ($Laufwerk in $Laufwerke) {
    $LaufwerkIndex++
    Write-Progress -Activity "Durchsuche Verzeichnisse auf Laufwerk $($Laufwerk.Root)" -Status "Laufwerk: $LaufwerkIndex von $LaufwerkCount" -PercentComplete (($LaufwerkIndex / $LaufwerkCount) * 100)
    try {
        if ($Laufwerk.Root -eq "C:\") {
            # Auf C:\ nur in Program Files und Program Files (x86) suchen
            $ProgramDirs = @("C:\Program Files", "C:\Program Files (x86)")
            foreach ($ProgramDir in $ProgramDirs) {
                if (Test-Path $ProgramDir) {
                    $VerzeichnisTreffer = Get-ChildItem -Path $ProgramDir -Directory -Recurse -ErrorAction SilentlyContinue -Exclude $ExcludedFolders |
                        Where-Object { 
                            $_.Name -like "*StarCitizen*" -or 
                            $_.Name -like "*Star Citizen*" -or
                            $_.Name -eq "StarCitizen" -or
                            $_.Name -eq "Star Citizen" -or
                            $_.Name -eq "Roberts Space Industries"
                        }
                    
                    # Prüfen auf leere Installationen
                    foreach ($Verzeichnis in $VerzeichnisTreffer) {
                        if ($Verzeichnis.Name -eq "Roberts Space Industries") {
                            $Laufwerk = ($Verzeichnis.FullName -split "\\")[0]
                            $LeereInstallationen += [PSCustomObject]@{
                                Pfad = $Verzeichnis.FullName
                                Laufwerk = $Laufwerk
                            }
                        }
                    }
                    
                    $GefundeneVerzeichnisse += $VerzeichnisTreffer.FullName
                }
            }
        } else {
            # Auf anderen Laufwerken vollständig suchen, irrelevante Verzeichnisse ausschließen
            $VerzeichnisTreffer = Get-ChildItem -Path $Laufwerk.Root -Directory -Recurse -ErrorAction SilentlyContinue -Exclude $ExcludedFolders |
                Where-Object { 
                    $_.Name -like "*StarCitizen*" -or 
                    $_.Name -like "*Star Citizen*" -or
                    $_.Name -eq "StarCitizen" -or
                    $_.Name -eq "Star Citizen" -or
                    $_.Name -eq "Roberts Space Industries"
                }
            
            # Prüfen auf leere Installationen
            foreach ($Verzeichnis in $VerzeichnisTreffer) {
                if ($Verzeichnis.Name -eq "Roberts Space Industries") {
                    $Laufwerk = ($Verzeichnis.FullName -split "\\")[0]
                    $LeereInstallationen += [PSCustomObject]@{
                        Pfad = $Verzeichnis.FullName
                        Laufwerk = $Laufwerk
                    }
                }
            }
            
            $GefundeneVerzeichnisse += $VerzeichnisTreffer.FullName
        }
    } catch {
        # Fehler ignorieren (z.B. Zugriffsprobleme)
        continue
    }
}

Write-Progress -Activity "Durchsuche Verzeichnisse" -Completed

# Gefundene Verzeichnisse anzeigen
$GefundeneVerzeichnisse = $GefundeneVerzeichnisse | Where-Object { $_ -and $_.Trim() -ne "" } | Sort-Object -Unique
if ($GefundeneVerzeichnisse.Count -eq 0) {
    Write-Host "Keine StarCitizen Verzeichnisse gefunden." -ForegroundColor Yellow
} else {
    Write-Host "Gefundene Star Citizen Verzeichnisse ($($GefundeneVerzeichnisse.Count)):" -ForegroundColor Green
    $GefundeneVerzeichnisse | ForEach-Object -Begin { $i = 1 } -Process {
        # Prüfen ob es sich um eine Roberts Space Industries Installation handelt
        $IsLeereInstallation = $LeereInstallationen | Where-Object { $_.Pfad -eq $_ }
        if ($IsLeereInstallation) {
            Write-Host ("  {0}: {1}" -f $i, $_) -ForegroundColor Red
        } else {
            Write-Output ("  {0}: {1}" -f $i, $_)
        }
        $i++
    }
}

# ==== ZWEITER SUCHLAUF: Data.p4k Dateien ====
Write-Host "`nSuche nach Data.p4k Datei in allen Laufwerken" -ForegroundColor Cyan
$GefundenePfade = @()
$LaufwerkIndex = 0

foreach ($Laufwerk in $Laufwerke) {
    $LaufwerkIndex++
    Write-Progress -Activity "Durchsuche Laufwerk $($Laufwerk.Root) nach Data.p4k" -Status "Laufwerk: $LaufwerkIndex von $LaufwerkCount" -PercentComplete (($LaufwerkIndex / $LaufwerkCount) * 100)
    try {
        if ($Laufwerk.Root -eq "C:\") {
            # Auf C:\ nur in Program Files und Program Files (x86) suchen
            $ProgramDirs = @("C:\Program Files", "C:\Program Files (x86)")
            foreach ($ProgramDir in $ProgramDirs) {
                if (Test-Path $ProgramDir) {
                    $Treffer = Get-ChildItem -Path $ProgramDir -Filter "Data.p4k" -Recurse -ErrorAction SilentlyContinue -Exclude $ExcludedFolders |
                        Where-Object { $_.FullName -match [regex]::Escape($SuchmusterData) }
                    $GefundenePfade += $Treffer | Select-Object FullName, @{Name="ParentDir";Expression={Split-Path -Parent $_.FullName}}
                }
            }
        } else {
            # Auf anderen Laufwerken vollständig suchen
            $Treffer = Get-ChildItem -Path $Laufwerk.Root -Filter "Data.p4k" -Recurse -ErrorAction SilentlyContinue -Exclude $ExcludedFolders |
                Where-Object { $_.FullName -match [regex]::Escape($SuchmusterData) }
            $GefundenePfade += $Treffer | Select-Object FullName, @{Name="ParentDir";Expression={Split-Path -Parent $_.FullName}}
        }
    } catch {
        # Fehler ignorieren (z.B. Zugriffsprobleme)
        continue
    }
}

Write-Progress -Activity "Durchsuche Data.p4k" -Completed

# ==== DRITTER SUCHLAUF: StarCitizen_Launcher.exe ====
Write-Host "Suche nach StarCitizen_Launcher.exe Datei in allen Laufwerken" -ForegroundColor Cyan
$GefundeneLauncherPfade = @()
$LaufwerkIndex = 0

foreach ($Laufwerk in $Laufwerke) {
    $LaufwerkIndex++
    Write-Progress -Activity "Durchsuche Laufwerk $($Laufwerk.Root) nach StarCitizen_Launcher.exe" -Status "Laufwerk: $LaufwerkIndex von $LaufwerkCount" -PercentComplete (($LaufwerkIndex / $LaufwerkCount) * 100)
    try {
        if ($Laufwerk.Root -eq "C:\") {
            # Auf C:\ nur in Program Files und Program Files (x86) suchen
            $ProgramDirs = @("C:\Program Files", "C:\Program Files (x86)")
            foreach ($ProgramDir in $ProgramDirs) {
                if (Test-Path $ProgramDir) {
                    $Treffer = Get-ChildItem -Path $ProgramDir -Filter "StarCitizen_Launcher.exe" -Recurse -ErrorAction SilentlyContinue -Exclude $ExcludedFolders |
                        Where-Object { $_.FullName -match [regex]::Escape($SuchmusterLauncher) }
                    $GefundeneLauncherPfade += $Treffer | Select-Object FullName, @{Name="ParentDir";Expression={Split-Path -Parent $_.FullName}}
                }
            }
        } else {
            # Auf anderen Laufwerken vollständig suchen
            $Treffer = Get-ChildItem -Path $Laufwerk.Root -Filter "StarCitizen_Launcher.exe" -Recurse -ErrorAction SilentlyContinue -Exclude $ExcludedFolders |
                Where-Object { $_.FullName -match [regex]::Escape($SuchmusterLauncher) }
            $GefundeneLauncherPfade += $Treffer | Select-Object FullName, @{Name="ParentDir";Expression={Split-Path -Parent $_.FullName}}
        }
    } catch {
        # Fehler ignorieren (z.B. Zugriffsprobleme)
        continue
    }
}

Write-Progress -Activity "Durchsuche StarCitizen_Launcher.exe" -Completed

# Konsolidierung der Pfade
$AllePfade = @($GefundenePfade + $GefundeneLauncherPfade) | Where-Object { $_.FullName -and $_.FullName.Trim() -ne "" }
$GefundeneInstallationen = @()

# Alle Pfade einzeln behandeln, aber build_manifest.id nur für Launcher ausgeben
foreach ($Pfad in $AllePfade) {
    $GefundeneInstallationen += [PSCustomObject]@{
        FullName = $Pfad.FullName
        ParentDir = $Pfad.ParentDir
        IsLauncher = $Pfad.FullName -like "*StarCitizen_Launcher.exe"
    }
}

# Entferne Duplikate basierend auf FullName und sortiere
$GefundeneInstallationen = $GefundeneInstallationen | Sort-Object FullName -Unique

# Zähle eindeutige Installationen basierend auf Elternverzeichnissen
$EindeutigeVerzeichnisse = $AllePfade | Select-Object -ExpandProperty ParentDir | Sort-Object -Unique

# Gesamtzeitmessung ausgeben
$Endzeit = Get-Date
$Dauer = $Endzeit - $Startzeit
Write-Host ("`nSuche in {0:mm\:ss} abgeschlossen." -f $Dauer)

# Leere Zeile für bessere Lesbarkeit
Write-Host "`n"

# ==== ERGEBNISSE DER SUCHE MIT BUILD INFO ====
Write-Host "Ergebnis der Installation-Suche" -ForegroundColor Cyan
if ($EindeutigeVerzeichnisse.Count -eq 0) {
    Write-Host "Keine Star Citizen Installationen gefunden." -ForegroundColor Yellow
} else {
    if ($EindeutigeVerzeichnisse.Count -gt 1) {
        Write-Host "Mehrere Installationen gefunden:" -ForegroundColor Red
    } else {
        Write-Host "Eine Installation gefunden:" -ForegroundColor Green
    }
    Write-Output ""

    $VerzeichnisseMitBuildInfo = @()
    $GefundeneInstallationen | ForEach-Object -Begin { $i = 1 } -Process {
        $Pfad = $_.FullName
        $ParentDir = $_.ParentDir
        $IsLauncher = $_.IsLauncher

        Write-Output ("   {1}" -f $i, $Pfad)

        # build_manifest.id nur für Launcher oder wenn keine Data.p4k im Verzeichnis ist
        if ($IsLauncher -and $ParentDir -notin $VerzeichnisseMitBuildInfo) {
            $BuildManifestPfad = Join-Path $ParentDir "build_manifest.id"
            
            if (Test-Path $BuildManifestPfad) {
                try {
                    # JSON-Datei einlesen und parsen
                    $BuildManifestInhalt = Get-Content $BuildManifestPfad -Raw | ConvertFrom-Json
                    
                    # Branch und BuildDateStamp aus der JSON-Struktur extrahieren
                    $Branch = $BuildManifestInhalt.Data.Branch
                    $BuildDateStamp = $BuildManifestInhalt.Data.BuildDateStamp
                    
                    if ($Branch) {
                        Write-Host ("     SC Version: {0}" -f $Branch) -ForegroundColor Cyan
                    }
                    if ($BuildDateStamp) {
                        Write-Host ("     Build Datum: {0}" -f $BuildDateStamp) -ForegroundColor Cyan
                        Write-Output ""
                    }
                    
                    if (-not $Branch -and -not $BuildDateStamp) {
                        Write-Host "   Keine Branch/BuildDateStamp Informationen gefunden" -ForegroundColor Yellow
                        Write-Output ""
                    }
                } catch {
                    Write-Host "   Fehler beim Lesen der build_manifest.id Datei: $_" -ForegroundColor Red
                    Write-Output ""
                }
            } else {
                Write-Host "   build_manifest.id Datei nicht gefunden" -ForegroundColor Yellow
                Write-Output ""
            }
            $VerzeichnisseMitBuildInfo += $ParentDir
        }
        
        $i++
    }
}

# ==== ZUSAMMENFASSUNG FÜR VOLLSTÄNDIGE INSTALLATIONEN ====
Write-Host "`n" -ForegroundColor Cyan
Write-Host "   Zusammenfassung" -ForegroundColor Green
$KompletteInstallationen = @()

# Gruppieren nach Elternverzeichnis, um vollständige Installationen zu finden
$GruppiertePfade = $AllePfade | Group-Object -Property ParentDir | Where-Object {
    ($_.Group | Where-Object { $_.FullName -like "*Data.p4k" }) -and
    ($_.Group | Where-Object { $_.FullName -like "*StarCitizen_Launcher.exe" }) -and
    (Test-Path (Join-Path $_.Name "build_manifest.id"))
}

foreach ($Gruppe in $GruppiertePfade) {
    $Laufwerk = ($Gruppe.Name -split "\\")[0]
    Write-Host "   Auf Laufwerk ${Laufwerk} wurde eine Installation identifiziert, in der die folgenden Dateien enthalten sind"
    Write-Host "   und wahrscheinlich die Star Citizen Hauptinstallation darstellt."
    Write-Host "     - Data.p4k"
    Write-Host "     - StarCitizen_Launcher.exe"
    Write-Host "     - build_manifest.id"
    Write-Host "`n"
    $KompletteInstallationen += $Gruppe.Name
}

# Hinweis auf leere Installationen hinzufügen (aber nur für Laufwerke ohne vollständige Installation)
if ($LeereInstallationen.Count -gt 0) {
    # Laufwerke mit vollständigen Installationen ermitteln
    $LaufwerkeMitVollstaendigerInstallation = @()
    foreach ($Gruppe in $GruppiertePfade) {
        $Laufwerk = ($Gruppe.Name -split "\\")[0]
        $LaufwerkeMitVollstaendigerInstallation += $Laufwerk
    }
    
    # Nur leere Installationen auf Laufwerken ohne vollständige Installation anzeigen
    $LaufwerkeGruppiertePfade = $LeereInstallationen | Where-Object { $_.Laufwerk -notin $LaufwerkeMitVollstaendigerInstallation } | Group-Object -Property Laufwerk
    
    foreach ($LaufwerkGruppe in $LaufwerkeGruppiertePfade) {
        Write-Host "   Auf Laufwerk $($LaufwerkGruppe.Name) wurde ein Verzeichnis identifiziert, das nach einer leeren Installation aussieht:" -ForegroundColor Yellow
        $LaufwerkGruppe.Group | ForEach-Object {
            Write-Host "      - $($_.Pfad)`n" -ForegroundColor Yellow
        }
    }
    Write-Host "`n"
}

if ($KompletteInstallationen.Count -eq 0 -and $LeereInstallationen.Count -eq 0) {
    Write-Host "Keine vollständige Installation mit Data.p4k, StarCitizen_Launcher.exe und build_manifest.id gefunden." -ForegroundColor Yellow
    Write-Host "###############" -ForegroundColor Cyan
} elseif ($KompletteInstallationen.Count -eq 0) {
    Write-Host "###############" -ForegroundColor Cyan
}

# Warten auf Benutzereingabe, bevor das Fenster geschlossen wird
Write-Output "`nDruecken Sie die Eingabetaste, um das Fenster zu schliessen..."
[void][System.Console]::ReadLine()