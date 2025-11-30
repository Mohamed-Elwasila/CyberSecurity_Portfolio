# Cybersecurity Learning Journey

This repository documents my progress in cybersecurity, including CTF writeups, TryHackMe learning paths, tool notes, and Python scripts for automation or security tasks.

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

*(Flags are never published.)*

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

