# Baupläne-Missionsintegration
Neben der englischsprachigen Community gibt es nun auch unsere deutsche Lösung, Baupläne den Missionen hinzuzufügen. Über unseren **[SC Deutsch Launcher](https://www.sc-deutsch-launcher.de/download/)** kannst du den aktuellen Stand der Baupläne bequem direkt in die Übersetzungsdatei (`global.ini`) integrieren.

<img width="772" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/hauptmenue.png?1" />

---

### Inhaltsverzeichnis

- **[Wie funktionieren die Baupläne?](#wie-funktionieren-die-baupläne)**
- **[Installation der Baupläne](#installation)**
- **[Features](#features)**

---

## Wie funktionieren die Baupläne?
Star Citizen vergibt bei bestimmten Missionen Baupläne (Blueprints) als Belohnung. Welche Baupläne vergeben werden, hängt von der Missionsbeschreibung, dem sogenannten **Blueprint Pool**, sowie von Reputationsstufe und Region ab. Diese Informationen sind in den Spieldaten vorhanden, werden dem Spieler aber standardmäßig nicht angezeigt.

Unsere Integration liest diese Daten direkt aus der **([scmdb.net](https://scmdb.net))**-Spieldatenbank aus und fügt sie als lesbaren Text in die Missionsbeschreibung ein. So sieht man bereits vor Annahme einer Mission, welche Baupläne möglich sind.

Das Ergebnis sieht im Spiel z. B. so aus:

```
─────────────────────────────────────────────────────
MÖGLICHE BAUPLÄNE FÜR DIESEN AUFTRAGSTYP

# Min. Reputation: Vertraut
# Max. Reputation: Berühmt

# Region: Stanton 1

- S1 FixedGun Laser Repeater (10 Schuss)
- S2 FixedGun Laser Cannon (5 Schuss)

Dieser Service ist experimentell. Die Daten können Fehlerhaft sein.
```

<br><br><br>

## Installation
<img width="780" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/blueprint-modul-aktivieren.png?1" />

### In wenigen Schritten zu Bauplänen in Missionstexten:
- Update (inGame) oder lade unseren **[SC Deutsch Launcher](https://www.sc-deutsch-launcher.de/download/)** und installiere ihn.
- Öffne den SC Deutsch Launcher und aktualisiere die Übersetzung
- Gehe in die Einstellungen, scrolle etwas nach unten unterhalb der SC-Pfade und aktiviere das Baupläne-Modul
- Auf der Hauptseite erscheint ein neues Icon <img width="27" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/injections_icon.png?1" /> in der Titelleiste
- Klicke darauf, um das Modul "Injections für global.ini" zu öffnen
- Klicke auf den **"Baupläne injizieren"**-Button – fertig

#### Überprüfe nach jedem neuen Star Citizen Patch, ob neue Baupläne verfügbar sind. Falls ja, wird dies durch einen orangenen Indikator-Punkt am Modul-Icon angezeigt.
### Indikator-Punkt
- Grüner Punkt: Baupläne sind aktuell
- Orangener Punkt: Baupläne haben ein Update
- Kein Punkt: Baupläne nicht installiert

<br><br><br>

## Features
### Baupläne direkt in der Missionsbeschreibung
<img width="1159" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/mission_details_01.png?1" />
Missionen mit Bauplänen werden in der Missionsliste direkt mit einem blauen [BP] markiert. Öffnest du eine solche Mission, findest du gleich zu Beginn der Beschreibung einen Hinweis darauf. Scrollst du weiter nach unten, werden dir die möglichen Baupläne für diesen Auftragstyp angezeigt.

### Hinweistext bei unvorhersehbaren Missionen
<img width="1159" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/mission_details_02.png?1" />
Manche Missionstypen werden vom Spiel dynamisch generiert. Die Bauplan-Vergabe ist dabei nicht eindeutig vorhersagbar. Statt falscher Sicherheit bekommst du einen klaren Hinweis in blau, dass die Ergebnisse variieren können. Diese Missionstypen geben je nach Reputation, Region und interner Spiellogik verschiedene Blueprint-Pools die nicht genau vorhersagbar sind.

### Reputationsanforderungen auf einen Blick
Manche Baupläne sind nur bei einer bestimmten Reputationsstufe verfügbar. Die Beschreibung zeigt dir die minimale und maximale Reputation, die du für den jeweiligen Bauplan benötigst. So weißt du sofort, ob sich die Mission für deinen aktuellen Fortschritt lohnt.

### Regionsgebundene Missionen klar gekennzeichnet
Wenn eine Mission nur in einer bestimmten Region des Spiels verfügbar ist, wird dir genau das angezeigt. Du siehst auf Anhieb, in welchem Gebiet du die Mission finden kannst.

### Manuelle Korrekturen (CIG-Bug-Patches)
Bekannte Fehler in den Spielrohdaten (falsche `descriptionKey`- oder `titleKey`-Zuweisungen) wurden automatisch durch ein internes Override-System korrigiert

### Immer aktuell
Die Daten werden bei jedem Update direkt aus der aktuellen Spielversion gezogen. Sobald CIG neue Missionen oder Baupläne hinzufügt, wird die Integration entsprechend aktualisiert.

<br><br><br>

## Hinweis
Dieser Service ist experimentell. Die Daten können Fehlerhaft sein. Bitte mit [star-head.de](https://star-head.de) oder [scmdb.net](https://scmdb.net) gegenchecken.

<br><br><br>

## Dateien im Überblick

| Datei | Beschreibung |
|:---|:---|
| `overrides_locality.txt` | Manuelle Regionsbezeichnungen |
| `Data/bp-contracts_short.json` | Ausgabe: Kompakte Blueprint-Contracts |
| `bp_titles_log.txt` | Ausgabe: Missionstitel-Log |
