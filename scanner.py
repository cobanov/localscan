import argparse
import concurrent.futures

from rich.console import Console
from rich.live import Live

from table import create_table
from utils import perform_nmap_scan, scan_network


def parse_arguments():
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument(
        "--network", default="192.168.0.1/24", help="Network range to scan"
    )
    parser.add_argument(
        "--timeout", type=int, default=1, help="Timeout for ARP requests"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    table = create_table()
    console = Console(log_path="network_scan.log", log_time_format="[%X]")

    with console.status("[bold green]Scanning Network...") as status:
        answered_list = scan_network(args.network, args.timeout)

    with Live(table, refresh_per_second=4):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_ip = {
                executor.submit(perform_nmap_scan, response): response.psrc
                for _, response in answered_list
            }
            for future in concurrent.futures.as_completed(future_to_ip):
                ip = future_to_ip[future]
                try:
                    mac, hostname, vendor, status = future.result()
                    table.add_row(
                        ":green_circle:" if status == "up" else ":red_circle:",
                        ip,
                        mac,
                        hostname or "N/A",
                        vendor or "Unknown",
                    )
                except Exception as e:
                    console.log(f"Failed to scan {ip}: {e}")


if __name__ == "__main__":
    main()
