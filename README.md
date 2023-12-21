# 🇩🇪 [WIP] Star Citizen deutsche Lokalisierung (global.ini)

### Willkommen zur deutschen Lokalisierung für Star Citizen LIVE und PTU (inkl. Umlaute)

**Diese Lokalisierung ist ein Gemeinschaftsprojekt. Es ist eine große Herausforderung, die englischen Begriffe in ein verständliches Deutsch zu übertragen. Sollte es noch zu seltsamen Übersetzungen kommen, kannst du sehr gerne unser [Formular für einen Fehlerbericht verwenden](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/issues/new?assignees=&labels=Fehler&projects=&template=bug_report.md&title=).**
<br/><br/>

![Static Badge](https://img.shields.io/badge/LIVE-%234cc71e?style=for-the-badge&label=3.22.0%20) ![Static Badge](https://img.shields.io/badge/PTU-%234cc71e?style=for-the-badge&label=3.22.0%20) <!-- ![Static Badge](https://img.shields.io/badge/Bereit-%234cc71e?style=for-the-badge&label=3.22%20PTU)--> ![Static Badge](https://img.shields.io/badge/Kein%20Fokus-%23ff2f00?style=for-the-badge&label=Preview%20Channel) <br/>
![Static Badge](https://img.shields.io/badge/Work%20In%20Process-%23f3ac04?style=for-the-badge&label=ini) [![Static Badge](https://img.shields.io/badge/%F0%9F%92%96-%23fff?style=for-the-badge&label=Star%20Citizen)](https://robertsspaceindustries.com/) ![Github All Releases](https://img.shields.io/github/downloads/rjcncpt/StarCitizen-Deutsch-INI/total?style=for-the-badge&)

<br/>

### Inhaltsverzeichnis

- **[Download als Zip-Datei](#download-als-zip-datei)**
- **[Nur die global.ini herunterladen](#direktdownload-der-globalini)**
- **[Preview/Test Channels](#previewtest-channels)**
- **[Das Team](#das-team)**
- **[Bekannte Fehler](#bekannte-fehler)**
  <br/><br/>

Die **`global.ini`** ist ein Work In Progress (WIP) Projekt. Unsere Veröffentlichungen werden stets im Spiel getestet, aber dennoch können wir keine 100%ige Funktionalität garantieren. Es wird eine beträchtliche Zeit dauern, bis wir alle Texte von über 70000 Zeilen übersetzt und überprüft haben.
<br/><br/>
An manchen Stellen hat das Spiel Schwierigkeiten mit Umlauten, zum Beispiel bei Terminals oder MouseOver. Die Umlaute werden einfach weggelassen, und es entsteht eine Lücke. Dies ist keine Übersetzungspanne, sondern ein Spielfehler. Wir behalten diese Fehler absichtlich bei, damit CIG darauf reagieren kann, und wir selbst feststellen können, ob seitens CIG Fixes vorgenommen wurden.
<br/>
__________________
<br/>

## Anleitung zur Installation
### Download als Zip-Datei

**Täglich um 4 Uhr Nachts wird aus den Fixes des Vortags automatisch ein LIVE und/oder PTU Release erstellt. Releases werden nur dann erstellt, wenn in den letzten 24h Änderungen an den jeweiligen ini-Dateien vorgenommen wurden.**<br/><br/>

Lade dir **[die für dich passende ZIP Datei herunter](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases)** und entpacke diese im LIVE bzw. PTU Ordner. (Nutzt du die INI Datei für LIVE im PTU und umgekehrt, kann es zu Darstellungsfehlern kommen wenn sich die Versionsnummern unterscheiden.)<br/><br/>

In der ZIP Datei befindet sich die **`global.ini`** und die **`user.cfg`** Datei. Wenn du nicht möchtest das die **`user.cfg`** Datei deine eigene überschreibt, lade die **`global.ini`** **[als einzelne Datei herunter](#direktdownload-der-globalini)**. Diese findest du im **`live`** und **`ptu`** Ordner. Bitte nutze nur die Dateien, welche für den jeweiligen Channel ausgelegt sind.
<br/>

#### Installation

![image](https://i.imgur.com/USRwGWM.png)

1. Lade dir die **`StarCitizen.Deutsch.LIVE.zip`** oder **`StarCitizen.Deutsch.PTU.zip`** herunter
2. Entpacke diese
3. Kopiere den Inhalt in den LIVE bzw. PTU Ordner
<br/><br/><br/><br/>

### Direktdownload der global.ini

Du kannst die **[global.ini auch direkt aus dem Verzeichnis laden](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/live/global.ini)**, wenn du nicht immer die Zip-Datei herunterladen möchtest. Auch ist diese Datei immer auf einem aktuelleren Stand als die Release Datei.
<br/><br/>

- LIVE Datei: **[Hier klicken](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/live/global.ini)** und die `global.ini` Datei für LIVE öffnen
- PTU Datei: **[Hier klicken](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/ptu/global.ini)** und die `global.ini` Datei für PTU öffnen
<br/>

Klicke im neuen Fenster auf den Downloadbutton oben rechts. Im Screenshot gelb markiert.<br/><br/>

![image](https://i.imgur.com/jTabj3V.png)
<br/>

#### Wohin muss die global.ini Datei?

![image](https://i.imgur.com/lM3jimv.png)

- Erstelle die Ordner im Star Citizen Verzeichnis und füge die Datei ein. So muss der Dateipfad aussehen:<br/>
**`\ Roberts Space Industries \ StarCitizen \ LIVE \ data \ Localization \ german_(germany) \ global.ini`**<br/>
**`\ Roberts Space Industries \ StarCitizen \ PTU \ data \ Localization \ german_(germany) \ global.ini`**

- speichere ggf. die `user.cfg` in den LIVE oder PTU Ordner:<br/>
**`\ Roberts Space Industries \ StarCitizen \ LIVE \`**<br/>
**`\ Roberts Space Industries \ StarCitizen \ PTU \`**
<br/><br/><br/><br/>

### Preview/Test Channels

Test- und Preview-Kanäle werden von uns nicht unterstützt. Damit du an den Tests in englischer Sprache problemlos teilhaben kannst, füge in der **`user.cfg`** Datei ein **`;`** vor die Zeile **`g_language = german_(germany)`** hinzu. Du kannst selbstverständlich auch die aktuellste deutsche Übersetzung ausprobieren. Sei dir aber bewusst, dass es zu Darstellungsfehler kommen kann!
<br/><br/><br/><br/>

### Das Team

| Team Name                                   | Position             | Aufgaben                                   |
|:--------------------------------------------|:---------------------|:-------------------------------------------|
| [rjcncpt](https://github.com/rjcncpt)       | `Ansprechparter`     | Übersetzungen & GitHub                     |
| [MaxM1211](https://github.com/MaxM1211)     | `Dev & Bugfixing`    | Korrekturen, GitHub, Dev & Bugfixing       |
| [greluc](https://github.com/greluc)         | `Übersetzer`         | Übersetzungen, GitHub                      |
| [Norinofu](https://github.com/Norinofu)     | `Dev & Bugfixing`    | Korrekturen, GitHub                        |
| [Drakonhawk](https://github.com/Drakonhawk) | `Dev & Bugfixing`    | GitHub, Dev & Bugfixing                    |
| Boy7                                        | `Dev & Bugfixing`    | Übersetzungen, Dev & Bugfixing             |
| Hikaruhoshi1                                | `Übersetzer`         | Übersetzungen                              |
| electron0                                   | `Dev & Bugfixing`    | GitHub, Dev & Bugfixing                    |
| APROVES                                     | `Übersetzer`         | Übersetzungen                              |
| Asaya87                                     | `Discord Management` | Übersetzungen & Discord Admin              |
| Fabi 18                                     | `Discord Management` | Discord Admin                              |

<br/>

| Dankeschön       | Position   | Beschreibung                                                                                                                       |
|:-----------------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------|
| Claudia Fröhlich | `Lektorin` | © Einige Textblöcke werden von ihr für etwas Geld Korrektur gelesen.                                                               |
| Knebel Discord   |            | Ein großes Dankeschön geht an die vielen Einsender der **[Knebel Discord Community](https://discord.com/invite/knebel)** \*Invite-Link |

<br/><br/>

### Bekannte Fehler

<details>
<summary>[Klick] Fehler: Es werden kryptische Variablen mit @-Zeichen am Anfang angezeigt</summary>
<br/>

Unsere **`global.ini`** Datei liegt bereits im korrekten **`UTF-8-BOM`** im Format vor. Wenn bei dir Variablen angezeigt werden, die mit einem @-Zeichen beginnen, aber die Ordnerstuktur richtig ist, scheint deine Datei-Codierung falsch zu sein. Lade entweder **[unsere Datei erneut herunter](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/live/global.ini)** oder stelle die Codierung deiner Datei manuell um:
<br/><br/>

1. Öffne die **`global.ini`** in einem Texteditor wie Notepad++ (kostenlos)
2. Klicke anschließend in der Symbolleiste auf "Codierung"
3. Wähle **`UTF-8-BOM`**
4. Speichern
<br/><br/>

Das sollte das Problem beheben.
___________
</details>


<details>
<summary>[Klick] Fehler: Ich habe alles richtig gemacht, aber es werden immer noch englische Texte angezeigt</summary>
<br/>

Achte bei den beiden Dateien **`global.ini`** und **`user.cfg`** auf die richtigen Dateiendungen.
<br/><br/>

Kontrolliere ob es die richtige Dateiendung ist:

1. Öffne den Windows Dateiexplorer
2. Klicke auf Ansicht am oberen Fensterrand
3. Aktiviere im Bereich Ein-/ausblenden: **`Dateinamenerweiterungen`**
4. Sollten die beiden Dateien nun **`global.ini.ini`** oder **`user.txt.cfg`** oder ähnlich heißen, musst du sie zurück in **`global.ini`** und **`user.cfg`** umbennenen.
<br/><br/>

Das sollte das Problem beheben.
___________
</details>


<details>
<summary>[Klick] Fehler: Keine englische Sprachausgabe im Spiel</summary>
<br/>

Es gibt einen Fix für das Audio Problem. Du musst deiner **`user.cfg`** Datei diese folgende Zeile hinzufügen:<br/>
**`g_languageAudio = english`**<br/><br/>
Alternativ lade dir unsere **`user.cfg`** Datei herunter, in der wir das bereits für dich übernommen haben.
<br/><br/>

Das sollte das Problem beheben.
___________
</details>

<br/><br/>
Salut and stay tuned!

<br/><br/><br/><br/>
-------<br/>
**Note about lecturer**<br/>
The entire repository is licensed under a [CC-BY-4.0](http://creativecommons.org/licenses/by/4.0/) license. To provide the best possible quality, we commission a lecturer to proofread some of the text modules. The copyright is held by Claudia Fröhlich. You may use our global.ini file privately and commercially, but you must not identify yourself as the author of this global.ini.
<br/><br/>
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg?style=for-the-badge)](https://creativecommons.org/licenses/by/4.0/)
