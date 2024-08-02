# Anleitung zur Installation

**Freitag ist Patchday. Jeden Freitag erstellen wir aus den Änderungen der Woche einen neuen Release.**

[<img src="https://i.imgur.com/rbsGtww.png" width="100%">](https://www.youtube.com/watch?v=_0H4Kc7s3Z4 "Installationsanleitung - Star Citizen in Deutsch")

> [!IMPORTANT]  
> **Um fehlende Übersetzungen und @-Fehler zu vermeiden, aktualisiere regelmäßig die Übersetzungsdatei. Wir optimieren regelmäßig unsere Übersetzung (durch Community Reports, Stream Beobachtungen etc.) und steigern ständig dessen Qualität. Außerdem kommen mit nahezu jedem Patch neue Zeilen hinzu, die Dir sonst im Spiel fehlen und als @-Fehler angezeigt werden.**
>
> **Auf unserem [Übersetzungs Discord-Server](https://discord.gg/5VZsTk3qjR) wirst du immer bei neuen Updates informiert und kannst aktiv an der Übersetzung mitwirken und ein Teil dieser werden.**

<br/>

### Variante 1: Download der ZIP-Datei
1. **Lade dir die neueste Übersetzung als ZIP-Datei herunter:** <br/>
   Ggf. musst du auf "Assets" klicken um die ZIP-Datei anzuzeigen.<br/><br/>
    <a href="https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases?q=live&expanded=true">![Static Badge](https://img.shields.io/badge/LIVE-brightgreen?style=for-the-badge&color=232323)![GitHub Release](https://img.shields.io/github/v/release/rjcncpt/StarCitizen-Deutsch-INI?include_prereleases&sort=date&filter=*LIVE*&display_name=release&style=for-the-badge&labelColor=232323&label=%20)</a><br/><a href="https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases?q=ptu&expanded=true">![Static Badge](https://img.shields.io/badge/PTU-brightgreen?style=for-the-badge&color=232323)![GitHub Release](https://img.shields.io/github/v/release/rjcncpt/StarCitizen-Deutsch-INI?include_prereleases&sort=date&filter=*PTU*&display_name=release&style=for-the-badge&labelColor=232323&label=%20)</a> <!-- https://shields.io/badges/git-hub-release --> <br/><br/>
2. **Entpacke die ZIP-Datei auf deine Festplatte** <br/>
3. **Kopiere den kompletten Inhalt der entpackten ZIP-Datei in den LIVE bzw. PTU/EPTU Ordner:** <br/>

![image](https://i.imgur.com/MjBMF4y.png)

   Speicherort (Laufwerksbuchstaben kann bei dir ein anderer sein):
   - `C:\ Program Files \Roberts Space Industries \ StarCitizen \ LIVE \` <br/>
   - `C:\ Program Files \Roberts Space Industries \ StarCitizen \ PTU \` <br/><br/>

> [!WARNING]  
> **Nutzt du eine eigene `user.cfg` Datei mit eigenen Anpassungen, überschreibe deine Datei auf keinen Fall. Ergänze deine Datei mit folgenden zwei Zeilen:** <br/>
> ```
> g_language = german_(germany)
> g_languageAudio = english
> ```

<br/><br/>
### Variante 2: Direktdownload der global.ini Datei
1. **Öffne die global.ini für [LIVE](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/live/global.ini) oder [PTU](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/ptu/global.ini)**
2. **Klicke links auf das "herunterladen"-Symbol und bestätige ggf. den Download.**
3. Bei Erstinstallation, erstelle die Ordnerstruktur im LIVE bzw. PTU Verzeichnis:
   - `data \ Localization \ german_(germany) \` <br/><br/>
4. Kopiere die heruntergeladene `global.ini` in den jeweiligen Star Citizen Installationspfad. <br/>
`\ LIVE \ data \ Localization \ german_(germany) \ global.ini` <br/>
`\ PTU \ data \ Localization \ german_(germany) \ global.ini`

<br/><br/>

### Variante 3: Automatisches Übersetzungs-Update (experimentell)
Nicht empfohlen da GitHub API Rate Limits setzt und in Stoßzeiten der automatische Download blockiert wird. Möchtest du trotzdem mehr darüber erfahren, **[auf dieser Seite](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/tree/main/docs_tools/apps#automatisches-%C3%BCbersetzungsupdate-bat)** zeigen wir dir welche Möglichkeiten du hast.
