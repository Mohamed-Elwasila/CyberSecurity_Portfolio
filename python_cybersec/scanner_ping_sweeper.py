import sys
from scapy.all import ICMP, IP, SR1

def ping_sweep(network, netmask):
    live_hosts = []
    total_hosts  = 0
    snanned_hosts = 0

    ip)network = IPNetwork(network + '/' + netmask)
    for host in ip_network.iter_hosts():
        total_hosts += 1

    for host in ip_network.iter_hosts():
        scanned_hosts += 1
        print
              
