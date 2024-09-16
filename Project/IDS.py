import scapy.all as scapy
from collections import defaultdict

# Threshold for packet count from a single IP to consider it suspicious
PACKET_THRESHOLD = 100

# Dictionary to keep track of packet counts from each IP
ip_packet_count = defaultdict(int)

def detect_attack(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_packet_count[ip_src] += 1

        if ip_packet_count[ip_src] > PACKET_THRESHOLD:
            print(f"Potential DoS attack detected from IP: {ip_src}")

def start_sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=detect_attack)

if __name__ == "__main__":
    network_interface = "eth0"  # Change this to the correct network interface
    print(f"Starting IDS on {network_interface}...")
    start_sniffing(network_interface)
