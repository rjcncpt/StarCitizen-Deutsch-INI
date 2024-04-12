# Symbolic Link vom LIVE Ordner erstellen

Der ständige Download von vielen Gigabyte Daten, wenn man zwischen LIVE und PTU wechselt, ist unnötig. Erstelle mit einem winzigen Tool eine symbolische Verknüpfung des LIVE Verzeichnisses und spare dir Zeit. Ein "Symbolic Link" ist nichts anderes als eine Verknüpfung, funktioniert jedoch anders.

![image](https://i.imgur.com/HrASh6V.png)

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

<br/><br/>
### Wichtiger Hinweis

Wenn du die Reihenfolge im Tool vertauschst, löschst du den LIVE Ordner. Also achte auf Quell- und Zielverzeichnis. Orientiere dich an meinem Screenshot.
