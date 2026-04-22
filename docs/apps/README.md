# Tools & Web-Apps
Auf dieser Seite listen wir eigens entwickelte und 3rd Party Tools und Web-Apps auf.

<br/>

### Inhaltsverzeichnis

- **[SC Deutsch Launcher (Auto Übersetzungsupdate)](#automatisches-übersetzungsupdate)**
- **[INI File Viewer (Web-App)](#ini-file-viewer-web-app)**
- **[Besseres Spectrum Dark Theme (Chrome Extension)](#besseres-spectrum-dark-theme-chrome-extension)**
- **[Symbolic Link vom LIVE Ordner erstellen](#symbolic-link-vom-live-ordner-erstellen)**
- **[SC Launch Conigurator (Tool)](#sc-launch-configurator)**

<br/><br/>

## Automatisches Übersetzungsupdate
![SC Deutsch Launcher Download](https://www.sc-deutsch-launcher.de/img/sc-deutsch-launcher-social.webp)

Der **SC DEUTSCH LAUNCHER** ist eine von uns entwickelte kostenfreie App, welche es dir ermöglicht, die Sprachen deiner Star Citizen Installation(en) bequem von Englisch auf Deutsch und wieder zurück zu stellen. Darüberhinaus erfolgt nach dem Update der Übersetzungsdateien der Start des RSI Launcher.<br/><br/>

[![SC Deutsch Launcher Download Portable](https://www.sc-deutsch-launcher.de/img/herunterladen.png)](https://www.sc-deutsch-launcher.de)

--------------------------------------------------------
<br/><br/><br/><br/>

## Manueller Download über Webapp
![SC Deutsch Launcher Download](https://www.sc-deutsch-launcher.de/img/sprachdatei-downloader-webapp.webp)

Wenn du unseren **SC Deutsch Launcher** nicht verwenden möchtest und stattdessen alles manuell erledigen willst, haben wir eine benutzerfreundliche Webapp entwickelt. Diese Webapp bietet dir die Möglichkeit, die aktuellen Releases für LIVE und PTU bequem als Zip-Archiv herunterzuladen, ohne dich durch GitHub-Seiten klicken zu müssen. Über ein Dropdown-Menü kannst du einfach auswählen, ob du den neuesten LIVE- oder PTU-Release herunterladen möchtest.<br/><br/>

Zur Webapp: https://www.sc-deutsch-launcher.de/apps/sc_release/ <br/>
Youtube Tutorial (Ab 0:15 Sekunden): https://youtu.be/_0H4Kc7s3Z4?si=wAe1GN7ylMPy4eCG&t=15

--------------------------------------------------------
<br/><br/><br/><br/>

## INI File Viewer (Web-App)
Eine Web-App, um bei der Suche nach fehlerhaften Texten zu unterstützen. Dabei wird die aktuelle global.ini-Datei aus dem `/live`-Verzeichnis unseres GitHub-Repositories ausgelesen und alle Einträge untereinander dargestellt.

![image](https://i.imgur.com/IzEfJKU.png)

### Formatierung
Wenn du auf die "Formatieren"-Checkbox klickst, werden alle Anfangsvariablen entfernt und alle `\n` werden durch Zeilenumbrüche ersetzt. So siehst du, wie der Text im Spiel dargestellt wird.

![image](https://i.imgur.com/Hh4yn6i.png)

### Filter- und Suchfunktion
Eine Filter- und Suchfunktion, die es ermöglicht, den Text, den du als fehlerhaft empfindest, direkt zu suchen oder aus vorgegebenen Filtern direkt die Kategorie anzuspringen. Filter und Suche sind kombinierbar, so dass du deine Suche auf einen Filter begrenzen kannst.

![image](https://i.imgur.com/vr8AGqA.png)

### Webseite
Hier geht es zur App: [https://www.sc-deutsch-launcher.de/apps/ini-file-viewer/](https://www.sc-deutsch-launcher.de/apps/ini-file-viewer/)

--------------------------------------------------------
<br/><br/><br/><br/>

## Besseres Spectrum Dark Theme (Chrome Extension)
![image](https://i.imgur.com/tpAHE8n.png)

Ich habe den CSS-Code für die Star Citizen Spectrum- und RSI-Website überarbeitet, da mir das ursprüngliche Farbschema nicht gefallen hat. Das auffällige Blau der Website habe ich dezenter gestaltet. Die Avatare sind jetzt rund, die Schriftarten sind besser lesbar, und ich habe die gelbe Staff-Schriftfarbe sowie die Hintergrundgrafiken entfernt. 

Insgesamt wirkt Spectrum nun viel aufgeräumter. Die Galerie wurde komplett überarbeitet und zeigt die Bilder jetzt nebeneinander statt untereinander, was viel Platz spart.<br/>

### Download

- [SpectrumDarkMode auf GitHub](https://github.com/rjcncpt/SpectrumDarkMode-Chrome-Extension/releases/)
- [SpectrumDarkMode im Chrome Web-Shop](https://chrome.google.com/webstore/detail/star-citizen-better-spect/omcmgcldeclkpakdccipdajcfddhcdkj)

--------------------------------------------------------
<br/><br/><br/><br/>

## Symbolic Link vom LIVE Ordner erstellen
![image](https://i.imgur.com/HrASh6V.png)

Der ständige Download von vielen Gigabyte Daten, wenn man zwischen LIVE und PTU wechselt, ist unnötig. Erstelle mit einem winzigen Tool eine symbolische Verknüpfung des LIVE Verzeichnisses und spare dir Zeit. Ein "Symbolic Link" ist nichts anderes als eine Verknüpfung, funktioniert jedoch anders.

### Symbolic Link für Ordner

- Ein Symbolic Link für einen Ordner ist eine Verknüpfung zu einem Verzeichnis, die einen Pfad zu einem anderen Verzeichnis darstellt.
- Symbolic Links können auf andere Laufwerke oder Netzwerkpfade verweisen.
- Änderungen am Zielordner beeinflussen den Symbolic Link und umgekehrt.
- Symbolic Links sind flexibler, da sie auf nicht existierende Pfade zeigen können.

### So geht's

1. Lade dir das Tool herunter: https://sourceforge.net/projects/symlink-creator/
2. Öffne die `SymlinkCreator.exe`
3. **Type of Link:** Wähle die Option `Directory Symbolic Link (/D)`
4. **Destination (Link):** Wähle dein Zielverzeichnis. Zum Beispiel PTU
5. **Source (Target):** Wähle das Quellverzeichnis. In diesem Fall LIVE
6. Klicke auf **Create Link**

<br/>Wenn du alles richtig gemacht hast und alle Verknüpfungen erstellt hast, die du brauchst, sollte es wie bei mir aussehen.

![image](https://i.imgur.com/VAsoJBz.png)

<br/>Jetzt brauchst du im RSI-Launcher nur noch die entsprechende Testumgebung auswählen und es werden immer nur die fehlenden Daten installiert, weil die Grundlage der symbolischen Verknüpfung der LIVE Ordner ist. Damit entfällt das Umbenennen oder Kopieren der Ordner.

![image](https://i.imgur.com/cEVsdeS.png)

<br/>

> [!IMPORTANT]  
> **Wenn du die Reihenfolge im Tool vertauschst, löschst du den LIVE Ordner. Also achte auf Quell- und Zielverzeichnis. Orientiere dich an meinem Screenshot.**



--------------------------------------------------------
<br/><br/><br/><br/>

## SC Launch Configurator
![image](https://www.luftwerft.com/images/sclc_en.png)

<p>Der SC Launch Configurator ist ein umfassendes Werkzeug für Star Citizen-Spieler, das als Erweiterung aller Spieleinstellungen dient. Es deckt Bereiche wie Spieleinstellungen, Grafik, Audio, Steuerung, Tastenbelegungen, Kommunikation, FOIP und Headtracking ab. Mit nur einem Mausklick können alle Star Citizen-Übersetzungen installiert, verwaltet und automatisch auf dem neuesten Stand gehalten werden. Die vollautomatische Updatefunktion sorgt dafür, dass die gewählte Sprache immer aktuell ist.</p>

<p>Das Programm überwacht nicht nur das Spiel oder den RSI Launcher, sondern erkennt auch Dateisystemänderungen aufgrund von Spielmodifikationen. Benutzer können Profile für alle Spielanpassungen speichern und vor dem Spiel nach Bedarf aktivieren. Der SC Launch Configurator ermöglicht nicht nur eine optimierte Spielerfahrung, sondern auch das mühelose Erzeugen von Hardcopies für jedes Build, was an Patchtagen eine erhebliche Zeitersparnis bedeutet.</p>

**<p>Download: https://www.luftwerft.com</p>**


<br/><br/>
Salut and stay tuned!

[![Made by the Community](https://i.imgur.com/2RWyGPJ.png)](#)

<br/><br/><br/><br/>
-------<br/>
**Urheberrecht und CC-Lizenz**<br/>
Das gesamte GitHub-Repository sowie individuelle Texte in den global.ini-Dateien, die sich erheblich in ihrer Schöpfungshöhe vom Original abheben, sind urheberrechtlich geschützt und unterliegen der freien [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) Lizenz. Dies bedeutet, dass Sie die Inhalte für nicht-kommerzielle Zwecke nutzen, bearbeiten und weiterverbreiten dürfen, solange Sie die Urheberschaft angeben und die gleiche Lizenz für Ihre Weiterbearbeitungen verwenden.
<br/><br/>
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_NC_SA_4.0-lightgrey.svg?style=for-the-badge)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
