import re
import requests
from pathlib import Path
from datetime import datetime
from ritual.ui import console
from rich.table import Table

from ritual.validator import _is_valid_name, fetch_github_name

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
    name = fullname or fetch_github_name(val_username)

    # Check: Read README.md safely
    section = get_hall_of_fame_section()
    if not section:
        return False

    text, table_start, section_end = section
    table_text = text[table_start:section_end]

    # Prevent duplicate entries
    if f"@{val_username}" in text.lower():
        console.print(
            f"[yellow]🫸  A BuffTeks contributor with the GitHub username of: {username} is already in the Hall of Fame![/]")
        console.print(
            "[cyan1]   - Please stage and commit changes to proceed into pushing your contribution to our repository! 🔥[/]")

        return False

    # Append new entry
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
        f"""[#C0C0C0]==========================================================================[/]\n[gold3]🔥 {name} has been successfully added to the BuffTeks Hall of Fame! 🎉[/]\n[#C0C0C0]==========================================================================[/]""")
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
