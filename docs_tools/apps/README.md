# Tools & Web-Apps
Auf dieser Seite listen wir eigens entwickelte und 3rd Party Tools und Web-Apps auf.

<br/>

### Inhaltsverzeichnis

- **[Automatisches Übersetzungsupdate](#automatisches-übersetzungsupdate)**
- **[INI File Viewer (Web-App)](#ini-file-viewer-web-app)**
- **[Sprachdatei Downloader (Web-App)](#sprachdatei-downloader-web-app)**
- **[Besseres Spectrum Dark Theme (Chrome Extension)](#besseres-spectrum-dark-theme-chrome-extension)**
- **[Symbolic Link vom LIVE Ordner erstellen](#symbolic-link-vom-live-ordner-erstellen)**
- **[SC Launch Conigurator (Tool)](#sc-launch-configurator)**

<br/><br/>

## Automatisches Übersetzungsupdate
![SC Deutsch Launcher Download](https://i.imgur.com/LcQRK6l.png)

Der **SC DEUTSCH LAUNCHER** ist eine von uns erstellte kostenfreie App, welche es dir ermöglicht, deine Star Citizen Installation(en) bequem von Englisch auf Deutsch und wieder zurück zu stellen.<br/><br/>

[![SC Deutsch Launcher Download](https://i.imgur.com/aZ0vkfF.png)](https://www.fwkart.de/sc-deutsch-launcher)
- **Version 1.2.1 (24. August 2024)**
- **[Dokumentation (PDF)](https://www.fwkart.de/apps/Dokumentation-SC-Deutsch-Launcher.pdf)**

<br/>

## Installationsanleitung

> [!IMPORTANT]  
> **Falls du die Version 1.0 (08. August 2024) installiert hast: Für eine saubere Installation, deinstalliere vor der Neuinstallation die alten Dateien komplett von deiner Festplatte.**

1. Entpacke das Zip und führe die `Install SC Deutsch Launcher.exe` aus.
2. Öffne nach der Installation den SC DEUTSCH LAUNCHER und konfiguriere das Programm.

Beim erstmaligen Start überprüft der SC DEUTSCH LAUNCHER automatisch, ob und auf welcher Festplatte Star Citizen installiert ist. Gefundene Installationen werden grün markiert, nicht erkannte Installationen bleiben schwarz.

Falls der SC DEUTSCH LAUNCHER keine Installation(en) automatisch erkennt, weil du Star Citizen in einem anderen Ordner installiert hast, den unsere App nicht findet, kannst du den Pfad manuell angeben:
1. Klicke auf den Button der gesuchten Installation (z.B. LIVE), um einen Datei-Explorer zu öffnen.
2. Navigiere zu dem Ordner, der das Verzeichnis /LIVE enthält (z.B. `D:/Roberts Space Industries/StarCitizen/LIVE)` und wähle "Öffnen".
3. Die Installation wird nun erkannt, grün markiert und der Pfad gespeichert.
4. Wiederhole diesen Vorgang für alle weiteren Installationen, die du verwenden möchtest.<br/><br/>

### Sprachen konfigurieren
Rechts neben den Buttons für die Spiel-Installationen (z.B. LIVE) kannst du die Sprache auswählen, die in Star Citizen verwendet werden soll. Durch Klicken auf den Button “eng” oder “de” stellst du die gewünschte Sprache ein. Für die LIVE-Version gibt es eine experimentelle Übersetzung (“de (voll)”), die alle Spieltexte ins Deutsche übersetzt. Weitere Informationen dazu findest du unter: https://github.com/rjcncpt/StarCitizen-Deutsch-INI

Die Spracheinstellungen gelten für alle erkannten Installationen. Die Pfadkonfiguration, Anpassungen der user.cfg-Datei und Updates der Sprachdateien werden automatisch im nächsten Schritt vorgenommen.<br/><br/>

### Update & Start
Wenn du auf “Update & Start” klickst, führt der Launcher automatisch alle notwendigen Dateianpassungen durch und lädt die neuesten Übersetzungsdateien von GitHub herunter. Anschließend wird der RSI-Launcher gestartet. Sollte sich der RSI-Launcher nicht im Standard-Installationspfad befinden, öffnet sich ein Datei-Explorer. Wähle dort die Datei “RSI Launcher.exe” aus, um den Pfad zu speichern.<br/><br/>

### Automatische Updates und Launcher-Start
Nach der ersten Konfiguration kannst du den gesamten Prozess, einschließlich Updates und Start des RSI-Launchers, vollständig automatisieren: Nachdem du die `SC DEUTSCH LAUNCHER`-App konfiguriert hast, inklusive der Zuordnung der Sprachdateien, kannst du für zukünftige Starts die `SC Deutsch Launcher (auto)`-Verknüpfung auf deinem Desktop oder im Startmenü verwenden, um den gesamten Vorgang automatisch ausführen zu lassen.<br/><br/>

### Das Icon ändern

1. Klicke auf dem Desktop mit der rechten Maustaste auf die **`SC Deutsch Launcher`** oder **`SC Deutsch Launcher (auto)`** Verknüpfung
2. Wähle `Eigenschaften` aus
3. Wähle `Anderes Symbol` ⇾ `Durchsuchen` und suche dir ein Icon aus

Tipp: Verwende die Spiel-Icons. Navigiere zum Star Citizen Ordner, um das SC Icon zu verwenden, oder zum RSI Launcher, um das Launcher Icon zu verwenden.

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
Hier geht es zur App: [https://fwkart.de/apps/ini-file-viewer/](https://fwkart.de/apps/ini-file-viewer/)

--------------------------------------------------------
<br/><br/><br/><br/>

## Sprachdatei Downloader (Web-App)
![image](https://i.imgur.com/dkuXC2W.png)

Erspare dir den Weg über GitHub um den neuesten Release der Übersetzung herunterzuladen. Eine Web-App mit der du ganz leicht den neuesten Build aus einem Dropdown-Menü auswählen und herunterladen kannst.<br/>

### Webseite
Hier geht es zur App: [https://fwkart.de/apps/sc_release/](https://fwkart.de/apps/sc_release/)

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
