# Cybersecurity Learning Journey
<p align="center">
  <img src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Go-00ADD8?logo=go&logoColor=white">
  <img src="https://img.shields.io/badge/Networking-0078D4?logo=cisco&logoColor=white">
  <img src="https://img.shields.io/badge/Nmap-004170?logo=linux&logoColor=white">
  <img src="https://img.shields.io/badge/Wireshark-1679A7?logo=wireshark&logoColor=white">
  <img src="https://img.shields.io/badge/Tcpdump-000000?logo=linux&logoColor=white">
  <img src="https://img.shields.io/badge/Gobuster-FF6F00?logo=apache&logoColor=white">
  <img src="https://img.shields.io/badge/Hydra-2F855A?logo=linux&logoColor=white">
</p>

This repository documents my progress in cybersecurity, including CTF writeups, TryHackMe learning paths, tool notes, and Python scripts for automation or security tasks.

## Professional Statement
### Summary
I'm currently building my Cybersecurity Portfolio by documenting everything I learn — from CTFs and TryHackMe labs to Python automation scripts and tool development.
My goal is to develop strong, practical foundations in:
- Penetration Testing
- Network Security
- SOC Analysis
- Threat Detection
- Python-based security automation

### Skills
- Linux • Bash • Python • Go
- Networking • SysAdmin Fundamentals
- Nmap • Wireshark • Tcpdump • Gobuster • Hydra

### Interests
Cybersecurity, Ethical Hacking, CTFs, SOC Operations, Python Automation, Cloud Security, Open-Source Tools.

---

## Learning Workflow (My Steps)

### 1. Enumeration
- Gather information
- Tools: `nmap`, `gobuster`, `curl`, `whatweb`
- Notes:
  - Look for open ports
  - Check services + versions
  - Find hidden directories

### 2. Exploitation
- Identify what can be used to gain access
- Common checks:
  - Default credentials
  - Hidden scripts/files
  - Vulnerable versions
  - Misconfigurations

### 3. Privilege Escalation
- Linux: `sudo -l`, SUID, capabilities, cron jobs
- Windows: systeminfo, weak permissions
- Tools I use: `linpe.sh`, `winPEAS`, manual checks

### 4. Post-Exploitation
- Stabilize shell
- Explore file system
- Document findings

---

## Tool Notes (Quick Commands)

### Nmap
nmap -sV -sC <target>
nmap -A <target>


### Gobuster



(More tools will be added as I learn them.)

---

## CTF Writeups

- `Pickle Rick (THM)` – *in progress*
- More coming soon...



---

## Python Automation
- Small scripts I build to automate recon, scanning, or enumeration.
- Examples:
  - Port scan wrapper
  - Directory fuzzing automation
  - Log parser

---

## Goals
- Build a strong habit of documenting what I learn.
- Complete multiple TryHackMe paths.
- Build and publish small security tools in Python.

