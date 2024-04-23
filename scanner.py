import nmap
from rich.console import Console
from rich.live import Live
from scapy.all import ARP, Ether, srp

from table import create_table


def scan_network(network):
    """Perform a network scan to find devices."""
    arp_request = ARP(pdst=network)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    return srp(arp_request_broadcast, timeout=1, verbose=False)[0]


def perform_nmap_scan(ip):
    """Use nmap to get additional information about a device."""
    scanner = nmap.PortScanner()
    scan_result = scanner.scan(ip, arguments="-sn")
    try:
        if "hostnames" in scan_result["scan"][ip]:
            hostname = scan_result["scan"][ip]["hostnames"][0]["name"]
        else:
            hostname = None
    except KeyError:
        hostname = None

    try:
        vendor = (
            list(scanner[ip]["vendor"].values())[0] if scanner[ip]["vendor"] else None
        )
    except KeyError:
        vendor = None

    try:
        status = scan_result["scan"][ip]["status"]["state"]
    except KeyError:
        status = None
    return hostname, vendor, status


def main():
    network = "192.168.0.1/24"
    table = create_table()
    console = Console()

    with console.status("[bold green]Scanning Network...") as status:
        answered_list = scan_network(network)

    with Live(table, refresh_per_second=4):
        for _, response in answered_list:
            ip = response.psrc
            mac = response.hwsrc
            hostname, vendor, status = perform_nmap_scan(ip)
            table.add_row(
                ":green_circle:" if status == "up" else ":red_circle:",
                ip,
                mac,
                hostname,
                vendor,
            )


if __name__ == "__main__":
    main()
