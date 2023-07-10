import socket
import ipaddress
import os

#basic_ip = 192.168.0
net4 = ipaddress.ip_network('192.168.0.0/24')
for ip in net4.hosts():
    ip_add = print(f"IP Address = {ip}")
    ip_in_str = str(ip)
    send_ping = os.popen(f'ping {ip}')
    send_ping
    if("Request timed out." or "unreachable") in send_ping:
	    print("Unreachable")
    else:
        try:
            name = socket.gethostbyaddr(ip_in_str)
            print(name)
        except:
            print("Error")
    #name = socket.gethostbyaddr(ip)
    #print(f"Name of Device = {name}")
    #print(f"name = {name}")

# To get the hostname
hostname = socket.gethostname()

# Get ip addr
ip_addr = socket.gethostbyname(hostname)

# Print the hostname
print(f"Hostname = {hostname}")
print(f"IP Address = {ip_addr}")
