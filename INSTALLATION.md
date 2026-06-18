### Inhaltsverzeichnis

- **[Anleitung zur Installation](#anleitung-zur-installation)**
- **[Baupläne-Missionsintegration & Datenbank](#ini-injections)**

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
Für dieses Feature werden die in den Spielressourcen enthaltenen String-Daten ausgewertet und aufbereitet. Da der SCDL erspielte Baupläne anhand der in den Logdateien enthaltenen Itemnamen erkennt, müssen bestimmte Präfixe und Kennzeichnungen aus den Rohdaten in ein einheitliches Format überführt werden.

Die String-Daten enthalten zusätzliche Informationen, die dem eigentlichen Itemnamen als Suffix angehängt werden:

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
