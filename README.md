<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmYxeW5ibnNndDZ3ZWkzODNzNGd5bGxndDV0eGN6Zm81OTFwM2U5eiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/tHIRLHtNwxpjIFqPdV/giphy.gif" alt="DarkRedirect Logo" width="150" style="border-radius: 50%;"/>
  
  # DarkRedirect🚀
  
  **A powerful URL masking tool with CLI and GUI interfaces**
  
  [![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://github.com/hacksagex/darkredirect)
</div>
## Features

- Command-line and GUI interfaces
- Multiple URL shorteners (TinyURL, DAGD, Clck.ru)
- QR code generation for masked URLs
- Custom domain masking
- History logging and URL validation
  
## Detailed Installation Guide

### System Requirements

#### Minimum Requirements
- Python 3.7 or higher
- Internet connection for URL shortening services

#### Supported Platforms
- Linux
- Android (Termux)
- macOS
- Windows

### Dependencies

```bash
# Core Dependencies
python >= 3.7
tkinter (for GUI mode)
pip (Python package manager)

# Python Packages
pyshorteners    # URL shortening services
qrcode         # QR code generation
rich           # CLI interface
Pillow         # Image processing
pyperclip      # Clipboard management
```

### Installation Steps

#### Standard Installation

1. **Ensure Python is installed**
   ```bash
   python --version
   # Should output Python 3.7 or higher
   ```

2. **Clone the Repository**
   ```bash
   git clone https://github.com/Sumitshah00/DarkRedirect.git
   cd DarkRedirect
   ```

3. **Install Dependencies**
   ```bash
   # For Linux/macOS
   python -m pip install -r requirements.txt

   # For Windows
   python -m pip install -r requirements.txt
   ```

#### Termux Installation

```bash
# Update package list
pkg update && pkg upgrade

# Install required packages
pkg install python git

# Clone repository
 git clone https://github.com/Sumitshah00/DarkRedirect.git
 cd DarkRedirect

# Install Python dependencies
pip install pyshorteners qrcode rich Pillow pyperclip

# Run the tool
python main.py
```

### Platform-Specific Setup

#### Linux
```bash
# Debian/Ubuntu - Install Tkinter
sudo apt-get update
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install python3-tkinter
```

#### Termux (Android)
```bash
# For clipboard support
pkg install xclip

# For GUI mode (optional)
pkg install x11-repo
pkg install python-tk
```

#### macOS
```bash
# Using Homebrew
brew install python-tk
```

#### Windows
- Tkinter comes pre-installed with Python
- Ensure Python is added to PATH during installation

### Troubleshooting

1. **Missing Tkinter**
   - Error: `ModuleNotFoundError: No module named 'tkinter'`
   - Solution: Install tkinter using platform-specific commands above

2. **URL Shortener Issues**
   - Error: `Connection Error`
   - Solution: Check internet connection and firewall settings

3. **QR Code Generation Fails**
   - Error: `ImportError: No module named 'qrcode'`
   - Solution: Reinstall dependencies:
     ```bash
     pip install qrcode pillow
     ```

4. **Clipboard Operations Fail**
   - Error: `Cannot access clipboard`
   - Solution: 
     ```bash
     # For Linux
     sudo apt-get install xclip  # Debian/Ubuntu
     sudo yum install xclip      # CentOS/RHEL

     # For Termux
     pkg install xclip
     ```

### Running the Application

```bash
# Run the main application
python main.py    # Interactive menu
python cli.py     # CLI mode
python gui.py     # GUI mode
```

## Screenshots

menu:-

![Screenshot_2025-03-20_01_05_52](https://github.com/user-attachments/assets/3e360ea7-4fe0-44d9-b453-25a7fe7529f4)

cli:-

![Screenshot_2025-03-20_01_07_34](https://github.com/user-attachments/assets/d48bb511-bc91-4fed-97e5-b784caa67bc7)

gui:-

![Screenshot_2025-03-20_01_07_47](https://github.com/user-attachments/assets/3733f7c9-ca66-4c28-b31e-e204c56aa7a1)

## Security Notice

For educational and ethical testing purposes only. Users are responsible for complying with applicable laws and regulations.

## License

Created by HackSageX❤️ (Sumit Shah)

---

##  Admin Contact  
👤 **HackSageX (Sumit Shah)**  
📷 **Instagram**: [@SumitShah](https://instagram.com/hacksagex)  

---

<div align="center">
<a href="https://github.com/sumitshah00">GitHub</a> •
<a href="https://instagram.com/hacksagex">Instagram</a>
</div>
