import time
import inquirer
from inquirer.themes import BlueComposure
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.progress import Progress, BarColumn, TextColumn
from rich.console import Console

console = Console()


def show_intro_banner():
    console.print("""
[bold cyan]🐃 BuffTeks Commit Ritual[/]
[bold gold3]────────────────────────────────────────[/]
[#C0C0C0]Welcome to the digital rite of passage.
Every contribution is part of our legacy.[/]
[bold gold3]────────────────────────────────────────────────────[/]
[italic cyan1]Commit to Learn, Commit to Code, Commit to BuffTeks![/]
""")
    time.sleep(0.5)


def run_loading_sequence():
    """Displays the progress bar for all loading stages."""

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
                        description="[#C0C0C0]✅ Workshop Ritual Loaded Successfully! 🎉")
        time.sleep(0.5)

    console.print(
        "🦬 [magenta3] Welcome to the [bold gold1]BuffTeks Commit Ritual[/bold gold1]![/magenta3]\n")


def display_github_user_conf(user_full_name: str) -> str:
    """
    Displays a confirmation prompt for the GitHub username.

    Args:
        username (str): GitHub username to confirm.

    Returns:
        str: Full name of the user (required).
    """
    if user_full_name:
        console.print(
            f"[bold]Is this your correct name[/]: [bold cyan1]{user_full_name}[/]")
        time.sleep(0.3)
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
            return user_full_name
        else:
            time.sleep(0.3)
            return _get_required_full_name()
    else:
        time.sleep(0.3)
        console.print(
            "[red3] Your full name is required to complete the ritual.[/]")
        time.sleep(0.3)

        return _get_required_full_name()


def _get_required_full_name() -> str:
    """
    Prompts the user to enter their full name and validates it.
    Keeps asking until a valid full name is provided.

    Returns:
        str: Valid full name
    """
    while True:
        try:
            full_name = console.input(
                "[bold cyan]📝 Please enter your full name (First Last):[/bold cyan] ").strip()

            if not full_name:
                console.print(
                    "[dark_orange]⚠️  Full name is required and cannot be empty.[/] [italic #C0C0C0]Please try again.[/]")
                continue

            # Check if name contains at least one space (first + last name)
            if ' ' not in full_name:
                console.print(
                    "[dark_orange]⚠️  Please enter both first and last name (e.g., 'John Doe').[/] [italic #C0C0C0]Please try again.[/]")
                continue

            # Split name and check each part has at least 2 characters
            parts = full_name.split()
            if len(parts) < 2 or len(parts[0]) < 2 or len(parts[1]) < 2:
                console.print(
                    "[dark_orange]⚠️  First and last name must each be at least 2 characters.[/] [italic #C0C0C0]Please try again.[/]")
                continue

            return full_name

        except Exception as e:
            console.print(f"[red3]Error: {e}[/]")
            return _get_required_full_name()
