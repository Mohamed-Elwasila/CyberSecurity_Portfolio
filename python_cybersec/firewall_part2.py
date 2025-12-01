# DoS Blocker
import os
import sys
import time
from collections import defaultdict
from scapy.all import sniff, IP

THRESHOLD = 1500  # packets per second

packet_count = defaultdict(int)
start_time = time.time()
blocked_ips = set()

def packet_callback(packet):
    global start_time

    if IP not in packet:
        return

    src_ip = packet[IP].src
    packet_count[src_ip] += 1

    current_time = time.time()
    time_interval = current_time - start_time

    # Check every 1 second
    if time_interval >= 1:
        for ip, count in list(packet_count.items()):
            packet_rate = count / time_interval

            if packet_rate > THRESHOLD and ip not in blocked_ips:
                print(f"[!] Blocking IP: {ip}    rate: {packet_rate}")
                os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
                blocked_ips.add(ip)

        # RESET properly
        packet_count.clear()
        start_time = current_time

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Run as root!")
        sys.exit(1)

    print(f"THRESHOLD: {THRESHOLD}")
    print("Monitoring network traffic...")
    sniff(filter="ip", prn=packet_callback)
