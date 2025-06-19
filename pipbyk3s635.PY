import os
import time
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.live import Live
    from rich.text import Text
    from rich.progress import track
except:
    os.system('pip install rich')
    from rich.console import Console
    from rich.panel import Panel
    from rich.live import Live
    from rich.text import Text
    from rich.progress import track

console = Console()
logo_text = Text("🛠️ PIP INSTALLER FOR SCRIPT🛠️", justify="center", style="bold")
colors = ["red", "yellow", "green", "cyan", "magenta", "blue"]
packages = [
    "OneClick", "stdiomask", "user_agent", "instaloader", "requests",
    "rich", "telebot", "python-cfonts", "pyfiglet", "py_compile", "socks",
    "youtube_dl", "uuid", "colorama", "beautifulsoup4", "pafy", "bs4",
    "argparse", "InstagramAPI", "generate_user_agent", "fore", "threading",
    "datetime", "secrets", "token_hex", "re", "cryptography==3.3.2", "nltk", "aiohttp"
]
def display_logo():
    with Live(console=console, refresh_per_second=2) as live:
        start_time = time.time()
        while time.time() - start_time < 5:
            for color in colors:
                logo_panel = Panel(
                    logo_text,
                    title="Welcome to the Installer",
                    title_align="center",
                    border_style=color,
                    padding=(2, 4),
                )
                live.update(logo_panel)
                time.sleep(0.5)
display_logo()

console.clear()

console.print("[bold cyan]🚀 Starting the installation of required packages...[/bold cyan]\n")

for package in track(packages, description="[bold green]Installing packages[/bold green]", style="green"):
    console.print(f"[bold yellow]→ Installing [italic]{package}[/italic]...[/bold yellow]")
    exit_code = os.system(f'pip install {package}')

    if exit_code == 0:
        console.print(f"[bold green]✔ Successfully installed [italic]{package}[/italic]![/bold green]\n")
    else:
        console.print(f"[bold red]✖ Failed to install [italic]{package}[/italic]. Check for errors above.[/bold red]\n")

console.print(Panel(
    "≠" * 60,
    style="bold red"
))
console.print(
    Panel.fit(
        "[bold green]🎉 All required packages have been successfully installed! 🎉[/bold green]\n"
        "[bold magenta]You can now use any tool without installation issues.[/bold magenta]",
        title="Installation Complete", border_style="green"
    )
)
console.print("\n[dim]💻 Script created by [@k3s63][/dim]", justify="center")
console.print("\n[bold cyan]Press [italic]Enter[/italic] to exit...[/bold cyan]", justify="center")
input()