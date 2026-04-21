# Baupläne-Missionsintegration
Neben der englischsprachigen Community gibt es nun auch unsere deutsche Lösung, Baupläne den Missionen hinzuzufügen. Über unseren **[SC Deutsch Launcher](https://www.sc-deutsch-launcher.de/download/)** kannst du den aktuellen Stand der Baupläne bequem direkt in die Übersetzungsdatei (`global.ini`) integrieren.

<img width="772" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/hauptmenue.png?1" />

---

### Inhaltsverzeichnis

- **[Wie funktionieren die Baupläne?](#wie-funktionieren-die-baupläne)**
- **[Installation der Baupläne](#installation)**
- **[Features](#features)**
- **[Was machen wir anders?](#was-machen-wir-anders)**

---

## Wie funktionieren die Baupläne?
Star Citizen vergibt bei bestimmten Missionen Baupläne (Blueprints) als Belohnung. Welche Baupläne vergeben werden, hängt von der Missionsbeschreibung, dem sogenannten **Blueprint Pool**, sowie von Reputationsstufe und Regionen ab. Diese Informationen sind in den Spieldaten vorhanden, werden dem Spieler aber standardmäßig nicht angezeigt.

Unsere Integration liest diese Daten direkt aus der **([scmdb.net](https://scmdb.net))**-Datenbank aus und fügt sie als lesbaren Text in die Missionsbeschreibung ein. In den Missionstitel wir ein `[BP]`-Kürzel hinzugefügt, so das man bereits vor Annahme einer Mission zieht, welche Mission Baupläne enthält.

Update: Wir haben das `[BP]`-Kürzel um ein Sternchen `[BP]*` erweitert, wenn zu einem Missionstitel mehrere Missionstexten existieren.

Das Ergebnis sieht im Spiel z. B. so aus:

```
---------------------------------------------------------

MÖGLICHE BAUPLÄNE FÜR DIESEN MISSIONSTYP

# Baupläne für die 43.750 / 54.500 / 81.250 aUEC Mission
# Min. / Max. Rep.: Auftragnehmer Senior (5.800 XP)

# Baupläne:
  - Arclight "Stormfall" Pistol
  - Arclight Pistol
  - Venture Arms
...

# Abgabe für 43.750 aUEC Mission:
  - Torite (min. 8 SCU)

# Abgabe für 54.500 aUEC Mission:
  - Agricium (min. 8 SCU) oder
  - Beryl (min. 7 SCU)

# Region: Nyx-System - Gefahr 3-6/10

Dieser Service ist experimentell. Die Daten können Fehlerhaft sein.
```

<br><br><br>

## Installation
<img width="780" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/blueprint-modul-aktivieren.png?1" />

### In wenigen Schritten zu Bauplänen in Missionstexten:
- Update (inGame) oder lade unseren **[SC Deutsch Launcher](https://www.sc-deutsch-launcher.de/download/)** herunter und installiere ihn
- Öffne den SC Deutsch Launcher und aktualisiere die Übersetzung
- Klicke im Hauptfenster auf das <img width="27" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/injections_icon.png?1" />-Icon in der Titelleiste
- Das Modul "Injections für global.ini" öffnet sich
- Klicke auf den **"Baupläne injizieren"**-Button – fertig

> [!TIP]
> > Möchtest du das Baupläne-Modul deaktivieren, kannst du dieses in den Einstellungen erledigen. Rufe dazu die Einstellungen auf, scrolle etwas herunter (unterhalb der SC-Pfade) und deaktiviere das Baupläne-Modul. Das Icon verschwindet in der Titelleiste.

> [!IMPORTANT]
> Überprüfe nach jedem neuen Star Citizen Patch, ob neue Baupläne verfügbar sind. Falls ja, wird dies durch einen orangenen Indikator-Punkt am Modul-Icon angezeigt.

### Indikator-Punkt
- Grüner Punkt: Baupläne sind aktuell
- Orangener Punkt: Baupläne haben ein Update
- Kein Punkt: Baupläne nicht installiert

<br><br><br>

## Features
### Baupläne direkt in den Missionstexten
<img width="1159" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/mission_details_01.png?1" />
Missionen mit Bauplänen werden in der Missionsliste direkt mit einem farbigen `[BP]` bzw `[BP]*` markiert. Scrollst du weiter nach unten, werden dir die möglichen Baupläne für diesen Auftragstyp angezeigt.

Besonderheit: Manche Missionen haben mehrere Missionstexte unter demselben Titel. In solchen Fällen wird `[BP]*`-Kürzel mit Sternchen verwendet. Zusätzlich erscheint am Anfang des Missionstextes ein Hinweis wie: `[!] Baupläne nur für 57.750 aUEC Mission enthalten`. So erkennst du eindeutig, welche Variante die Baupläne enthält.
<br><br>

### Hinweistext bei unvorhersehbaren Missionen
<img width="1159" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/mission_details_02.png?1" />
Manche Missionstypen werden vom Spiel dynamisch generiert. Die Bauplan-Vergabe ist dabei nicht eindeutig vorhersagbar. Statt falscher Sicherheit bekommst du einen klaren Hinweis in blau, dass die Ergebnisse variieren können. Diese Missionstypen geben je nach Reputation, Region und interner Spiellogik verschiedene Blueprint-Pools die nicht genau vorhersagbar sind.
<br><br>

### Reputationsanforderungen auf einen Blick
Manche Baupläne sind nur bei einer bestimmten Reputationsstufe verfügbar. Die Beschreibung zeigt dir die minimale und maximale Reputation mit den erforderlichen XP, die du für den jeweiligen Bauplan benötigst. So weißt du sofort, ob sich die Mission für deinen aktuellen Fortschritt lohnt.
<br><br>

### Regionsgebundene Missionen klar gekennzeichnet
Wenn eine Mission nur in einer bestimmten Region des Spiels verfügbar ist, wird dir genau das angezeigt. Du siehst auf Anhieb, in welchem Gebiet du die Mission finden kannst.
<br><br>

### Manuelle Korrekturen (CIG-Bug-Patches)
Bekannte Fehler in den Spielrohdaten (falsche `descriptionKey`- oder `titleKey`-Zuweisungen) wurden automatisch durch ein internes Override-System korrigiert.
<br><br>

### Immer aktuell
Die Daten werden bei jedem Update direkt aus der aktuellen Spielversion gezogen. Sobald CIG neue Missionen oder Baupläne hinzufügt, wird die Integration entsprechend aktualisiert.

Die Bauplandaten werden zur Zeit aus der **([scmdb.net](https://scmdb.net))**-Datenbank extrahiert. Vielen Dank für deine hervorragende Arbeit!

<br><br><br>

## Was machen wir anders?
Die englische Community war Vorreiter bei der Integration von Bauplänen in Missionstexte. Das Problem bisheriger Lösungen ist, dass wenn es mehrere Baupläne für den gleichen Missionstypen gibt, diese nicht dargestellt wurden. Baupläne werden je nach Region, Reputation und interner Spiellogik ausgeliefert.

Da alle Missionstexte in einer statischen Datei liegen, stellen wir alle verfügbaren Baupläne für den jeweiligen Missionstyp – abhängig von Reputation (XP) und/oder Region – gesammelt dar. Dadurch kann es vorkommen, dass in einzelnen Missionstexten zwei oder mehr Blueprint-Pools angezeigt werden. Zwei Beispiele dazu folgen weiter unten.

Wir als deutsches Team haben die bisherige englische Umsetzung um einige weitere Aspekte ergänzt:
- Ein dezenter Hinweis **`Baupläne enthalten`** an erster Position in Missionstexten die Baupläne enthalten
- Selektierung durch aUEC Angaben für welche Mission(en) die BP-Pools gültig sind
- Selektierung durch minimalen und maximalen Reputaion mit benötigten XP, die für den Bauplan erforderlich sind
- Selektierung durch Regionen mit Gefahrenlage: **`Pyro, Region B (Bloom) - Gefahr 4/10`**
- Unterstützung für mehrere Baupläne je Missionstyp (abhängig von Region, Reputation oder Spiellogik)


### Beispiele unterschiedlicher Bauplan-Auflistungen
#### Einzel-Bauplan
```
Lima Endicott
Leitende Einsatzkoordinatorin
Citizens for Prosperity
---------------------------------------------------------

MÖGLICHE BAUPLÄNE FÜR DIESEN MISSIONSTYP

# Baupläne für die 43.750 / 54.500 / 81.250 aUEC Mission
# Min. / Max. Rep.: Auftragnehmer Senior (5.800 XP)

# Baupläne:
  - Arclight "Stormfall" Pistol
  - Arclight Pistol
  - Venture Arms
...

# Abgabe für 43.750 aUEC Mission:
  - Torite (min. 8 SCU)

# Abgabe für 54.500 aUEC Mission:
  - Agricium (min. 8 SCU) oder
  - Beryl (min. 7 SCU)

# Region: Nyx-System - Gefahr 3-6/10

Dieser Service ist experimentell. Die Daten können Fehlerhaft sein.
```
#### Multi-Baupläne
```
Lima Endicott
Leitende Einsatzkoordinatorin
Citizens for Prosperity

---------------------------------------------------------
Dieser Missionstyp wird vom Spiel dynamisch erzeugt.
Die Vergabe der Baupläne ist nicht eindeutig vorhersagbar und
wird je nach Region, Reputation oder interner Spiellogik ausgeben.
Vergleiche mit Datenbanken wie star-head.de oder scmdb.net.
---------------------------------------------------------

MÖGLICHE BAUPLÄNE FÜR DIESEN MISSIONSTYP

# Baupläne für 400.250 aUEC Mission

# Min. Rep.: Auftragnehmer Senior (5.800 XP)
# Max. Rep.: Auftragnehmer Elite (95.250 XP)

# Baupläne:
  - Prism "Deep Sea" Laser Shotgun
  - Prism "Bonedust" Laser Shotgun
  - Prism "Firesteel" Laser Shotgun
...

# Abgabe:
  - Irradiated Valakkar Pearl (Grade AAA) (min. 1x) oder
  - Irradiated Valakkar Pearl (Grade AA) (min. 10x)

---------------------------------------------------------

# Baupläne für 113.750 aUEC Mission

# Min. Rep.: Auftragnehmer Senior (5.800 XP)
# Max. Rep.: Auftragnehmer Elite (95.250 XP)

# Baupläne:
  - P8-AR Rifle
  - Palatino Arms
  - Palatino Core
  - Palatino Legs
...

# Abgabe:
  - Yormandi Eye (min. 4x)

Dieser Service ist experimentell. Daten können Fehlerhaft sein.
```
Die Baupläne sind in der [bp-contracts_short.json](https://github.com/rjcncpt/StarCitizen-Deutsch-INI/blob/main/blueprints/Data/bp-contracts_short.json) Datei gespeichert.


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
