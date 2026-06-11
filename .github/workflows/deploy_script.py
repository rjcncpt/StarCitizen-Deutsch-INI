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
                time.sleep(5)

    logger.error("Alle Versuche zum Neuladen der Website fehlgeschlagen")
    return False


def send_discord_message(
    title: str,
    message: str,
    color: int = 3066993,
    footer_text: str = None,
    footer_icon_url: str = None,
    content: str = None,
    webhook_url_override: str = None,
) -> bool:
    """Sendet eine Discord-Nachricht als Embed über einen Webhook.

    Args:
        title (str): Der Titel der Nachricht.
        message (str): Der Inhalt der Nachricht.
        color (int): Die Farbe des Embeds Bsp: 3066993 (grün), 15158332 (rot), 15844367 (gelb), 3447003 (blau), 10181046 (lila), 0 (schwarz)
        footer_text (str): Optionaler Footer-Text
        footer_icon_url (str): Optionale URL für das Footer Icon
        content (str): Optionaler Inhalt außerhalb des Embeds
        webhook_url_override (str): Optionale Webhook-URL, überschreibt DISCORD_WEBHOOK_URL aus den Umgebungsvariablen
    Returns:
        bool: True wenn die Nachricht erfolgreich gesendet wurde, sonst False.
    """
    webhook_url = webhook_url_override or os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        logger.error("DISCORD_WEBHOOK_URL fehlt in den Umgebungsvariablen")
        return False

    embed = {
        "title": title,
        "description": message,
        "color": color,
    }

    embed["footer"] = {}

    if footer_text:
        embed["footer"]["text"] = f"{footer_text}"

    if footer_icon_url:
        embed["footer"]["icon_url"] = f"{footer_icon_url}"

    payload = {"content": content, "embeds": [embed]}

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


def get_remote_url() -> str:
    """Gibt die HTTPS-Web-URL des Repositories zurück."""
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            capture_output=True,
            text=True,
            check=True,
        )
        remote_url = result.stdout.strip()
        if remote_url.startswith("git@"):
            remote_url = remote_url.replace(":", "/").replace("git@", "https://")
        return remote_url.rstrip("/").removesuffix(".git")
    except Exception as e:
        logger.error(f"Fehler beim Abrufen der Remote-URL: {e}")
        return ""


def get_commit_url() -> tuple[str, str]:
    """Erstellt die URL zum letzten Commit für live/global.ini.

    Returns:
        tuple[str, str]: (commit_url, short_hash) oder ("", "") bei Fehler
    """
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=%H", "live/global.ini"],
            capture_output=True,
            text=True,
            check=True,
        )
        commit_hash = result.stdout.strip()
        short_hash = commit_hash[:7]
        remote_url = get_remote_url()
        if not remote_url:
            return "", ""
        commit_url = f"{remote_url}/commit/{commit_hash}"
        return commit_url, short_hash
    except Exception as e:
        logger.error(f"Fehler beim Erstellen der Commit-URL: {e}")
        return "", ""


def get_todays_blueprint_commits() -> list[dict]:
    """Sammelt alle Commits des heutigen Tages für bp-contracts_short*.json.

    Returns:
        list[dict]: Liste von {hash, short_hash, message, url}
    """
    try:
        remote_url = get_remote_url()
        if not remote_url:
            return []

        # Heute 00:00:00 Berliner Zeit (TZ=Europe/Berlin ist gesetzt)
        today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        after_arg = today_start.strftime("%Y-%m-%d %H:%M:%S")

        result = subprocess.run(
            [
                "git", "log",
                f"--after={after_arg}",
                "--pretty=%H|%s",
                "--",
                "blueprints/Data/bp-contracts_short.json",
                "blueprints/Data/bp-contracts_short_en.json",
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        commits = []
        for line in result.stdout.strip().splitlines():
            if not line or "|" not in line:
                continue
            commit_hash, subject = line.split("|", 1)
            short_hash = commit_hash[:7]
            commit_url = f"{remote_url}/commit/{commit_hash}"
            commits.append({
                "hash": commit_hash,
                "short_hash": short_hash,
                "message": subject.strip(),
                "url": commit_url,
            })

        return commits

    except Exception as e:
        logger.error(f"Fehler beim Abrufen der Tages-Commits: {e}")
        return []


def send_blueprints_notification():
    """Sendet eine gebündelte Discord-Meldung für alle Blueprint-Updates des Tages."""
    logger.info("=== Blueprints Notification Script gestartet ===")

    webhook_url = os.getenv("DISCORD_WEBHOOK_URL_BP")
    if not webhook_url:
        logger.error("DISCORD_WEBHOOK_URL_BP fehlt in den Umgebungsvariablen")
        sys.exit(1)

    locale.setlocale(locale.LC_ALL, "de_DE.utf-8")
    now = datetime.now()

    commits = get_todays_blueprint_commits()

    if not commits:
        logger.info("Keine Blueprint-Commits heute – keine Discord-Meldung.")
        return

    logger.info(f"{len(commits)} Commit(s) heute gefunden.")

    if len(commits) == 1:
        commit_lines = (
            f"Änderungen zum Update: [#{commits[0]['short_hash']}]({commits[0]['url']})"
        )
    else:
        lines = "\n".join(
            f"• [#{c['short_hash']}]({c['url']}) {c['message']}" for c in commits
        )
        commit_lines = f"Alle Änderungen des Tages ({len(commits)} Updates):\n{lines}"

    message = (
        f"Die Baupläne wurden am "
        f"{now.strftime('%d. %B %Y')} aktualisiert. "
        f"Bitte aktualisiere deine Baupläne für das bestmögliche Spielerlebnis.\n\n"
        f"{commit_lines}"
        f"\n<:kofi:1319086302116708444> An SCDL-Team spenden: [ko-fi.com/scdeutsch](https://ko-fi.com/scdeutsch)"
    )

    send_discord_message(
        title="Baupläne aktualisiert!",
        message=message,
        color=3447003,  # blau
        webhook_url_override=webhook_url,
    )

    logger.info("=== Blueprints Notification abgeschlossen ===")


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

    message = (
        f"Die Star Citizen Übersetzung wurde am "
        f"{now.strftime('%d. %B %Y um %H:%M Uhr')} aktualisiert. "
        f"Bitte aktualisiere deine Übersetzung für das bestmögliche Spielerlebnis.\n\n"
        f"{patch_number}"
    )

    if commit_url and commit_hash:
        message += f"\n\nAlle Änderungen zum Update: [#{commit_hash}]({commit_url})"

    message += "\n<:kofi:1319086302116708444> An SCDL-Team spenden: [ko-fi.com/scdeutsch](https://ko-fi.com/scdeutsch)"

    send_discord_message(
        "Neue LIVE-Übersetzung verfügbar!",
        message,
        content="<@&1319635148471406724>",
    )

    logger.info("\n=== Deployment abgeschlossen ===")


if __name__ == "__main__":
    if "--blueprints" in sys.argv:
        send_blueprints_notification()
    else:
        main()
