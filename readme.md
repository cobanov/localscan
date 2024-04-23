# LocalScan

This Python script scans a specified network range to identify active devices and gather information about them.

![image](assets/demo.png)

**Usage**

```bash
python network_scanner.py --network <network_range> [--timeout <timeout_seconds>]
```

- Replace `<network_range>` with the IP address range to scan (e.g., `192.168.0.1/24`).
- The `--timeout` option (optional) allows you to adjust the timeout for ARP requests in seconds (defaults to 1 second).

## Install

nmap should be installed

### Windows

```plain
https://nmap.org/download.html#windows
```

### MacOS

```bash
brew install nmap
```

## To-do

- [ ] Better colorization
- [ ] Fix hostname problem
- [ ] Refresh table with "R" key
- [ ] Refresh automatically every n second
- [ ] Remove nmap logging error



## Disclaimer

This script is intended for educational purposes and penetration testing with proper authorization. It's crucial to respect network security and only scan networks you have permission to access.
