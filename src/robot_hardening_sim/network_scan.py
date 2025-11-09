# src/robot_hardening_sim/network_scan.py
import socket

def check_open_ports(ip_address, ports=(22, 80, 443)):
    results = {}
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.connect((ip_address, port))
            results[port] = "open"
        except Exception:
            results[port] = "closed"
        finally:
            sock.close()
    return results
