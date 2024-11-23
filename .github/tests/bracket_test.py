import re

# Definition der auszuschließenden Präfixe
excluded_prefixes = {
    "live": [
        "test_prefix=",
        "ignore_this=",
        "skip_line=",
    ],
    "ptu": [
        "exclude_this=",
        "ptu_ignore=",
    ]
}


def check_brackets(filename, excluded_prefixes):
    """
    :param filename: Der Name der Datei, die auf Klammerpaare überprüft wird.
    :param excluded_prefixes: Liste von Präfixen, deren Zeilen übersprungen werden.
    :return: None

    Überprüft die Datei auf korrektes Klammerpaar-Matching, ignoriert Zeilen, die mit bestimmten Präfixen beginnen.
    """
    with open(filename, 'r', encoding="UTF-8-SIG") as file:
        for line_number, line in enumerate(file, start=1):
            # Überspringe Zeilen mit ausgeschlossenen Präfixen
            if any(line.startswith(prefix) for prefix in excluded_prefixes):
                continue

            # Bereinige die Zeile von unerwünschten Teilen
            clean_line = re.sub(r'\d\.\)|\s[a-z]\)|:\)', '', line)  # Entferne "1.)", "a)", ":)" Teile.

            bracket_stack = []
            for char in clean_line:
                if char == '(':
                    bracket_stack.append(char)
                elif char == ')':
                    try:
                        bracket_stack.pop()
                    except IndexError:
                        print(f"Zeile {line_number}: Zusätzliche schließende Klammer gefunden.")
                        break

            if bracket_stack:
                print(f"Zeile {line_number}: Offene Klammer wurde nicht geschlossen.")


if __name__ == "__main__":
    # Dateien für live und ptu
    deu_live_file = "live/global.ini"
    deu_ptu_file = "ptu/global.ini"

    print()
    print(f"Prüfe {deu_live_file}...")
    check_brackets(deu_live_file, excluded_prefixes["live"])
    print()
    print(f"Prüfe {deu_ptu_file}...")
    check_brackets(deu_ptu_file, excluded_prefixes["ptu"])
