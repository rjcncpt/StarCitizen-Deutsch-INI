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

## Baupläne-Missionsintegration

Star Citizen vergibt bei bestimmten Missionen Baupläne (Blueprints) als Belohnung. Welche Baupläne vergeben werden, hängt vom Blueprint Pool, der Reputationsstufe und Regionen ab. Neben der englischsprachigen Community gibt es nun auch unsere deutsche Lösung, Baupläne den Missionen hinzuzufügen.

### 🛠️ Installation der Baupläne für Missionstexte (InGame)
Über unseren **SC Deutsch Launcher** kannst du den aktuellen Stand der Baupläne bequem direkt in die Übersetzungsdatei **(`global.ini`)** integrieren.

1. Öffne den SC Deutsch Launcher und aktualisiere die Übersetzung.
2. Klicke im Hauptfenster auf das **Injections-Icon** <img width="27" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/injections_icon.png?1" /> in der Titelleiste.
3. Das Modul "Injections für global.ini" öffnet sich.
4. Klicke auf den **"Baupläne injizieren"**-Button – fertig.

**Features der InGame-Integration:**
- Missionen mit Bauplänen werden direkt im Titel mit einem `[BP]` oder `[BP]*` markiert.
- Anzeige der minimalen und maximalen Reputationsanforderungen (XP) auf einen Blick.
- Regionsgebundene Missionen werden klar gekennzeichnet.
- Ein Indikator-Punkt am Modul-Icon im Launcher zeigt dir an, ob nach einem Star Citizen Patch neue Baupläne verfügbar sind.

### 📊 Baupläne-Datenbank (Web-Tool)
Die Baupläne DB ist ein übersichtliches Tracking-Tool für Star Citizen, mit dem du deinen Fortschritt beim Sammeln von Bauplänen organisieren und im Blick behalten kannst.
- **Fortschritt tracken:** Markiere einzelne Baupläne ganz einfach als "Erledigt" oder "Vorgemerkt".
- **Suchen & Filtern:** Finde gezielt Baupläne anhand von Missionstiteln, Orten oder ganzen Sonnensystemen.
- **Zur Baupläne-Datenbank:** [https://rjcncpt.github.io/StarCitizen-Deutsch-INI/](https://rjcncpt.github.io/StarCitizen-Deutsch-INI/)

💡 **Wir arbeiten an einer Möglichkeit, erledigte Baupläne in die Spieltexte zu integrieren. Daher kannst du auf der [Baupläne-Datenbankseite](https://rjcncpt.github.io/StarCitizen-Deutsch-INI/) erledigte Baupläne als `.json`-Datei exportieren. Aktuell prüfen wir eine Lösung, mit der der SCDL diese Datei einliest und deine Baupläne-Integration entsprechend anpasst.**
