# Scripts zum prüfen der richtigen Artikel für Vehikel
Dieses Python Script hilft dabei, die richtigen Artikel für Vehikel zu finden. In unserer Übersetzung sind Schiffe und Gravlev Vehikel weiblich und Fahrzeuge männlich. Eine Auflistung aller gefundenen Zeilen erfolgt nach dem Scan über eine HTML Datei.

### Anleitung
- Speichere die "Vehikelnamen finden.py" und "Vehikelnamen finden_prefixes.txt" ab.
- Starte das Python Script und suche nach der global.ini Datei.
- Die "Vehikelnamen finden_prefixes.txt" Datei beinhaltet bereits alle geprüften Zeilen die beim erneuten Scan nicht mehr berücksichtigt werden.
- Nach dem Scan wird eine "Vehikelnamen finden_global.html" Datei erstellt mit allen neuen Zeilen in denen Vehikelnamen vorkommen.
- Möchtest du neu beginnen, lösche die "Vehikelnamen finden_prefixes.txt" Datei.

### Hinweis
Die "Vehikelnamen finden_prefixes.txt" darf gern aktualisiert werden wenn jemand aus dem Team das Script zu einem späteren Zeitpunkt durchlaufen lässt.

### Python requirements
```pip install tqdm```

Erstellt von rjcncpt | [Deutsche Star Citizen Übersetzung](https://github.com/rjcncpt/StarCitizen-Deutsch-INI)
