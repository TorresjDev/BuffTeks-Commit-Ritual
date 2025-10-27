import time
import inquirer
from inquirer.themes import BlueComposure
from numpy import full
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.progress import Progress, BarColumn, TextColumn
from rich.console import Console

console = Console()


def show_banner():
    console.print("""
[bold cyan]🐃 BuffTeks Commit Ritual[/]
────────────────────────────────────────
Welcome to the digital rite of passage.
Every contribution is part of our legacy.
────────────────────────────────────────────────────
[italic cyan1]Commit to Learn, Commit to Code, Commit to BuffTeks![/]
""")
    time.sleep(0.5)


def run_loading_sequence():
    """Single unified progress bar for all loading stages."""

    stages = [
        ("red3", "Initializing BuffTeks system...", "🛠️ "),
        ("orange3", "Validating core components...", "🤔"),
        ("yellow3", "Unboxing workshop modules...", "📤"),
        ("green3", "Configuring your environment...", "⚙️ "),
        ("blue3", "Cleaning up Workshop 🏪", "🧹")
    ]

    # Create progress display
    with Progress(
        SpinnerColumn(),
        BarColumn(bar_width=30, style="gold3", complete_style="green4",
                  finished_style="deep_sky_blue3"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("{task.description}"),
        console=console,
        transient=True
    ) as progress:

        task = progress.add_task(
            "[yellow]🔄 Preparing the BuffTeks ritual...", total=100)

        stage_count = len(stages)
        increment_per_stage = 100 / stage_count

        for i, (color, message, emoji) in enumerate(stages):
            # Change task description dynamically
            progress.update(
                task, description=f"[bold {color}]{emoji} {message}")
            # Animate smooth progression through each phase
            start = int(i * increment_per_stage)
            end = int((i + 1) * increment_per_stage)
            for percent in range(start, end):
                progress.update(task, completed=percent)
                time.sleep(0.03)
            time.sleep(0.02)

        # Finish progress cleanly
        progress.update(task, completed=100,
                        description="[dodger_blue2]✅ Workshop Ritual Complete! 🎉")
        time.sleep(0.5)

    console.print(
        "🦬 [magenta3] Welcome to the [bold gold1]BuffTeks Commit Ritual[/bold gold1]![/magenta3]\n")


def confirm_github_user(username: str) -> str:
    """
    Confirms if the provided GitHub username exists via the public API.

    Args:
        username (str): GitHub username to confirm.

    Returns:
        str: Full name of the user if confirmed, else prompts for manual entry.
    """
    if username:
        console.print(
            f"[bold]Is this your correct name[/]: [bold cyan1]{username}[/]")

        confirmation_question = [
            inquirer.List(
                'confirm_name',
                message="Please confirm",
                choices=[' Yes', ' No'],
                default=' Yes'
            )
        ]
        confirmation = inquirer.prompt(
            confirmation_question, theme=BlueComposure())
        if confirmation['confirm_name'] == ' Yes':
            return username
        else:
            return console.input(
                "[bold cyan]📝 Enter your full name (optional):[/bold cyan] ").strip()
    else:
        console.print("[red3]GitHub name could not be verified.[/]")
        return console.input(
            "[bold cyan]📝 Enter your full name (optional):[/bold cyan] ").strip()
