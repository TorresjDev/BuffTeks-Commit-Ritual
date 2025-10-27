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
