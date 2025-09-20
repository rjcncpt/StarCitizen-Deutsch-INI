#!/usr/bin/env python3

import os
import sys
import time
from ftplib import FTP

import requests


def log_message(message):
    """Log-Nachricht ausgeben."""
    print(f"[LOG] {message}")


def reload_website(retry_count=3):
    """Funktion, um die Webseite neu zu laden."""
    log_message("Webseite wird neu geladen...")

    # Website-URL aus Umgebungsvariable
    website_url = os.getenv("WEBSITE_URL")
    if not website_url:
        log_message("FEHLER: WEBSITE_URL fehlt in den Umgebungsvariablen")
        return False

    for attempt in range(retry_count):
        try:
            response = requests.get(website_url, timeout=30)
            if response.status_code == 200:
                log_message("Die Website wurde erfolgreich neu geladen.")
                return True
            else:
                log_message(
                    f"Website konnte nicht neu geladen werden. Status: {response.status_code}"
                )
        except Exception as e:
            log_message(
                f"Fehler beim Neuladen der Website (Versuch {attempt + 1}): {e}"
            )
            if attempt < retry_count - 1:
                time.sleep(5)  # Warte 5 Sekunden vor dem nächsten Versuch

    log_message("Alle Versuche zum Neuladen der Website fehlgeschlagen")
    return False


def delete_files():
    """Löschen von Cache-Dateien auf dem FTP-Server."""
    log_message("Löschen von Dateien auf dem FTP-Server...")

    # FTP-Credentials aus Umgebungsvariablen
    ftp_host = os.getenv("FTP_HOST")
    ftp_user = os.getenv("FTP_USER")
    ftp_pass = os.getenv("FTP_PASS")

    if not all([ftp_host, ftp_user, ftp_pass]):
        log_message("FEHLER: FTP-Credentials fehlen in den Umgebungsvariablen")
        sys.exit(1)

    files_to_delete = [
        "/httpdocs/inc/cache/total_accesses.cache",
        "/httpdocs/inc/commit_info.txt",
    ]

    try:
        ftp = FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)
        log_message("Verbindung zum FTP-Server hergestellt.")

        for file_path in files_to_delete:
            try:
                ftp.delete(file_path)
                log_message(f"Datei gelöscht: {file_path}")
            except Exception as e:
                log_message(f"Fehler beim Löschen der Datei '{file_path}': {e}")

        ftp.quit()
        log_message("Die Verbindung zum FTP-Server wurde getrennt.")
        return True

    except Exception as e:
        log_message(f"Verbindung zum FTP-Server fehlgeschlagen: {e}")
        return False


def main():
    """Hauptfunktion des Deployment-Scripts."""
    log_message("=== Deployment Script gestartet ===")

    # Schritt 1: Cache-Dateien löschen
    log_message("\n--- Schritt 1: Cache-Dateien löschen ---")
    if not delete_files():
        log_message("FEHLER: Cache-Dateien konnten nicht gelöscht werden")
        sys.exit(1)

    # Schritt 2: Erste Website-Aktualisierung
    log_message("\n--- Schritt 2: Erste Website-Aktualisierung ---")
    if not reload_website():
        log_message("WARNUNG: Erste Website-Aktualisierung fehlgeschlagen")

    # Schritt 3: Warte 5 Sekunden
    log_message("\n--- Warte 5 Sekunden ---")
    time.sleep(5)

    # Schritt 4: Zweite Website-Aktualisierung
    log_message("\n--- Schritt 3: Zweite Website-Aktualisierung ---")
    if not reload_website():
        log_message("WARNUNG: Zweite Website-Aktualisierung fehlgeschlagen")

    log_message("\n=== Deployment abgeschlossen ===")


if __name__ == "__main__":
    main()
