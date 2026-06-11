[![Static Badge](https://img.shields.io/badge/LIVE%204.8.1-brightgreen?style=for-the-badge&color=232323)![Static Badge](https://img.shields.io/badge/✔-%234cc71e?style=for-the-badge&labelColor=232323%20)](#) [![Static Badge](https://img.shields.io/badge/EVOCATI-brightgreen?style=for-the-badge&color=232323)![Static Badge](https://img.shields.io/badge/X-%23db0909?style=for-the-badge&labelColor=red%20)](#evocati-builds-und-tech-preview-channels) [![Static Badge](https://img.shields.io/badge/%F0%9F%92%96-%23fff?style=for-the-badge&labelColor=232323&label=Star%20Citizen)](https://robertsspaceindustries.com/) <br/>
[![Static Badge](https://img.shields.io/badge/Sag%20dem%20Team%20Danke-brightgreen?style=for-the-badge&logo=kofi&logoColor=fff&logoSize=auto&label=Ko-fi&labelColor=red&color=fff)](https://ko-fi.com/scdeutsch) [![Static Badge](https://img.shields.io/badge/57k-brightgreen?style=for-the-badge&logoColor=000&label=Downloads&labelColor=232323&color=fff)](https://grev.shehryar.ae/?owner=rjcncpt&repo=StarCitizen-Deutsch-INI) [![Discord](https://img.shields.io/discord/1234564972198236261?style=for-the-badge&logo=discord&logoColor=fff&label=Discord&labelColor=232323&color=4cc71e)](https://discord.gg/5VZsTk3qjR)

[![Star Citizen in Deutsch](https://i.imgur.com/WAP6UNa.png)](#)

# Star Citizen in Deutsch - Lokalisierung für LIVE

Die deutsche Sprachdatei für Star Citizen ist ein Gemeinschaftsprojekt, das darauf abzielt, Star Citizen im deutschsprachigen Raum zugänglicher und verständlicher zu gestalten. Das Projekt trägt dazu bei, den Erfolg des Spiels zu fördern und ein besseres Spielerlebnis für deutsche Spieler zu schaffen, indem wir die Immersion und das Verständnis durch eine sorgfältig angepasste Übersetzung stärken.

Hilf mit, die Übersetzung zu verbessern! Trete **[unserem öffentlichen Übersetzungs-Discord](https://discord.gg/5VZsTk3qjR)** bei, starte **[eine Diskussion](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/discussions/categories/%C3%BCbersetzungsvorschl%C3%A4ge)** oder erstelle **[ein Issue](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/issues/new?assignees=&labels=Fehler&projects=&template=bug_report.md&title=)** hier auf Github, um uns deine Vorschläge mitzuteilen.

<br>

### SCMDB Übersetzungsdatei
Unsere Übersetzung für SCMDB. Klicke folgenden Link und die SCMDB-Übersetzung wird automatisch installiert.

**Link: [https://scmdb.net/?lang=https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/refs/heads/main/scmdb/lang-de.json](https://scmdb.net/?lang=https://raw.githubusercontent.com/rjcncpt/StarCitizen-Deutsch-INI/refs/heads/main/scmdb/lang-de.json)**

---

### Inhaltsverzeichnis

- **[Über diese Übersetzung](#über-diese-übersetzung)**
- **[Anleitung zur Installation](#anleitung-zur-installation)**
- **[Baupläne-Missionsintegration & Datenbank](#ini-injections)**
- **[Wie aktuell ist die deutsche Übersetzung?](#wie-aktuell-ist-die-deutsche-übersetzung)**
- **[Fragen und Antworten](#fragen-und-antworten)**

---

<br>

## Über diese Übersetzung

![Star Citizen Deutsch Hauptmenü](https://www.sc-deutsch-launcher.de/img/thumbnails/alpha-4.0-home.png)

Wir stellen zwei Varianten unserer Sprachdatei bereit:
- eine **Standard-Übersetzung (Hybrid)** sowie
- eine darauf basierende **erweiterte Version (Deutsch+)**.

Grundsätzlich sind in unserer Übersetzung Eigennamen, Missionstitel, Items und Orte/Unternehmen nicht übersetzt. Die erweiterte Version unterscheidet sich nur in zwei Punkten: Hier werden die Missionstitel ebenfalls übersetzt und in den Item-Beschreibungen entfällt die englische Typbezeichnung. 

Wir interpretieren Missionstexte neu: Um holprige Formulierungen durch komplexe Verzweigungen und Keys zu bewältigen, haben wir komplexe Missions-, Journal- und Reputationstexte analysiert und ein eigenständiges Questlog-Layout erschaffen, um die Lesbarkeit zu vereinfachen.

---

<br>

## Anleitung zur Installation

### Variante 1: Automatisches Update der Übersetzung (SC Deutsch Launcher)
Der **SC Deutsch Launcher** ist eine einfache und benutzerfreundliche Lösung zur Umstellung der Star Citizen Spieltexte von Englisch auf Deutsch. Unsere kostenlose App kümmert sich automatisch um alle Dateianpassungen und stellt sicher, dass immer die aktuellsten deutschen Sprachdateien installiert werden.

[<img src="https://www.sc-deutsch-launcher.de/img/features/2026/sc-deutsch-launcher-ui_v2026.webp?t=177451851">](https://www.sc-deutsch-launcher.de/download/ "SC Deutsch Launcher Download")

1. Lade den **[SC Deutsch Launcher](https://www.sc-deutsch-launcher.de/download/)** herunter und installiere ihn.
2. Nach der Installation, starte den SC Deutsch Launcher.
3. Der Launcher sucht automatisch nach deinem Star Citizen Verzeichnis.
4. Wird keine Star Citizen Installation gefunden oder treten andere Probleme auf, komme gern auf **[unseren Support-Discord](https://discord.gg/5VZsTk3qjR)** und wir helfen dir bei dem Problem.

<br>

### Variante 2: Manueller Download (ZIP-Datei)

1. Lade die **[Neueste ZIP-Datei](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/releases?q=live&expanded=true)** mit der Übersetzung herunter.
2. Entpacke die ZIP-Datei auf deine Festplatte.
3. Kopiere den Inhalt (`data` Ordner und `user.cfg` Datei) in den richtigen Ordner (Standard: `C:\Program Files\Roberts Space Industries\StarCitizen\LIVE\`).

<img width="1040" height="415" alt="installationspfad" src="https://github.com/user-attachments/assets/1d28aa53-8138-4f02-aa7e-869c35288089" />
<br>

> [!IMPORTANT]
> **Die Übersetzungsdatei wird regelmäßig verbessert. Neue Star Citizen Patches fügen oft neue Texte hinzu. Lade die ZIP-Datei regelmäßig herunter, um Fehler zu vermeiden. Oder nutze unseren Launcher der die Aufgabe für dich erledigt.**

> [!WARNING]
> **Hast du eine eigene user.cfg Datei? Überschreibe sie nicht! Füge einfach diese zwei Zeilen hinzu:** <br/>
> ```
> g_language = german_(germany)
> g_languageAudio = english
> ```

---

<br>

## INI-Injections
INI-Injection ist ein Modul, das die `global.ini` mit hilfreichen Features erweitert. Zu den aktuellen Funktionen gehören:
- Baupläne
- Komponenten-Strings
- Waffen-Strings

Nähere Informationen zu den einzelnen Features findest du nachfolgend.

<br>

### Baupläne-Missionsintegration

Star Citizen vergibt bei bestimmten Missionen Baupläne (Blueprints) als Belohnung. Welche Baupläne vergeben werden, hängt vom Blueprint-Pool, der Reputationsstufe und der jeweiligen Region ab. Neben der englischsprachigen Community gibt es nun auch unsere deutsche Lösung, die Baupläne direkt in die Missionstexte integriert.

### Installation der Baupläne für Missionstexte (InGame)
Über unseren **SC Deutsch Launcher** kannst du den aktuellen Stand der Baupläne bequem direkt in die Übersetzungsdatei **(`global.ini`)** integrieren.

1. Öffne den SC Deutsch Launcher und aktualisiere die Übersetzung.
2. Klicke im Hauptfenster auf das **Injections-Icon** <img width="27" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/injections_icon.png?1" /> in der Titelleiste.
3. Das Modul "Injections für global.ini" öffnet sich.
4. Klicke auf den **"Baupläne injizieren"**-Button – fertig.

**Features der InGame-Integration:**
- Missionen mit Bauplänen werden direkt im Titel mit einem `[BP]` oder `[BP]*` markiert.
- Anzeige der minimalen und maximalen Reputationsanforderungen (XP) auf einen Blick.
- Regionsgebundene Missionen werden klar gekennzeichnet.
- Verfügbarkeit der Baupläne anhand des aUEC-Missions-Payouts.
- In welcher Region dieser Bauplan gilt mit Gefahrenangabe.
- Cooldown-Zeit wann eine Mission erneut angenommen werden kann.

<br>

#### Baupläne-Datenbank (Web-Tool)
Die Baupläne DB ist ein nützliches Tracking-Tool für Star Citizen, mit dem du deinen Fortschritt beim Sammeln von Bauplänen organisieren und im Blick behalten kannst.
- **Fortschritt tracken:** Markiere einzelne Baupläne ganz einfach als "Erledigt" oder "Vorgemerkt".
- **Suchen & Filtern:** Finde gezielt Baupläne anhand von Missionstiteln, Orten oder ganzen Sonnensystemen.
- **Zur Baupläne-Datenbank:** [https://rjcncpt.github.io/StarCitizen-Deutsch-INI/](https://rjcncpt.github.io/StarCitizen-Deutsch-INI/)

<br>

### Waffen- und Komponenten-Strings
Für dieses Feature verwenden wir die Daten von [MrKraken's StarStrings](https://github.com/MrKraken/StarStrings). Da der SCDL erspielte Baupläne anhand der in den Logdateien enthaltenen Itemnamen erkennt, passen wir die Darstellung der erweiterten Strings von MrKraken entsprechend an.

StarStrings ergänzt Itemnamen standardmäßig nach folgendem Muster:

```text
Civ/2/C Frost-Star EX
[EM1] Pioneer-G
```

<br>

Für die Bauplan-Erkennung muss der SCDL diese Einträge jedoch in ein einheitliches Format überführen:

```text
Frost-Star EX (Civ/2/C)
Pioneer-G (EM1)
```

<br>

Werden die String-Optionen im Spiel verwendet, erscheinen die Zusatzinformationen sowohl in der Benutzeroberfläche als auch in den erzeugten Logdateien. Beim Auslesen der Logs entfernt der SCDL diese Zusätze anschließend wieder und normalisiert die Namen auf das ursprüngliche Format:

```text
Frost-Star EX
Pioneer-G
```

<br>

Dadurch können die Einträge zuverlässig erkannt und den entsprechenden Bauplänen korrekt zugeordnet werden.

---

<br><br>

## Wie aktuell ist die deutsche Übersetzung?
Die deutsche Übersetzung ist tagesaktuell. Die LIVE-Übersetzung wird unmittelbar zur LIVE-Schaltung bereitgestellt und bis zum nächsten Patch mehrmals aktualisiert. Sollten im Spiel Variablen mit einem `@-Zeichen` angezeigt werden, liegt der Fehler meist bei CIG und wird in späteren Patches korrigiert.

💡 **Es kommt häufig vor, dass eine neue Spielversion veröffentlicht wird aber kein Update auf Github hochgeladen wurde. In diesem Fall gab es keine Veränderungen an den Spieltexten und demzufolge kann sich die Versionsnummer hier auf Github mit der Spielversion unterscheiden.**

---

<br><br>

## Fragen und Antworten

<details>
<summary>[Klick] Fehler: Das Spiel ist noch komplett auf Englisch</summary>
Häufig ist die Ursache hierfür ein doppelter StarCitizen-Ordner auf dem System (z. B. `...\LIVE\StarCitizen\LIVE`). Markiere alle Dateien im doppelten Ordner, schneide sie aus, füge sie eine Ebene darüber ein und lösche den doppelten Ordner. Verifiziere anschließend die Spieldateien über den RSI Launcher (`VERIFY GAME`).
</details>

<details>
<summary>[Klick] Fehler: Das Bild wird plötzlich rot eingefärbt</summary>
Dieser Fehler konnte auf eine fehlerhafte `user.cfg` Datei zurückgeführt werden, die z.B. Shader oder Schatten beeinflusst. Lösche entweder alle Einstellungen in deiner Datei bis auf die Sprachbefehle oder ändere deine benutzerdefinierten Einstellungen.
</details>

<details>
<summary>[Klick] Fehler: Es werden kryptische Variablen mit @-Zeichen angezeigt</summary>
Wenn bei dir Variablen angezeigt werden, die mit einem @-Zeichen beginnen, ist entweder deine Datei-Codierung falsch oder du hast die `user.cfg` Datei vergessen. Öffne die `global.ini` mit Notepad++ und ändere die Codierung auf **`UTF-8-BOM`**.
</details>

---

<br><br>

## Urheberrecht
**Das gesamte GitHub-Repository unterliegen der freien [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) Lizenz.**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_NC_SA_4.0-lightgrey.svg?style=for-the-badge)]([https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/))

[![Made by the Community](https://i.imgur.com/2RWyGPJ.png)](#)
