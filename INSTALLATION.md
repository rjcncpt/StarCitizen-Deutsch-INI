# Anleitung zur Installation

### Variante 1: Automatisches Update der Übersetzung (SC Deutsch Launcher)
Der **SC Deutsch Launcher** ist eine einfache und benutzerfreundliche Lösung zur Umstellung der Spieltexte von Star Citizen auf Deutsch. Unsere kostenlose App kümmert sich automatisch um alle Dateianpassungen, stellt sicher, dass immer die aktuellsten deutschen Sprachdateien für Star Citizen von unserem GitHub installiert werden und startet im Anschluss automatisch den RSI Launcher für dich.

[<img src="https://www.sc-deutsch-launcher.de/img/sc-deutsch-launcher-ui_v2.webp">](https://www.sc-deutsch-launcher.de/download/ "SC Deutsch Launcher Download")

### So funktioniert’s:
1. Lade den SC Deutsch Launcher herunter.
   - Download-Link: [SC Deutsch Launcher](https://www.sc-deutsch-launcher.de/download/)
2. Entpacke die ZIP-Datei.
3. Kopiere das "SC Deutsch Launcher"-Verzeichnis an einen Ort deiner Wahl.
   - Zum Beispiel in das "Roberts Space Industries"-Verzeichnis
5. Starte die SC Deutsch Launcher.exe.
   - Unser Launcher benötigt die NET.8 Runtime. Diese wird möglicherweise vorher von microsoft.com heruntergeladen.
7. Der Launcher sucht automatisch nach deinem Star Citizen Ordner.
   - Gefundene Ordner sind grün.
   - Nicht gefundene Ordner bleiben schwarz.
8. Klicke auf "Update Übersetzung".
9. Der Launcher lädt die neuesten deutschen Sprachdateien herunter.
10. Der RSI Launcher startet automatisch wenn in den Einstellungen aktiviert.

[![SC Deutsch Launcher Download Portable](https://www.sc-deutsch-launcher.de/img/herunterladen.png)](https://www.sc-deutsch-launcher.de/download/)
<br/><br/><br/>


### Variante 2: Manueller Download - ZIP-Datei herunterladen

[<img src="https://i.imgur.com/rbsGtww.png" width="100%">](https://www.youtube.com/watch?v=_0H4Kc7s3Z4 "Installationsanleitung - Star Citizen in Deutsch")

Wenn du unseren **SC Deutsch Launcher** nicht verwenden möchtest, kannst du unsere Star Citizen Übersetzung auch händisch installieren.

1. **Lade die Neueste ZIP-Datei mit der Übersetzung herunter:** <br/>
   Manchmal musst du auf "Assets" klicken, um die Datei zu sehen.<br/><br/>
    <a href="https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases?q=preview&expanded=true">![Static Badge](https://img.shields.io/badge/ÜBERSETZUNG%20FÜR-brightgreen?style=for-the-badge&color=232323)![Static Badge](https://img.shields.io/badge/4.0%20PREVIEW%20(ZIP)-brightgreen?style=for-the-badge&color=ffffff)</a><br/><a href="https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases?q=live&expanded=true">![Static Badge](https://img.shields.io/badge/ÜBERSETZUNG%20FÜR-brightgreen?style=for-the-badge&color=232323)![Static Badge](https://img.shields.io/badge/3.24%20LIVE%20(ZIP)-brightgreen?style=for-the-badge&color=ffffff)</a><br/><a href="https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases?q=ptu&expanded=true">![Static Badge](https://img.shields.io/badge/ÜBERSETZUNG%20FÜR-brightgreen?style=for-the-badge&color=232323)![Static Badge](https://img.shields.io/badge/PTU%20(ZIP)-brightgreen?style=for-the-badge&color=ffffff)</a><br/><a href="https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases?q=eptu&expanded=true">![Static Badge](https://img.shields.io/badge/ÜBERSETZUNG%20FÜR-brightgreen?style=for-the-badge&color=232323)![Static Badge](https://img.shields.io/badge/EPTU%20(ZIP)-brightgreen?style=for-the-badge&color=ffffff)</a> <!-- https://shields.io/badges/git-hub-release --> <br/><br/>
2. **Entpacke die ZIP-Datei auf deine Festplatte** <br/>
3. **Kopiere den Inhalt (`data` Ordner und `user.cfg` Datei) der ZIP-Datei in den richtigen Ordner:**
   - Für die **3.24 LIVE**-Version: `C:\Program Files\Roberts Space Industries\StarCitizen\LIVE\`
   - Für die **4.0 PREVIEW**-Version: `C:\Program Files\Roberts Space Industries\StarCitizen\4.0_PREVIEW\`
   - Für die **PTU**-Version: `C:\Program Files\Roberts Space Industries\StarCitizen\PTU\`
   - Für die **EPTU**-Version: `C:\Program Files\Roberts Space Industries\StarCitizen\EPTU\`
   
   Der Pfad kann bei dir ein anderer sein.

![image](https://i.imgur.com/MjBMF4y.png)

<br/><br/>

------------------------------------

> [!IMPORTANT]  
> **Die Übersetzungsdatei wird regelmäßig verbessert. Neue Star Citizen Patches fügen oft neue Texte hinzu. Lade die ZIP-Datei also immer wieder neu herunter, um Fehler zu vermeiden. Oder nutze unseren Launcher der die Aufgabe für dich erledigt.**

> [!WARNING]  
> **Hast du eine eigene user.cfg Datei? Überschreibe sie nicht! Füge einfach diese zwei Zeilen hinzu:** <br/>
> ```
> g_language = german_(germany)
> g_languageAudio = english
> ```
