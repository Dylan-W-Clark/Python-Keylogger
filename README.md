# Python-Keylogger

This Repo demonstrates how to build a custom keylogger using Python, documenting the technical implementation, development process, and key learnings. It also explores the legitimate use cases of keyloggers in cybersecurity, including threat analysis, penetration testing, and defensive security research.


---
⚠️ **DISCLAIMER: EDUCATIONAL AND RESEARCH PURPOSES ONLY**

This project is developed strictly for cybersecurity education, authorised security testing, and research purposes. It is intended to help security professionals, students, and researchers understand how keyloggers work and how to defend against them.

⚠️ **LEGAL WARNING**: Unauthorised use of keylogging software is illegal in most jurisdictions. Using this tool to monitor individuals without their explicit consent or on systems you do not own or have authorisation to test may result in criminal charges and civil liability.

⚠️ **By using this code, you agree to:**
- Only use it on systems you own or have explicit written authorisation to test
- Comply with all applicable local, state, and federal laws
- Take full responsibility for your actions
- Use it solely for legitimate security research and educational purposes

⚠️ **The author(s) of this repository assume no liability for misuse of this software.**

---

# Keylogger Benefits:

- **Threat analysis** - Understand attack vectors and malware behavior patterns

- **Security testing** - Conduct penetration testing and vulnerability assessments on authorised systems

- **Incident response** - Investigate security breaches and trace attacker activities

- **Security awareness training** - Demonstrate real-world threats to educate users and organizasions

- **Honeypot deployment** - Monitor attacker behavior in controlled environments to gather threat intelligence

- **Forensic analysis** - Collect evidence during digital investigations with proper authorisation

- **Defensive development** - Build and test anti-keylogging technologies and endpoint protection solutions

# 📝Walkthrough:

## Step 1 - Prerequisites

### Environment Setup

**Create a project directory**
```bash
mkdir python-keylogger
cd python-keylogger
```

**Set up a virtual environment**

Creating a virtual environment is recommended to isolate dependencies and maintain a clean development environment.
```bash
python -m venv venv
```

**Activate the virtual environment**

- **Windows:**
```bash
  venv\Scripts\activate
```
- **macOS/Linux:**
```bash
  source venv/bin/activate
```

**Install required dependencies**
```bash
pip install pynput
```

### Verify Installation

Confirm that `pynput` is installed correctly:
```bash
py -m pip list
```

You should see `pynput` listed among the installed packages.

## Step 2 - Create and Configure the Script

### Create the Python File

Open your preferred code editor (e.g., VS Code, Sublime Text) in the project directory and create a new Python file for the keylogger:
```bash
keylogger.py
```

### Write the Script

Refer to the `keylogger.py` file in this Repo for the complete implementation/information. The script will demonstrate the core functionality of keyboard event monitoring using the `pynput` library.

### 🔏Antivirus Considerations

**Important**: Legitimate keyloggers will often trigger antivirus software, as their behavior is similar to malicious keyloggers.

Before running the script on your own system:

1. **Add an exception** in your antivirus/Windows Defender settings for your project directory
2. **Whitelist the script** to prevent it from being quarantined or deleted
3. **Understand the risks** - only do this in a controlled environment for authorised testing!

## Step 3 - Testing the Keylogger

### Activate the Virtual Environment

Ensure your virtual environment is active before running the script:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Run the Keylogger

Execute the script:
```bash
python keylogger.py
```

### Verify Functionality

1. **Monitor the console output** - You should see keyboard events being captured in real-time as you type
2. **Open a browser or text editor** and type some test phrases
3. **Check the output file** - A log file (e.g., `keylog.txt`) should be created in your project directory containing all captured keystrokes

### Expected Results

- Real-time keystroke data appearing in the terminal
- A text file generated with logged keyboard input
- Timestamps (if implemented) showing when keys were pressed

### Stop the Keylogger

Press `Ctrl + C` in the terminal to terminate the script.

---

**Success!** You've successfully built and tested a functional keylogger for educational purposes.
