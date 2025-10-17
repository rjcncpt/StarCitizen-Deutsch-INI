#!/usr/bin/env python3

import locale
import logging
import os
import re
import subprocess
import sys
import time
from datetime import datetime

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def execute_create_files():
    """Führt das Kommando aus dem CREATE_FILES Secret aus."""
    logger.info("Ausführen des CREATE_FILES Kommandos...")

    create_files_cmd = os.getenv("CREATE_FILES")
    if not create_files_cmd:
        logger.error("CREATE_FILES fehlt in den Umgebungsvariablen")
        sys.exit(1)

    try:
        response = requests.get(create_files_cmd, timeout=30)
        if response.status_code == 200:
            logger.info("CREATE_FILES Kommando erfolgreich ausgeführt.")
            return True
        else:
            logger.error(
                f"Fehler beim Ausführen von CREATE_FILES: {response.status_code}"
            )
            return False
    except Exception as e:
        logger.error(f"Exception beim Ausführen von CREATE_FILES: {e}")
        return False


def reload_website(retry_count=3):
    """Funktion, um die Webseite neu zu laden."""
    logger.info("Webseite wird neu geladen...")

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


def send_dicord_message(title: str, message: str, color: int = 3066993) -> bool:
    """Sendet eine Discord-Nachricht als Embed über einen Webhook.

    Args:
        title (str): Der Titel der Nachricht.
        message (str): Der Inhalt der Nachricht.
        color (int): Die Farbe des Embeds Bsp: 3066993 (grün), 15158332 (rot), 15844367 (gelb), 3447003 (blau), 10181046 (lila), 0 (schwarz)
    Returns:
        bool: True wenn die Nachricht erfolgreich gesendet wurde, sonst False.
    """
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        logger.error("DISCORD_WEBHOOK_URL fehlt in den Umgebungsvariablen")
        return False

    embed = {
        "title": title,
        "description": message,
        "color": color,
    }
    payload = {"embeds": [embed]}

    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        if response.status_code == 204:
            logger.info("Discord-Nachricht erfolgreich gesendet.")
            return True
        else:
            logger.error(
                f"Fehler beim Senden der Discord-Nachricht: {response.status_code} {response.text}"
            )
            return False
    except Exception as e:
        logger.error(f"Exception beim Senden der Discord-Nachricht: {e}")
        return False


def get_patch_number() -> str:
    """Parst den commit titel um die Patch-Nummer zu extrahieren."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=%s", "live/global.ini"],
            capture_output=True,
            text=True,
            check=True,
        )
        commit_title = result.stdout.strip()
        if "|" not in commit_title:
            return ""
        clean_title = re.sub(r"\s*\([^)]*\)\s*$", "", commit_title).strip()
        return clean_title
    except Exception as e:
        logger.error(f"Fehler beim Abrufen der Patch-Nummer: {e}")
        return ""


def main():
    """Hauptfunktion des Deployment-Scripts."""
    logger.info("=== Deployment Script gestartet ===")

    # Schritt 1: CREATE_FILES ausführen
    logger.info("\n--- Schritt 1: CREATE_FILES ausführen ---")
    if not execute_create_files():
        logger.error("CREATE_FILES konnte nicht ausgeführt werden")
        sys.exit(1)

    # Schritt 2: Website-Aktualisierung
    logger.info("\n--- Schritt 2: Website-Aktualisierung ---")
    if not reload_website():
        logger.warning("Website-Aktualisierung fehlgeschlagen")

    # Schritt 3: Warte 5 Sekunden
    logger.info("\n--- Schritt 3: Warte 5 Sekunden ---")
    time.sleep(5)

    # Schritt 4: Sende Discord-Nachricht
    logger.info("\n--- Schritt 4: Sende Discord-Nachricht ---")
    locale.setlocale(locale.LC_ALL, "de_DE.utf-8")
    now = datetime.now()
    patch_number = get_patch_number()

    message = f"Die Star Citizen Übersetzung wurde am {now.strftime('%d. %B %Y um %H:%M Uhr')} aktualisiert. Bitte aktualisiere deine Übersetzung für das bestmögliche Spielerlebnis.\n\n{patch_number}"
    send_dicord_message("Neue LIVE-Übersetzung verfügbar!", message)

    logger.info("\n=== Deployment abgeschlossen ===")


if __name__ == "__main__":
    main()
