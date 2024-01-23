import re

def read_ini_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
        return None
    except UnicodeDecodeError:
        print(f"Fehler beim Dekodieren der Datei {file_path}. Überprüfen Sie die Zeichenkodierung.")
        return None

def check_and_print_lines(file_lines):
    if file_lines:
        for line_number, line in enumerate(file_lines, start=1):
            # Überprüfe, ob ein Leerzeichen vor dem Komma steht
            if ' ,' in line:
                print(line_number, end=', ')

if __name__ == "__main__":
    # Passe den Dateipfad und die Zeichenkodierung entsprechend an
    ini_file_path = "global.ini"
    file_encoding = "utf-8"  # Ändere dies entsprechend der tatsächlichen Zeichenkodierung

    lines = read_ini_file(ini_file_path, encoding=file_encoding)

    if lines:
        check_and_print_lines(lines)
