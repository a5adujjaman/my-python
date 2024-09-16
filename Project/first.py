import scapy.all as scapy
from scapy.layers.inet import IP, ICMP, TCP
import socket

def scan_network(ip_range):
    print(f"Scanning network: {ip_range}")
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices = []
    for element in answered_list:
        device_info = {
            "ip": element[1].psrc,
            "mac": element[1].hwsrc
        }
        devices.append(device_info)

    return devices

def scan_ports(ip):
    print(f"Scanning ports for IP: {ip}")
    open_ports = []
    for port in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
    except:
        service_name = "Unknown"

    return service_name

def main(ip_range):
    devices = scan_network(ip_range)
    for device in devices:
        print(f"IP: {device['ip']} \t MAC: {device['mac']}")
        open_ports = scan_ports(device['ip'])
        if open_ports:
            print("Open Ports:")
            for port in open_ports:
                service = get_service_name(port)
                print(f"Port {port}: {service}")
        else:
            print("No open ports found.")
        print("\n")

if __name__ == "__main__":
    ip_range = "192.168.0.1/24"  # Modify this based on your network range
    main(ip_range)
