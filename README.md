<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmYxeW5ibnNndDZ3ZWkzODNzNGd5bGxndDV0eGN6Zm81OTFwM2U5eiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/tHIRLHtNwxpjIFqPdV/giphy.gif" alt="DarkRedirect Logo" width="150" height="150" style="border-radius: 50%; background: transparent; object-fit: cover;"/>
  
  # DarkRedirect🚀
  
  **A sophisticated URL masking and redirection tool with both CLI and GUI interfaces**
  
  [![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://github.com/hacksagex/darkredirect)
</div>

## Overview

DarkRedirect is a versatile URL manipulation tool designed for security researchers and developers. It provides powerful URL masking capabilities through both command-line and graphical interfaces, making it suitable for various use cases from penetration testing to legitimate URL management.

## Key Features

- **Dual Interface**: Choose between an intuitive GUI or efficient CLI
- **Multiple URL Shorteners**: Support for TinyURL, DAGD, and Clck.ru
- **QR Code Generation**: Instantly create QR codes for masked URLs
- **Custom Domain Masking**: Personalize your redirects with custom domains
- **History Tracking**: Built-in logging of all URL operations
- **URL Validation**: Robust checking of input URLs
- **Cross-Platform**: Works on Windows, Linux, macOS, and Android (Termux)

## System Requirements

### Minimum Specifications
- Python 3.7 or higher
- Active internet connection
- 50MB free disk space
- Basic terminal knowledge for CLI mode

### Supported Operating Systems
- Windows 10/11
- Linux (All major distributions)
- macOS 10.15+
- Android via Termux

## Installation Guide

### Quick Start

```bash
# Clone the repository
git clone https://github.com/Sumitshah00/DarkRedirect.git
cd DarkRedirect

# Install dependencies
python -m pip install -r requirements.txt

# Launch the application
python main.py
```

### Platform-Specific Setup

#### Windows
```bash
# Install Python from python.org
# Ensure Python is added to PATH during installation
python -m pip install -r requirements.txt
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-tk
pip3 install -r requirements.txt
```

#### Termux (Android)
```bash
pkg update && pkg upgrade
pkg install python git
pip install -r requirements.txt
```

#### macOS
```bash
# Using Homebrew
brew install python
pip3 install -r requirements.txt
```

## Usage Modes

### Interactive Menu
```bash
python main.py
```

### Command Line Interface
```bash
python cli.py
```

### Graphical Interface
```bash
python gui.py
```

## Screenshots

menu:-

![Screenshot_2025-03-20_01_05_52](https://github.com/user-attachments/assets/3e360ea7-4fe0-44d9-b453-25a7fe7529f4)

cli:-

![Screenshot_2025-03-20_01_07_34](https://github.com/user-attachments/assets/d48bb511-bc91-4fed-97e5-b784caa67bc7)

gui:-

![Screenshot_2025-03-20_01_07_47](https://github.com/user-attachments/assets/3733f7c9-ca66-4c28-b31e-e204c56aa7a1)

## Troubleshooting

### Common Issues

1. **Module Not Found Errors**
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

2. **Permission Denied**
   ```bash
   # Linux/macOS
   sudo pip3 install -r requirements.txt
   ```

3. **Tkinter Missing**
   - Windows: Reinstall Python with Tkinter option
   - Linux: `sudo apt install python3-tk`
   - Termux: `pkg install x11-repo && pkg install python-tk`

## Security Notice

This tool is intended for educational and ethical testing purposes only. Users are responsible for complying with applicable laws and regulations. The developers assume no liability for misuse.

## License

Created by HackSageX❤️ (Sumit Shah)
---

##  Contact Information
🧑🏽‍💻 **HackSageX (Sumit Shah)**  
📷 **Instagram**: [@SumitShah](https://instagram.com/hacksagex)  

---

<div align="center">
<a href="https://github.com/sumitshah00">GitHub</a> •
<a href="https://instagram.com/hacksagex">Instagram</a>
</div>
