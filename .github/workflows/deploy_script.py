#!/usr/bin/env python3

import logging
import os
import sys
import time
from ftplib import FTP

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def reload_website(retry_count=3):
    """Funktion, um die Webseite neu zu laden."""
    logger.info("Webseite wird neu geladen...")

    # Website-URL aus Umgebungsvariable
    website_url = os.getenv("WEBSITE_URL")
    if not website_url:
        logger.error("WEBSITE_URL fehlt in den Umgebungsvariablen")
        return False

    for attempt in range(retry_count):
        try:
            response = requests.get(website_url, timeout=30)
            if response.status_code == 200:
                logger.info("Die Website wurde erfolgreich neu geladen.")
                return True
            else:
                logger.warning(
                    f"Website konnte nicht neu geladen werden. Status: {response.status_code}"
                )
        except Exception as e:
            logger.warning(
                f"Fehler beim Neuladen der Website (Versuch {attempt + 1}): {e}"
            )
            if attempt < retry_count - 1:
                time.sleep(5)  # Warte 5 Sekunden vor dem nächsten Versuch

    logger.error("Alle Versuche zum Neuladen der Website fehlgeschlagen")
    return False


def delete_files():
    """Löschen von Cache-Dateien auf dem FTP-Server."""
    logger.info("Löschen von Dateien auf dem FTP-Server...")

    # FTP-Credentials aus Umgebungsvariablen
    ftp_host = os.getenv("FTP_HOST")
    ftp_user = os.getenv("FTP_USER")
    ftp_pass = os.getenv("FTP_PASS")

    if not all([ftp_host, ftp_user, ftp_pass]):
        logger.error("FTP-Credentials fehlen in den Umgebungsvariablen")
        sys.exit(1)

    files_to_delete = [
        "/httpdocs/inc/cache/total_accesses.cache",
        "/httpdocs/inc/commit_info.txt",
    ]

    try:
        ftp = FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)
        logger.info("Verbindung zum FTP-Server hergestellt.")

        for file_path in files_to_delete:
            try:
                ftp.delete(file_path)
                logger.info(f"Datei gelöscht: {file_path}")
            except Exception as e:
                logger.error(f"Fehler beim Löschen der Datei '{file_path}': {e}")

        ftp.quit()
        logger.info("Die Verbindung zum FTP-Server wurde getrennt.")
        return True

    except Exception as e:
        logger.error(f"Verbindung zum FTP-Server fehlgeschlagen: {e}")
        return False


def main():
    """Hauptfunktion des Deployment-Scripts."""
    logger.info("=== Deployment Script gestartet ===")

    # Schritt 1: Cache-Dateien löschen
    logger.info("\n--- Schritt 1: Cache-Dateien löschen ---")
    if not delete_files():
        logger.error("Cache-Dateien konnten nicht gelöscht werden")
        sys.exit(1)

    # Schritt 2: Erste Website-Aktualisierung
    logger.info("\n--- Schritt 2: Erste Website-Aktualisierung ---")
    if not reload_website():
        logger.warning("Erste Website-Aktualisierung fehlgeschlagen")

    # Schritt 3: Warte 5 Sekunden
    logger.info("\n--- Warte 5 Sekunden ---")
    time.sleep(5)

    # Schritt 4: Zweite Website-Aktualisierung
    logger.info("\n--- Schritt 3: Zweite Website-Aktualisierung ---")
    if not reload_website():
        logger.warning("Zweite Website-Aktualisierung fehlgeschlagen")

    logger.info("\n=== Deployment abgeschlossen ===")


if __name__ == "__main__":
    main()
