import os
import time
import random
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def banner():
    hacking_quotes = [
    "Empowering cybersecurity, one tool at a time!",
    "Security isn’t a product, it’s a process!",
    "Code hard, secure harder!",
    "Hacking is not a crime, it's an art of protection!",
    "Stay anonymous, stay safe!",
    "Hack the system, secure the future!",
"Encryption is not an option, it's a necessity!",
"Every byte counts when security is at stake!",
"Think like a hacker, defend like a warrior!",
"Digital footprints never fade—stay cautious!",
"In cybersecurity, knowledge is the ultimate weapon!",
"Firewalls up, threats down!",
"Security through obscurity is not security at all!",
"The best defense is an unpredictable offense!",
"Your password is your first line of defense—make it strong!",
"Data is the new gold—protect it at all costs!",
"Privacy isn’t a privilege, it’s a right!",
"Hack ethically, secure endlessly!",
"Cybersecurity is a mindset, not just a skill!",
"Stay alert, stay secure!",
"There’s no patch for human error—educate yourself!",
"Protect first, react second!",
"Hackers don’t break in, they log in!",
"The weakest link in security is always human!",
"Without security, innovation is just a risk!",
"Threats evolve, so should your defenses!",
"A single click can cost millions—think before you click!",
"Cybercrime doesn’t sleep, neither should your defenses!",
"Not all hackers wear hoodies, some wear suits!",
"A strong password is like a good lock—don't leave it weak!",
"Cybersecurity starts with you!",
"Trust, but verify!",
"Never underestimate the power of a good VPN!",
"Phishing is real—don’t take the bait!",
"Hackers exploit ignorance—educate yourself!",
"Antivirus is good, but common sense is better!",
"Secure your code like your life depends on it!",
"Zero trust is the best trust in cybersecurity!",
"Hackers adapt, so should your security!",
"Privacy matters—don’t trade it for convenience!",
"No system is 100% secure, but layers of security help!",
"Your security is only as strong as your weakest link!",
"Cybersecurity is not a destination, it's a journey!",
"Hackers don’t need doors when there are open windows!",
"Online security isn’t optional, it’s mandatory!",
"Protect your data before it becomes someone else’s!",
"Cyber threats don’t knock, they break in!",
"Two-factor authentication: Because one isn’t enough!",
"The internet never forgets—think before you share!",
"Malware doesn’t discriminate—stay protected!",
"Data leaks faster than water—secure your flow!",
"Security isn’t just a tool, it’s a culture!",
"Backups save data, but security saves trust!",
"Digital security is the key to online freedom!",
"Hack wisely, secure fiercely!"
]

    quote = random.choice(hacking_quotes)
    
    banner_text = """
╭──────────────────── DarkRedirect ───────────────────────╮
│                                                         │
│ ⠀⠀⠀⠀⠀⠀⠀⠀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡟⠉⠙⠳⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠇⠐⠀⠀⠀⠀⠉⠛⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠈⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠓⠒⠓⠒⠶⠤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣄
⠀⠀⠀⠀⠀⠀⠀⣿⢿⠈⢻⣆⠀⠀⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡙⠻⢯⣉⠛⠉⠉⠉⠁⠀⠀⠀⠀⢨⣽
⠀⠀⠀⠀⠀⠀⠀⣿⡇⠗⠈⢿⣶⣾⡿⠃⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢸⣿⡿⠁⠀⠀⣠⠖⠛⢉⣯⡉⠙⠳⢦⡀⠀⠀⠀⠀⢀⣠⣀⣀⣀⠀⠀⠀⠀⠀⠀⢀⣠⣬⣿⠃
⠀⠀⠀⠀⠀⠀⠀⣿⡇⣶⠰⣼⡟⠀⠀⢠⡞⠁⠀⠀⢸⣿⡇⠀⠀⠀⣿⠀⠀⠀⢠⡟⠉⠀⢹⣯⠛⢦⡀⢀⣴⣾⣿⣿⣿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣷⡿⣸⠟⠀⠀⠀⠈⣧⡀⠀⠀⠈⣿⢃⣠⡴⠞⢁⠀⢀⡀⢈⣧⡀⠀⢸⣿⠀⠀⢹⣼⣿⣿⣿⣿⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡟⠀⠀⠀⠀⠀⠈⠉⠉⠉⠙⠋⠉⠁⠀⠀⠻⠶⠿⣷⡾⠋⡙⢦⣜⡛⠀⠀⣰⠏⢻⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠇⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣶⣷⣶⣿⡁⠀⡈⠉⠻⠟⠁⠀⢸⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠀⣀⠀⠀⠀⠀⢀⣀⣠⣤⡤⠶⠟⠛⠋⠉⠀⠀⠀⠀⠀⠈⠻⢦⡀⠀⠀⠀⠀⠈⢹⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣿⡇⣿⡿⣶⣿⣟⣿⣿⡿⠟⠋⠙⠻⢷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣽⣷⣄⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⣙⢿⣿⠿⠯⠤⢤⣀⣀⣀⡴⠮⠋⠀⠀⠀⠀⠀⠀⠀⠰⠾⠛⡏⠉⠀⠛⣷⣄⡀⣺⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣀⣀⠤⠤⠈⠉⠁⠀⠀⠀⠀⣆⠀⠀⡀⠀⣤⡀⠀⠀⠹⣤⣀⣀⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠛⢿⡈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠋⠛⠚⠋⠀⠀⠀⠲⢤⣄⡈⢙⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣶⢾⣷⣄⠈⠻⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣵⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡿⣿⣿⣿⠿⣿⣾⣽⣿⢿⣶⣄⣀⠀⠀⠀⠀⣀⣀⣀⣤⣶⣶⣾⣿⣿⣟⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣷⣿⣿⣁⠀⠀⢈⣙⣙⣻⢷⣿⣿⣦⡀⢈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⡿⣻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠿⣣⣾⠟⠛⠛⢿⣿⡿⣿⡿⣿⣿⢿⠙⠙⡿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣶⣿⡏⠀⢀⣠⣿⡿⠗⢾⡷⠶⣿⣿⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣰⣟⢛⣭⡉⠀⠀⣹⠀⠀⠘⠿⣤⣀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣟⠓⠲⠤⣤⣤⣀⣀⣀⣀⣀⣿⣿⣿⣿⣿⣿⣟⡻⠶⣿⣷⣶⣿⣤⣤⣤⣤⣿⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠓⠲⠤⢤⣤⣤⣄⣀⣬⣯⣿⣿⠉⠉⢻⡛⠛⠛⠛⠻⠿⠿⠿⣶⣶⠿⠿⠿⠿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡷⡆⠀⠀⡀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠈⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⡟⠛⠛⠒⠶⠶⠶⠶⠶⣶⠊⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⢄⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
│     Admin: HackSageX aka Sumit Shah    Version: 1.0.0 │
│     {quote:<50}                                       │
│                                                       │
╰───────────────────────────────────────────────────────╯
"""
    console.print(Text(banner_text.format(quote=quote), style="green"))

def main_menu():
    console.print("\n[cyan]Select an option:[/cyan]")
    console.print("[1] CLI (Terminal Based Tool)")
    console.print("[2] GUI (Graphical User Interface)")
    console.print("[3] Exit")
    choice = Prompt.ask("[bold yellow]Enter your choice[/bold yellow]", choices=["1", "2", "3"])
    return choice

def main():
    os.system("clear" if os.name == "posix" else "cls")
    banner()
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            console.print("\n[green]Launching CLI Tool...[/green]", style="bold")
            time.sleep(1)
            os.system("python cli.py")
        elif choice == "2":
            console.print("\n[blue]Launching GUI Tool...[/blue]", style="bold")
            time.sleep(1)
            os.system("python gui.py")
        elif choice == "3":
            console.print("\n[red]Exiting... Stay Safe![/red]", style="bold")
            time.sleep(1)
            break
        
if __name__ == "__main__":
    main()
