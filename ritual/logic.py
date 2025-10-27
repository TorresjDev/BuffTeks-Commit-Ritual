import re
from turtle import st
import requests
from pathlib import Path
from datetime import datetime

# from streamlit import user
from ritual.ui import console
from rich.table import Table

README_PATH = Path("README.md")


def get_hall_of_fame_section():
    """
    Validates README.md and locates the BuffTeks Hall of Fame section.
    Returns a tuple of (text, table_start, section_end) if successful, or None on failure.
    """
    if not README_PATH.exists():
        console.print("[red3]❌ README.md not found.[/]")
        return None

    text = README_PATH.read_text(encoding="utf-8")

    start_marker = "## 🏆 BuffTeks Hall of Fame"
    table_header = "| Name         | GitHub                                       | Join Date  |\n| ------------ | -------------------------------------------- | ---------- |\n"
    end_marker = "\n---"

    start_index = text.find(start_marker)
    table_start = text.find(table_header, start_index)

    if start_index == -1 or table_start == -1:
        console.print(
            "[red3]❌ Could not locate Hall of Fame table in README.md.[/]")
        return None

    section_end = text.find(end_marker, table_start)
    section_end = section_end if section_end != -1 else len(text)

    # Return all relevant values so they can be reused elsewhere
    return text, table_start, section_end


def add_to_hall_of_fame(username: str, fullname: str):
    """
    Adds a contributor entry to the Hall of Fame section in README.md.
    Uses the GitHub API to fetch the user's display name and appends their data
    to the contributor table without overwriting existing rows.

    Args:
        username (str): GitHub username of the contributor.
        fullname (str, optional): Full name of the contributor. If not provided, fetched from GitHub. Defaults to None.

    Returns:
        Bool: True if added successfully, False otherwise.
    """

    val_username = username.strip().lower()
    # --- 1st Check: Basic input validation
    if not re.fullmatch(r"[A-Za-z0-9-]+", val_username):
        console.print(
            f"[red3]❌ Invalid GitHub username format. [/] {val_username}")
        return False

    # --- 2nd Check: Verify GitHub user existence
    name = fullname or fetch_github_name(val_username)
    if not name:
        console.print(
            f"[red3]❌ Unable to verify GitHub user: {val_username}[/]")
        return False
    else:
        name = name.replace("|", "\\|").strip()

    # # --- 3rd Check: Read README.md safely
    section = get_hall_of_fame_section()
    if not section:
        return False

    text, table_start, section_end = section
    table_text = text[table_start:section_end]

    # --- 4th Check: Prevent duplicate entries
    if f"@{val_username}" in text.lower():
        console.print(
            f"[yellow]🫸  A BuffTeks contributor with the GitHub username of: {username} is already in the Hall of Fame![/]")
        console.print(
            "[cyan1]   - Please confirm and proceed to pushing your contribution to our repository![/]")

        return False

    # --- 5th Step: Append new entry
    today = datetime.now().strftime("%Y-%m-%d")
    new_entry = f"| {name} | [@{val_username}](https://github.com/{val_username}) | {today} |\n"

    if new_entry.strip() in table_text:
        console.print("[yellow]🫸  You are already in the Hall of Fame![/]")
        console.print(
            "[cyan1]   - Please proceed to pushing your contribution to our repository![/]")
        return False

    updated_table = table_text.strip() + "\n" + new_entry
    updated_readme = text[:table_start] + updated_table + text[section_end:]

    # --- 6th Step: Write back to README.md
    tmp_path = README_PATH.with_suffix(".tmp")
    tmp_path.write_text(updated_readme, encoding="utf-8")
    tmp_path.replace(README_PATH)

    console.print(
        f"[green3]🔥 {name} has been successfully added to the BuffTeks Hall of Fame! 🎉[/]\n")
    return True


def display_hall_of_fame():
    """
    Reads and prints the BuffTeks Hall of Fame Markdown table as a Rich table.
    """
    section = get_hall_of_fame_section()
    if not section:
        return

    # Parse Markdown table rows
    text, table_start, section_end = section
    table_text = text[table_start:section_end]
    lines = table_text.strip().split("\n")
    # Extract headers
    headers = [h.strip() for h in lines[0].split("|")[1:-1]]
    table = Table(title="🏆 BuffTeks Hall of Fame", header_style="bold gold3")
    for header in headers:
        table.add_column(header, justify="center")

    for row in lines[2:]:  # Skip header + divider line
        cols = [c.strip() for c in row.split("|")[1:-1]]
        table.add_row(*cols)

    console.print(table)


def fetch_github_name(username: str):
    """
    Fetches a GitHub user's display name via the public API.
    Returns the name if found, or None otherwise.
    """
    try:
        headers = {"User-Agent": "BuffTeks-Commit-Ritual"}
        response = requests.get(
            f"https://api.github.com/users/{username}", headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # console.print(data) # Debug: print full response data
            return data.get("name") or username
        elif response.status_code in (403, 429):
            console.print(
                "[yellow]⚠️  GitHub API limit reached. Try again later.[/]")
        elif response.status_code == 404:
            console.print("[red3]User not found on GitHub.[/]")
        else:
            console.print(
                f"[red3]GitHub API returned status {response.status_code}.[/]")
    except Exception as e:
        console.print(f"[red3]Network or API error: {e}[/]")
    return None
