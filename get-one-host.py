import socket
import ipaddress
import os

ip = str("192.168.0.4")
ping_ip = os.popen(f'ping -c 4 {ip}')
ping_ip
if ("Request timed out." or "unreachable"):
    print("Unreachable")
else :
    name = socket.gethostbyaddr(ip)
    print(name)
