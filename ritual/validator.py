import shutil
import sys
import requests
from rich.table import Table
from ritual.ui import console


def run_system_check():
    """
    Validates environment setup for BuffTeks Commit Ritual.
    Checks Python version, Git installation, internet access, and dependencies.
    Return:
        bool: True if all checks pass.
    """
    console.print("\n🧰 [bold green4]Running system validation checks...[/]\n")

    table = Table(title="System Validation Checks",
                  show_header=True, header_style="bold magenta")
    table.add_column("Check", justify="left",)
    table.add_column("Status", justify="center")

    checks = {
        "Python Version (>=3.8)": sys.version_info >= (3, 8),
        "Git Installed": shutil.which("git") is not None,
        "Internet Connection": _test_connection(),
        "Required Libraries": _test_dependencies(),
    }

    all_passed = True
    for check, result in checks.items():
        status = "✅" if result else "❌"
        if not result:
            all_passed = False
        table.add_row(check, status)

    console.print(table)

    if not all_passed:
        console.print(
            "\n[red3]Some checks failed. Please fix the issues above before continuing.[/]\n")
    else:
        console.print("[bold green4]All systems operational![/]\n")

    return all_passed


def _test_connection():
    """
    Tests for internet connectivity by pinging GitHub API.

    Returns:
        bool: True if internet connection is available, False otherwise.

    """
    try:
        requests.head("https://api.github.com", timeout=3)
        return True
    except Exception:
        console.print(
            "[dark_orange]⚠️ No internet connection. GitHub validation may fail.[/]")
        return False


def _test_dependencies():
    """
    Ensures core dependencies are installed locally.

    Returns:
        bool: True if all dependencies are present, False otherwise.
    """
    try:
        import rich
        import inquirer
        return True
    except ImportError as e:
        console.print(f"[red3]Missing dependency:[/] {e.name}")
        return False


def _is_valid_name(name: str, username: str) -> bool:
    """
    Validates the fetched GitHub name.
    Ensures it's not None, not empty, not just the username, and contains first + last name.

    Args:
        name (str): Fetched GitHub name.
        username (str): GitHub username.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not name or name.strip() == "":
        return False

    name = name.strip()
    username = username.strip().lower()

    # Check if name is just the username (case-insensitive)
    if name.lower() == username or name.lower() == f"@{username}":
        return False

    # Check if name contains at least one space (first + last name)
    if ' ' not in name:
        return False

    return True

# validate github account exists and return owner name


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

            if data.get("user_view_type") != "public":
                console.print("[yellow]⚠️  GitHub user is not public.[/]")
                console.print("Unable to access full name from GitHub.")
                return None, None

            github_username = data.get("login")
            console.print(f"[green3]GitHub user {github_username} found[/]")
            full_name = data.get("name")

            # validate name
            if _is_valid_name(full_name, username):
                return full_name, github_username
            else:
                console.print(
                    "[yellow] - But could not find a valid full name from GitHub account 🤔[/]")
                return None, github_username
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
    return None, None
