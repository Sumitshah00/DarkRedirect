import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyshorteners
import re, socket, random, time, qrcode, pyperclip, threading
from PIL import Image, ImageTk
import os

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


# Initialize URL Shortener
shortener = pyshorteners.Shortener()

# Functions
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
        return "error"

def shortener_service(url, service):
    if service == "TinyURL":
        return shorting_url(shortener.tinyurl, url)
    elif service == "DAGD":
        return shorting_url(shortener.dagd, url)
    elif service == "Clck.ru":
        return shorting_url(shortener.clckru, url)
    else:
        return "error"

def combiner(masked_url, domain_name, phishing_keyword):
    url_header, url_tail = masked_url.split("://")
    return f"{url_header}://{domain_name}-{phishing_keyword}@{url_tail}" if phishing_keyword else f"{url_header}://{domain_name}@{url_tail}"

def generate_qr_code(url):
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        qr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "masked_url_qr.png")
        img.save(qr_path)
        return img
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None

def copy_to_clipboard(url):
    pyperclip.copy(url)
    messagebox.showinfo("Copied", "URL copied to clipboard!")

def log_history(url):
    with open("history.log", "a") as f:
        f.write(f"{time.ctime()}: {url}\n")

# Matrix Background Animation
class MatrixBackground:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.digits = "01"
        self.font_size = 14
        self.columns = max(1, width // (self.font_size * 2))  # Increased number of columns
        self.positions = [random.randint(-height, 0) for _ in range(self.columns)]
        self.speed = 50  # Reduced delay for faster updates
        self.last_update = time.time()
        self.frame_rate = 60  # Increased target FPS
        self.frame_interval = 1.0 / self.frame_rate
        self.matrix_items = []
        self.create_matrix()

    def create_matrix(self):
        for i in range(self.columns):
            x = i * self.font_size * 2
            y = self.positions[i]
            for j in range(random.randint(3, 10)):
                char = random.choice(self.digits)
                item = self.canvas.create_text(x, y + j * self.font_size, text=char, fill="#00ff00", font=("Courier", self.font_size))
                self.matrix_items.append(item)

    def update(self):
        current_time = time.time()
        if current_time - self.last_update < self.frame_interval:
            self.canvas.after(int(self.speed / 2), self.update)
            return

        # Clean up old items
        for item in self.matrix_items:
            self.canvas.delete(item)
        self.matrix_items.clear()

        # Create new items
        for i in range(self.columns):
            x = i * self.font_size * 2
            y = self.positions[i]
            for j in range(random.randint(3, 10)):
                char = random.choice(self.digits)
                item = self.canvas.create_text(x, y + j * self.font_size, text=char, fill="#00ff00", font=("Courier", self.font_size))
                self.matrix_items.append(item)
            self.positions[i] += self.font_size
            if self.positions[i] > self.height:
                self.positions[i] = random.randint(-self.height, 0)

        self.last_update = current_time
        self.canvas.after(self.speed, self.update)

# GUI Application
class DarkRedirectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DarkRedirect")
        self.root.geometry("1000x700")
        self.root.configure(bg="#000000")
        self.root.bind("<Configure>", self.on_resize)
        self.setup_ui()

    def setup_ui(self):
        # Matrix Background
        self.canvas = tk.Canvas(self.root, bg="#000000", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.matrix = MatrixBackground(self.canvas, self.root.winfo_width(), self.root.winfo_height())
        self.matrix.update()

        # Main Frame
        self.main_frame = tk.Frame(self.root, bg="#000000", bd=2, relief=tk.RIDGE)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Header
        header = tk.Label(self.main_frame, text="DarkRedirect", font=("Courier", 24, "bold"), fg="#00ff00", bg="#000000")
        header.pack(pady=10)

        # Admin Info
        admin_info = tk.Label(self.main_frame, text=f"Admin: {ADMIN_NAME} | Version: {VERSION}", font=("Courier", 12), fg="#00ff00", bg="#000000")
        admin_info.pack()

        # Random Quote
        self.quote_label = tk.Label(self.main_frame, text=random.choice(QUOTES), font=("Courier", 10), fg="#00ff00", bg="#000000", wraplength=400)
        self.quote_label.pack(pady=5)

        # URL Input
        url_frame = tk.Frame(self.main_frame, bg="#000000")
        url_frame.pack(pady=10)
        tk.Label(url_frame, text="Enter Original URL:", font=("Courier", 12), fg="#00ff00", bg="#000000").grid(row=0, column=0, padx=5)
        self.url_entry = tk.Entry(url_frame, width=50, font=("Courier", 12), bg="#1a1a1a", fg="#00ff00")
        self.url_entry.grid(row=0, column=1, padx=5)

        # Domain Input
        tk.Label(url_frame, text="Enter Domain:", font=("Courier", 12), fg="#00ff00", bg="#000000").grid(row=1, column=0, padx=5)
        self.domain_entry = tk.Entry(url_frame, width=50, font=("Courier", 12), bg="#1a1a1a", fg="#00ff00")
        self.domain_entry.grid(row=1, column=1, padx=5)

        # Phishing Keyword
        tk.Label(url_frame, text="Phishing Keyword (optional):", font=("Courier", 12), fg="#00ff00", bg="#000000").grid(row=2, column=0, padx=5)
        self.phishing_entry = tk.Entry(url_frame, width=50, font=("Courier", 12), bg="#1a1a1a", fg="#00ff00")
        self.phishing_entry.grid(row=2, column=1, padx=5)

        # Shortener Service Buttons
        self.service_var = tk.StringVar(value="TinyURL")
        services = ["TinyURL", "DAGD", "Clck.ru"]
        service_frame = tk.Frame(self.main_frame, bg="#000000")
        service_frame.pack(pady=10)
        for service in services:
            tk.Radiobutton(service_frame, text=service, variable=self.service_var, value=service, font=("Courier", 12), fg="#00ff00", bg="#000000", selectcolor="#1a1a1a").pack(side=tk.LEFT, padx=5)

        # Generate Button
        generate_btn = tk.Button(self.main_frame, text="Generate Masked URL", font=("Courier", 12), fg="#00ff00", bg="#1a1a1a", command=self.generate_url)
        generate_btn.pack(pady=20)

        # Result Display
        self.result_label = tk.Label(self.main_frame, text="", font=("Courier", 12), fg="#00ff00", bg="#000000")
        self.result_label.pack(pady=10)

        # QR Code Display
        self.qr_label = tk.Label(self.main_frame, bg="#000000")
        self.qr_label.pack(pady=10)

        # History Log with improved scrolling
        history_frame = tk.Frame(self.main_frame, bg="#000000")
        history_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        history_label = tk.Label(history_frame, text="History Log", font=("Courier", 12), fg="#00ff00", bg="#000000")
        history_label.pack(pady=5)
        
        # Create scrollbar first
        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create text widget with scrollbar
        self.history_text = scrolledtext.ScrolledText(
            history_frame,
            width=80,
            height=10,
            font=("Courier", 10),
            bg="#1a1a1a",
            fg="#00ff00",
            yscrollcommand=scrollbar.set,
            wrap=tk.WORD
        )
        self.history_text.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        
        # Configure scrollbar
        scrollbar.config(command=self.history_text.yview)
        
        self.load_history()

    def on_resize(self, event):
        if event.widget == self.root:
            try:
                width = event.width
                height = event.height
                if width > 0 and height > 0:  # Ensure valid dimensions
                    self.canvas.configure(width=width, height=height)
                    self.matrix.width = width
                    self.matrix.height = height
                    self.matrix.columns = max(1, width // self.matrix.font_size)
                    self.matrix.positions = [random.randint(-height, 0) for _ in range(self.matrix.columns)]
                    # Update main frame position
                    if hasattr(self, 'main_frame'):
                        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            except Exception as e:
                print(f"Error during resize: {e}")

    def generate_url(self):
        def url_generation_task():
            original_url = self.url_entry.get()
            domain_name = self.domain_entry.get()
            phishing_keyword = self.phishing_entry.get()
            service = self.service_var.get()
        
            if not internet_connection():
                messagebox.showerror("Error", "No internet connection detected!")
                return
        
            if not validate_url(original_url):
                messagebox.showerror("Error", "Invalid URL! Please enter a valid URL.")
                return
        
            if not validate_domain(domain_name):
                messagebox.showerror("Error", "Invalid domain! Please enter a correct domain.")
                return
        
            if phishing_keyword and not validate_phishing_keyword(phishing_keyword):
                messagebox.showerror("Error", "Invalid keyword! Use letters, numbers, '-' or '_'.")
                return
        
            masked_url = shortener_service(original_url, service)
            if masked_url == "error":
                messagebox.showerror("Error", "An error occurred while shortening the URL!")
                return
        
            final_url = combiner(masked_url, domain_name, phishing_keyword)
            
            # Update UI in main thread
            self.root.after(0, lambda: self.update_ui(final_url))
        
        # Start URL generation in a separate thread
        threading.Thread(target=url_generation_task, daemon=True).start()

    def update_ui(self, final_url):
        self.result_label.config(text=f"Masked URL: {final_url}")
        self.result_label.bind("<Button-1>", lambda e: copy_to_clipboard(final_url))

        # Generate QR Code
        qr_img = generate_qr_code(final_url)
        if qr_img:
            qr_img_tk = ImageTk.PhotoImage(qr_img)
            self.qr_label.config(image=qr_img_tk)
            self.qr_label.image = qr_img_tk
        else:
            messagebox.showerror("Error", "Failed to generate QR code!")

        # Log History
        log_history(final_url)
        self.load_history()

    def load_history(self):
        if os.path.exists("history.log"):
            with open("history.log", "r") as f:
                self.history_text.delete(1.0, tk.END)
                self.history_text.insert(tk.END, f.read())

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = DarkRedirectApp(root)
    root.mainloop()
