# [WIP] StarCitizen Deutsch global.ini
### Willkommen zu unserer deutschen Lokalisierung für Star Citizen mit Umlaute.

**Diese Lokalisierung ist ein Gemeinschaftsprojekt und wird sich in vielen Bereichen unterscheiden. Es ist eine große Herausforderung, die englischen Begriffe ins verständliche Deutsch zu übertragen. Oft können wir keine 1:1-Übersetzung verwenden, da einige englische Begriffe in der deutschen Sprache mehrere Bedeutungen haben.**
<br/>

![Static Badge](https://img.shields.io/badge/Ready-%2339cb75?label=3.21.0%20LIVE) ![Static Badge](https://img.shields.io/badge/Work%20In%20Process-%23f3ac04?label=ini) ![Static Badge](https://img.shields.io/badge/%F0%9F%92%96-%23fff?label=Star%20Citizen)
<br/><br/>

### Table of Content
* [Das Team](https://github.com/rjcncpt/StarCitizen-Deutsch-INI#das-team)
* [Direktdownload der global.ini](https://github.com/rjcncpt/StarCitizen-Deutsch-INI#direktdownload-der-globalini)
* [Download als ZIP](https://github.com/rjcncpt/StarCitizen-Deutsch-INI#download-als-zip)
* [Installation](https://github.com/rjcncpt/StarCitizen-Deutsch-INI#installation)
* [Troubleshooting](https://github.com/rjcncpt/StarCitizen-Deutsch-INI#troubleshooting)
<br/><br/>

Die `global.ini` ist ein Work In Progress (WIP) Projekt. Unsere Veröffentlichungen werden stets im Spiel getestet, aber dennoch können wir keine 100%ige Funktionalität garantieren. Es wird eine beträchtliche Zeit dauern, bis wir alle Texte manuell von Zeile 1 bis etwa Zeile 62000 übersetzt und überprüft haben.
<br/><br/>
An manchen Stellen hat das Spiel Schwierigkeiten mit Umlauten, zum Beispiel bei Terminals oder MouseOver. Die Umlaute werden einfach weggelassen, und es entsteht eine Lücke. Dies ist keine Übersetzungspanne, sondern ein Spielfehler. Wir behalten diese Fehler absichtlich bei, damit CIG darauf reagieren kann, und wir selbst feststellen können, ob seitens CIG Fixes vorgenommen wurden.
<br/><br/><br/>

### Das Team
| Team | Position | Beschreibung |
| :--- | :--- | :--- |
| [rjcncpt](https://github.com/rjcncpt) | `Management` | Übersetzungen & GitHub |
| [MaxM1211](https://github.com/MaxM1211) | `Management` | Korrekturen & GitHub |
| [Norinofu](https://github.com/Norinofu) | `Management` | GitHub |
| [Drakonhawk](https://github.com/Drakonhawk) | `Management` | Korrekturen & GitHub |
| APROVES | `Übersetzer-Team` | Übersetzungen |
| Hikaruhoshi1 | `Übersetzer-Team` | Übersetzungen |
| electron0 | `Übersetzer-Team` | GitHub & Development |
| Asaya87 | `Discord Management` | |
| Fabi 18 | `Discord Management` | |
<br/>

| Dankeschön | Position | Beschreibung |
| :--- | :--- | :--- |
| Claudia Fröhlich | `Lektorin` | © Einige Textblöcke werden von ihr für etwas Geld korrekturgelesen. |
| Knebel Discord | | Ein großes Dankeschön geht an die vielen Einsender der [Knebel Discord Community](https://discord.com/invite/knebel)*Invite-Link |

<br/><br/>

### Direktdownload der global.ini
Du kannst die [global.ini direkt aus dem Verzeichnis laden](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/global.ini). Ein Vorteil ist, dass sie oft aktueller ist.<br/><br/>
![image](https://i.imgur.com/jTabj3V.png)
<br/>

### Wohin muss die global.ini Datei?
1. [Klicke hier](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/global.ini) und öffne die `global.ini` Datei
2. klicke im neuen Fenster auf den Downloadbutton oben rechts. Im Screenshot gelb markiert.
3. Erstelle die Ordner im Star Citizen Verzeichnis und füge die Datei ein. So muss der Dateipfad aussehen:<br/>
`\ Roberts Space Industries \ StarCitizen \ LIVE \ data \ Localization \ german_(germany) \ global.ini`
4. speichere ggf. die user.cfg in den LIVE oder PTU Ordner:<br/>
`\ Roberts Space Industries \ StarCitizen \ LIVE \`<br/>
`\ Roberts Space Industries \ StarCitizen \ PTU \`
<br/><br/><br/><br/>

### Download als ZIP
Das ZIP ist eine stable Version aber nicht immer aktuell zur `global.ini` die im Main liegt.<br/>
https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases
<br/><br/>

### Installation aus ZIP Datei
Im ZIP ist auch die user.cfg enthalten.

1. Lade dir die `Deutsche.SC.Lokalisierung.zip` herunter
2. entpacke diese
3. kopiere den Inhalt in den LIVE oder PTU Ordner
<br/><br/><br/><br/>

### Troubleshooting
Die `global.ini` liegt im Format `UTF-8-BOM` vor. Das ist eigentlich unnötig, und `UTF-8` würde ausreichen. Aus unerklärlichen Gründen führt dies bei einigen zu Problemen, bei denen statt der Übersetzung kryptische Variablen, die mit einem @-Zeichen beginnen, angezeigt werden. Wenn du alles richtig gemacht hast und die Datei sich im korrekten Ordner befindet, musst du wahrscheinlich die Codierung der Datei von `UTF-8` auf `UTF-8-BOM` ändern.
<br/><br/>
1. öffne die `global.ini` in einem Texteditor wie Notepad++ (kostenlos)
2. klicke anschliefend in der Symbolleiste auf "Codierung"
3. wähle `UTF-8-BOM`
4. speichern
<br/><br/>

Das sollte das Problem beheben.
<br/><br/>

Salut and stay tuned!


<br/><br/><br/><br/>
-------<br/>
**Note about lecturer**<br/>
The entire repository is licensed under a [CC-BY-4.0](http://creativecommons.org/licenses/by/4.0/) license. To provide the best possible quality, we commission a lecturer to proofread some of the text modules. The copyright is held by Claudia Fröhlich. You may use our global.ini file privately and commercially, but you must not identify yourself as the author of this global.ini.
<br/><br/>
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
