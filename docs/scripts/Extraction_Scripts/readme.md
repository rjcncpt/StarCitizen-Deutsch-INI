# Scripts zum extrahieren der global.ini Dateien
Dieses Script extrahiert die global.ini Dateien aus den entsprechenden SC Installationen. Die Aufgaben der scripts umfassen:

### Allgemeine Aufgaben
- Auswahl der Umgebung
- Die Buildnummer der ini Datei wird aus der `build_manifest.id` extrahiert.
- UTF-8 Fehler werden korrigiert.
- Offensichtlich fehlerhafte Präfixe werden korrigiert.

### Benutzerdefinierte Aufgaben
- Aus einigen Zeilen wird das erste `~mission(Location|Address)` entfernt da wir diese in unserer Übersetzung nicht benötigen.
- Es wird nach der Zeile `Frontend_PU_Version,P=` bzw. `Frontend_PU_Version=` gesucht und diese an erste Position verschoben.

### Zu beachten
- Die Dateien im unp4k Verzeichnis ablegen
- Die Pfade für `exe_path`, `argument_data, build_manifest_path` und ggf. für `output_file_path` anpassen.