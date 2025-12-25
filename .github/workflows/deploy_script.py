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


def send_dicord_message(
    title: str,
    message: str,
    color: int = 3066993,
    footer_text: str = None,
    footer_url: str = None,
) -> bool:
    """Sendet eine Discord-Nachricht als Embed über einen Webhook.

    Args:
        title (str): Der Titel der Nachricht.
        message (str): Der Inhalt der Nachricht.
        color (int): Die Farbe des Embeds Bsp: 3066993 (grün), 15158332 (rot), 15844367 (gelb), 3447003 (blau), 10181046 (lila), 0 (schwarz)
        footer_text (str): Optionaler Footer-Text
        footer_url (str): Optionale URL für den Footer
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

    if footer_text and footer_url:
        embed["footer"] = {"text": f"{footer_text}\n{footer_url}"}
    elif footer_text:
        embed["footer"] = {"text": footer_text}

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


def get_commit_url() -> tuple[str, str]:
    """Erstellt die URL zum letzten Commit für live/global.ini.

    Returns:
        tuple[str, str]: (commit_url, short_hash) oder ("", "") bei Fehler
    """
    try:
        # Hole den Commit-Hash
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=%H", "live/global.ini"],
            capture_output=True,
            text=True,
            check=True,
        )
        commit_hash = result.stdout.strip()
        short_hash = commit_hash[:7]  # Kurze Version für Anzeige

        # Hole die Remote-URL
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            capture_output=True,
            text=True,
            check=True,
        )
        remote_url = result.stdout.strip()

        # Konvertiere SSH/HTTPS URL zu HTTPS Web-URL
        if remote_url.startswith("git@"):
            # git@github.com:user/repo.git -> https://github.com/user/repo
            remote_url = remote_url.replace(":", "/").replace("git@", "https://")

        # Entferne .git am Ende
        remote_url = remote_url.rstrip("/").removesuffix(".git")

        # Erstelle Commit-URL
        commit_url = f"{remote_url}/commit/{commit_hash}"
        return commit_url, short_hash
    except Exception as e:
        logger.error(f"Fehler beim Erstellen der Commit-URL: {e}")
        return "", ""


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
    commit_url, commit_hash = get_commit_url()

    message = f"Die Star Citizen Übersetzung wurde am {now.strftime('%d. %B %Y um %H:%M Uhr')} aktualisiert. Bitte aktualisiere deine Übersetzung für das bestmögliche Spielerlebnis.\n\n{patch_number}"

    if commit_url and commit_hash:
        message += f"\nAlle Änderungen zum Update: [{commit_hash}]({commit_url})"

    send_dicord_message(
        "Neue LIVE-Übersetzung verfügbar!",
        message,
        footer_text="An SCDL-Team spenden",
        footer_url="https://ko-fi.com/scdeutsch",
    )

    logger.info("\n=== Deployment abgeschlossen ===")


if __name__ == "__main__":
    main()
