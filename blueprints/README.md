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
Star Citizen vergibt bei bestimmten Missionen Baupläne (Blueprints) als Belohnung. Welche Baupläne vergeben werden, hängt von der Missionsbeschreibung, dem sogenannten **Blueprint Pool**, sowie von Reputationsstufe und Region ab. Diese Informationen sind in den Spieldaten vorhanden, werden dem Spieler aber standardmäßig nicht angezeigt.

Unsere Integration liest diese Daten direkt aus der **([scmdb.net](https://scmdb.net))**-Spieldatenbank aus und fügt sie als lesbaren Text in die Missionsbeschreibung ein. So sieht man bereits vor Annahme einer Mission, welche Baupläne möglich sind.

Das Ergebnis sieht im Spiel z. B. so aus:

```
---------------------------------------------------------

<EM4>MÖGLICHE BAUPLÄNE FÜR DIESEN AUFTRAGSTYP</EM4>

# Min. Reputation: Auftragnehmer Junior
# Max. Reputation: Auftragnehmer Elite

# Region: Pyro, Region B (Bloom) - Gefahr 4/10

- Atzkav Sniper Rifle
- Atzkav "Igniter" Sniper Rifle
- Atzkav "Mirage" Sniper Rifle
- Calico Arms Tactical
- Calico Core Tactical
- Calico Legs Tactical
- Calico Helmet Tactical
- Atzkav Sniper Rifle Battery (8 Schuss)

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
### Baupläne direkt in der Missionsbeschreibung
<img width="1159" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/mission_details_01.png?1" />
Missionen mit Bauplänen werden in der Missionsliste direkt mit einem blauen [BP] markiert. Öffnest du eine solche Mission, findest du gleich zu Beginn der Beschreibung einen Hinweis darauf. Scrollst du weiter nach unten, werden dir die möglichen Baupläne für diesen Auftragstyp angezeigt.
<br><br>

### Hinweistext bei unvorhersehbaren Missionen
<img width="1159" alt="image" src="https://www.sc-deutsch-launcher.de/img/features/blueprints/mission_details_02.png?1" />
Manche Missionstypen werden vom Spiel dynamisch generiert. Die Bauplan-Vergabe ist dabei nicht eindeutig vorhersagbar. Statt falscher Sicherheit bekommst du einen klaren Hinweis in blau, dass die Ergebnisse variieren können. Diese Missionstypen geben je nach Reputation, Region und interner Spiellogik verschiedene Blueprint-Pools die nicht genau vorhersagbar sind.
<br><br>

### Reputationsanforderungen auf einen Blick
Manche Baupläne sind nur bei einer bestimmten Reputationsstufe verfügbar. Die Beschreibung zeigt dir die minimale und maximale Reputation, die du für den jeweiligen Bauplan benötigst. So weißt du sofort, ob sich die Mission für deinen aktuellen Fortschritt lohnt.
<br><br>

### Regionsgebundene Missionen klar gekennzeichnet
Wenn eine Mission nur in einer bestimmten Region des Spiels verfügbar ist, wird dir genau das angezeigt. Du siehst auf Anhieb, in welchem Gebiet du die Mission finden kannst.
<br><br>

### Manuelle Korrekturen (CIG-Bug-Patches)
Bekannte Fehler in den Spielrohdaten (falsche `descriptionKey`- oder `titleKey`-Zuweisungen) wurden automatisch durch ein internes Override-System korrigiert.
<br><br>

### Immer aktuell
Die Daten werden bei jedem Update direkt aus der aktuellen Spielversion gezogen. Sobald CIG neue Missionen oder Baupläne hinzufügt, wird die Integration entsprechend aktualisiert.

<br><br><br>

## Was machen wir anders?
Die englische Community war Vorreiter bei der Integration von Bauplänen in Missionstexte. Das Problem bisheriger Lösungen ist, dass wenn es mehrere Baupläne für den gleichen Missionstypen gibt, diese nicht dargestellt wurden. Baupläne werden je nach Region, Reputation und interner Spiellogik ausgeliefert.

Da alle Missionstexte in einer statischen Datei liegen, stellen wir alle verfügbaren Baupläne für den jeweiligen Missionstyp – abhängig von Reputation und/oder Region – gesammelt dar. Dadurch kann es vorkommen, dass in einzelnen Missionstexten zwei oder mehr Blueprint-Pools angezeigt werden. Zwei Beispiele dazu folgen weiter unten.

Wir als deutsches Team haben die bisherige englische Umsetzung um einige weitere Aspekte ergänzt:
- Ein dezenter Hinweis **`Baupläne enthalten`** an erster Position in Missionstexten die Baupläne enthalten
- Angaben der minimalen und maximalen Reputaion die für den Bauplan erforderlich ist
- Angaben zur Region mit Gefahrenlage: **`Pyro, Region B (Bloom) - Gefahr 4/10`**
- Unterstützung für mehrere Baupläne je Missionstyp (abhängig von Region, Reputation oder Spiellogik)


### Beispiele unterschiedlicher Bauplan-Auflistungen
#### Einzel-Bauplan
```
---------------------------------------------------------

<EM4>MÖGLICHE BAUPLÄNE FÜR DIESEN AUFTRAGSTYP</EM4>

# Min. Reputation: Auftragnehmer Junior
# Max. Reputation: Auftragnehmer Elite

# Region: Pyro, Region B (Bloom) - Gefahr 4/10

- Atzkav Sniper Rifle
- Atzkav "Igniter" Sniper Rifle
- Atzkav "Mirage" Sniper Rifle
- Calico Arms Tactical
- Calico Core Tactical
- Calico Legs Tactical
- Calico Helmet Tactical
- Atzkav Sniper Rifle Battery (8 Schuss)

Dieser Service ist experimentell. Die Daten können Fehlerhaft sein.
```
#### Multi-Baupläne
```
---------------------------------------------------------

<EM4>Dieser Missionstyp wird vom Spiel dynamisch erzeugt.
Die Vergabe der Baupläne ist nicht eindeutig vorhersagbar und
wird je nach Region, Reputation oder interner Spiellogik ausgeben.

Bitte mit Datenbanken wie star-head.de oder scmdb.net vergleichen.</EM4>


MÖGLICHE BAUPLÄNE FÜR DIESEN AUFTRAGSTYP

# Region: Nyx System - Gefahr 3-6/10

# Min. Reputation: Auftragnehmer Junior

- R97 "Kismet" Shotgun
- R97 "Righteous" Shotgun
- Monde Arms Delta Camo
- Monde Legs Delta Camo
- Monde Core Delta Camo
- R97 Shotgun Magazine (18 Schuss)

---------------------------------------------------------

# Region: Nyx System - Gefahr 3-6/10

# Min. Reputation: Auftragnehmer Junior
# Max. Reputation: Auftragnehmer Elite

- Custodian SMG
- Custodian "Midnight" SMG
- Custodian "Scorched" SMG
- Arden-SL Arms
- Arden-SL Core
- Arden-SL Legs

---------------------------------------------------------

# Region: Stanton System - Gefahr 4-6/10
# Region: Stanton 1 (Hurston) - Gefahr 4/10
# Region: Stanton 2 (Crusader) - Gefahr 4/10
# Region: Stanton 3 (ArcCorp) - Gefahr 6/10
# Region: Stanton 4 (microTech) - Gefahr 5/10

# Max. Reputation: Auftragnehmer Elite

- Lumin V SMG
- Inquisitor Core Black
- Inquisitor Arms Black
- Inquisitor Legs Black
- Morningstar Helmet Icefall

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
