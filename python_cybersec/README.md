# Python Cybersecurity Scripts

## 1. firewall_part1
### Basic firewall rule checker with IP address validation
A simple demonstration script that generates random IP addresses and checks them against predefined firewall rules.

### Usage
```bash
python firewall_part1.py
```

---
## 2. firewall_part2
### Real-time DoS attack detection and automatic IP blocking system
A real-time network traffic monitoring tool that detects and blocks potential DoS attacks by analyzing packet rates from source IP addresses.

### Requirements
- Root/sudo privileges
- Python 3.x
- Scapy library

### Usage
```bash 
sudo python firewall_part2.py
```
---
## 3. scanner_ping_sweeper.py
### Ping sweeper, a simple tool which can scan a subnet and return a list of live hosts.

```bash 
sudo -E python scanner_ping_sweeper.py <IP address: ex. (127.0.0.1)> <Subnet: ex. (24)>
```
