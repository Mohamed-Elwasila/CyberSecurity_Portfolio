# 
import os
import sys 
import time 
from collections import defaultdict
from scapy.all import sniff, IP, TCP

THRESHOLD = 40
print(f"THRESHOLD: {THRESHOLD}")

def read_ip_file(filename):
    """Read IP function"""
    with open(filename, "r" ) as file: # open the file in read mode
        ips = [line.strip() for line in file]
    return set(ips)

def is_nimda_worm(packet):
    if packet.haslayer(TCP) and packet[TCP].payload
    return "GET /scripts/root.exe" in str(payload)
return False


