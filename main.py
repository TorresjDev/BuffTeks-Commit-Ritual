from ritual.ui import console, show_intro_banner, run_loading_sequence, display_github_user_conf
from ritual.logic import fetch_github_name, add_to_hall_of_fame, display_hall_of_fame
from ritual.validator import run_system_check


def main():
    """
    BuffTeks Commit Ritual main entry point.
    Handles the sequence: banner -> validation -> ritual -> contribution.
    """
    console.print("\nloading BuffTeks Commit Ritual...\n")
    show_intro_banner()

    # Phase 1: Run system checks
    if not run_system_check():
        console.print(
            "[red3]❌ System validation failed. Please fix issues and retry.[/]")
        return

    # Phase 2: Run Rich loading animation
    run_loading_sequence()

    # Phase 3: Collect GitHub username while input is empty
    while True:
        input_github_username = console.input(
            "\n[bold cyan]👤 Enter your GitHub username:[/bold cyan] ").strip()
        if input_github_username:
            break
        console.print(
            "[dark_orange]⚠️  GitHub username is required and cannot be empty.[/] [italic #C0C0C0]Please try again.[/]")

    # input_github_username = console.input(
    #     "\n[bold cyan]👤 Enter your GitHub username:[/bold cyan] ").strip()
    github_full_name, github_username = fetch_github_name(
        input_github_username)
    full_name = display_github_user_conf(github_full_name)

    # Phase 4: Add to Hall of Fame
    success = add_to_hall_of_fame(github_username, full_name)
    if success:
        display_hall_of_fame()
        console.print(
            "[bold green4]✅ You can now proceed to push your contribution![/]")

        console.print("\n[bold cyan]💾 Remember:[/] Commit your changes and push them to GitHub!\n"
                      "Use VS Code Source Control or Git Bash:\n"
                      "  git add .\n  git commit -m 'Commit: Contributed to BuffTeks' "
                      "\n  git push\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[magenta]\n⚠️  Ritual aborted by user.[/]")
