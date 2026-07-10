"""

DESCRIPTION

    TODO In order to use this script you provide the code with the IP address of the target device that you wish to scan for any open ports

EXAMPLES

    TODO: For example I might put down the IP address 192.168.15.13 and run a scan for port 1-400

AUTHOR

    TODO: Lindsay Coudert 30082098@tafe.wa.edu.au

LICENSE

    This script is the exclusive and proprietary property of
    TiO2 Minerals Consultants Pty Ltd. It is only for use and
    distribution within the stated organisation and its
    undertakings.

VERSION

    $Id$
"""

import sys
from scapy.all import *

def port_scan(target, ports):
    for port in ports:
        response = sr1(IP(dst="192.168.15.13")/TCP(dport=[21, 22, 23, 53, 80, 110, 135, 137, 138, 139, 443, 1433, 1434, 8080], flags="S"), timeout=1, verbose=0)
        if response is None:
            print(f"Port {port} on {target} is filtered or closed")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            print(f"Port {port} on {target} is open")
        else:
            print(f"Port {port} on {target} is closed")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <target_IP> <starting_port>-<ending_port>")
        sys.exit(1)

    if not sys.stdin.isatty():
        print("Please run this script in a PowerShell prompt.")
        sys.exit(1)

    target = sys.argv[1]
    ports = sys.argv[2].split('-')
    starting_port = int(ports[0])
    ending_port = int(ports[1])

    port_scan(target, range)
