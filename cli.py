import pyshorteners
import re, sys, socket, random, time, qrcode, os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.progress import Progress
from datetime import datetime

# Initialize Rich console
console = Console()

# Admin Details
ADMIN_NAME = "HackSageX aka Sumit Shah"
VERSION = "1.0.0"

# Dynamic Quotes
QUOTES = [
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

# Logging file
LOG_FILE = "url_history.log"

def animated_text(text, delay=0.05):
    for char in text:
        console.print(char, end="", style="cyan", justify="center")
        time.sleep(delay)
    console.print()

def home_logo():
    console.print(Panel.fit(f"""
    [bold magenta]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣦⠄⠀⠀⠀⠀
⠀⠈⠙⠿⣿⣿⣷⣦⣤⣤⣴⣾⣿⣿⠟⢋⠀⠀⠀⠀⠀⠀
⠀⣀⣀⣤⣤⣽⣿⣿⣿⣿⣿⣿⣿⣶⣤⣼⣤⠄⠀⠀⠀⠀
⠀⢸⣿⡿⢿⠿⠛⠉⠉⣇⠈⠉⠙⢻⡟⠿⡟⠀⠀⠀⠀⠀
⠀⠀⢀⠃⠸⠀⠀⠀⠀⡇⠀⠀⠀⠀⡇⠀⢳⠀⠀⠀⠀⠀
⠀⠀⢸⠀⢸⠀⠀⠀⠀⢳⠀⠀⠀⠀⡇⠀⢸⠀⠀⠀⠀⠀
⠀⠀⢸⠀⢸⠀⠀⠀⠀⢸⠀⠀⠀⠀⢹⠀⠀⡇⠀⠀⠀⠀
⠀⠀⢸⠀⢸⠀⠀⠀⠀⢸⠀⠀⠀⠀⠸⡀⠀⢣⠀⠀⠀⠀
⠀⠀⢸⠀⢸⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⡇⠀⢸⡀⠀⠀⠀
⠀⠀⢸⠀⢸⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⡇⠀⠀⣇⠀⠀⠀
⠀⠀⠀⠀⢸⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⢳⠀⠀⢻⠀⠀⠀
⠀⠀⢠⠀⢸⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢸⠀⠀⠘⡄⠀⠀
⠀⠀⠈⠀⢸⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢸⠀⠀⠀⡇⠀⠀
⠀⠀⡆⠀⢸⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠈⡇⠀⠀⢸⠀⠀
⠀⠀⡇⠀⢸⠀⠀⠀⢀⣴⣷⣦⡀⠀⠀⠀⡇⠀⠀⠘⡆⠀
⠀⢰⡇⠀⢸⠀⠀⠀⢸⣿⣿⣿⡧⠀⠀⠀⢇⠀⢀⣤⣧⡀
⠀⠀⡇⠀⠸⡄⠀⠀⠈⠻⢿⡟⠁⠀⠀⠀⠘⣰⡟⠁⠛⠃
⠠⣴⡷⣦⣄⠇⢀⢀⣤⢶⣿⣿⣿⠛⠛⠛⢻⠋⠀⠀⠀⠀
⠀⠑⠃⠈⢛⠷⡶⠟⠁⢸⣿⣿⣿⡆⠀⠀⠘⡆⠀⠀⠀⠀
⠀⠀⠀⠀⢰⡆⠀⠀⠀⢸⣿⣿⣿⣇⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠈⡇⠀⠀⠀⠘⢿⣿⣿⡟⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⢠⣿⠇⢸⣷⠀⠀⠀⢹⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⣾⡏⠀⠘⣿⡀⠀⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⢀⣼⡟⠀⠀⠀⠻⣧⣄⡀⠘⡄⠀⠀⠀
⠀⠀⠀⠀⠀⣧⡴⠟⠍⠀⠀⠀⠀⠀⠈⠙⠻⣦⣇⡀⠀⠀
⠀⠀⠀⢠⣿⣯⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⡿⠃⠀⠀
⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
    [bold yellow]Admin:[/] [cyan]{ADMIN_NAME}[/]    [bold yellow]Version:[/] [cyan]{VERSION}[/]
    [bold green]{random.choice(QUOTES)}
    """, title="[bold red]DarkRedirect[/]"))

def validate_url(url):
    return url.lower() if "http" in url.lower() and "://" in url else ""

def validate_domain(domain):
    return bool(re.match(r'^[A-Za-z0-9.]+$', domain))

def validate_phishing_keyword(keyword):
    return bool(re.match(r'^[a-zA-Z0-9-_]+$', keyword))

def internet_connection():
    try:
        socket.gethostbyname("www.google.com")
        return True
    except socket.gaierror:
        return False

def shorting_url(short_obj, url):
    try:
        return short_obj.short(url)
    except:
        console.print("[bold red]An error occurred while shortening the URL![/]")
        return "error"

def shortener_service(url):
    console.print("\n[bold yellow]Choose a URL shortening service:[/]")
    console.print("1. TinyURL\n2. DAGD\n3. Clck.ru\n4. is.gd\n5. osdb.link\n6. chilp.it", style="cyan")
    try:
        select = int(Prompt.ask("[bold green]Select (1-6)[/]", default="1"))
        shortener = pyshorteners.Shortener()
        if select == 1:
            return shorting_url(shortener.tinyurl, url)
        elif select == 2:
            return shorting_url(shortener.dagd, url)
        elif select == 3:
            return shorting_url(shortener.clckru, url)
        elif select == 4:
            return shorting_url(shortener.isgd, url)
        elif select == 5:
            return shorting_url(shortener.osdb, url)
        elif select == 6:
            return shorting_url(shortener.chilpit, url)
        else:
            console.print("[bold red]Invalid selection, please choose between 1-6.[/]")
            return "error"
    except ValueError:
        console.print("[bold red]Invalid input, please enter a number between 1-6.[/]")
        return "error"

def combiner(masked_url, domain_name, phishing_keyword):
    url_header, url_tail = masked_url.split("://")
    return f"{url_header}://{domain_name}-{phishing_keyword}@{url_tail}" if phishing_keyword else f"{url_header}://{domain_name}@{url_tail}"

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("masked_url_qr.png")
    console.print("[bold green]QR code generated and saved as 'masked_url_qr.png'![/]")

def log_url(url):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {url}\n")

def urlmask():
    home_logo()
    if not internet_connection():
        console.print("[bold red]No internet connection detected! Exiting...[/]")
        return
    
    original_url = Prompt.ask("[bold cyan]Enter original URL[/]", default="https://google.com")
    if validate_url(original_url) == "":
        console.print("[bold red]Invalid URL! Please enter a valid URL.[/]")
        return
    
    console.print("[bold yellow]Shortening URL...[/]")
    with Progress() as progress:
        task = progress.add_task("Shortening...", total=100)
        for _ in range(10):
            time.sleep(0.1)
            progress.update(task, advance=10)
    masked_url = shortener_service(original_url)
    if masked_url == "error":
        return

    domain_name = Prompt.ask("[bold cyan]Enter the domain to mask the URL with[/]", default="google.com").lower()
    if not validate_domain(domain_name):
        console.print("[bold red]Invalid domain! Please enter a correct domain.[/]")
        return

    phishing_key = Prompt.ask("[bold cyan]Do you want to add a phishing keyword? (yes/no)[/]", default="no").lower()
    phishing_keyword = ""
    if phishing_key == "yes":
        phishing_keyword = Prompt.ask("[bold cyan]Enter phishing keyword[/]", default="free").lower()
        if not validate_phishing_keyword(phishing_keyword):
            console.print("[bold red]Invalid keyword! Use letters, numbers, '-' or '_'.[/]")
            return
    
    final_url = combiner(masked_url, domain_name, phishing_keyword)
    console.print(Panel.fit(f"[bold green]Masked URL:[/] {final_url}", title="[bold blue]Final Result[/]"))
    
    # Generate QR Code
    generate_qr_code(final_url)
    
    # Log the URL
    log_url(final_url)
    console.print("[bold green]URL logged to history![/]")

if __name__ == "__main__":
    urlmask()
