import nmap
from scapy.all import ARP, Ether, srp


def scan_network(network, timeout):
    arp_request = ARP(pdst=network)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    return srp(arp_request_broadcast, timeout=timeout, verbose=False)[0]


def perform_nmap_scan(response):
    ip = response.psrc
    mac = response.hwsrc
    hostname = None
    vendor = None
    status = None

    scanner = nmap.PortScanner()
    scan_result = scanner.scan(ip, arguments="-sn")

    try:
        hostname = scan_result["scan"][ip]["hostnames"][0].get("name", None)
        vendor = (
            list(scan_result["scan"][ip].get("vendor", {}).values())[0]
            if scan_result["scan"][ip].get("vendor")
            else None
        )
        status = scan_result["scan"][ip]["status"]["state"]
    except KeyError as e:
        print(f"Error scanning {ip}: {e}")

    return mac, hostname, vendor, status
