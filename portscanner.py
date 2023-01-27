import socket
import argparse
from datetime import datetime

def port_scanner(host, start_port, end_port):
    """Scans a host for open ports in a given range."""
    open_ports = []
    for port in range(start_port, end_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
            print(f"[+] Port {port} is open")
        else:
            print(f"[-] Port {port} is closed or filtered")
        sock.close()
    return open_ports

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("host", help="Hostname or IP address to scan")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start of port range (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=65535, help="End of port range (default: 65535)")
    args = parser.parse_args()

    host = args.host
    start_port = args.start
    end_port = args.end

    print(f"[*] Scanning {host} for open ports...")
    start_time = datetime.now()
    open_ports = port_scanner(host, start_port, end_port)
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"[*] Scan complete in {total_time}")
    print(f"[*] Open ports on {host}: {open_ports}")
