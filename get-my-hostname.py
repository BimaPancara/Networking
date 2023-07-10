import socket

# To get the hostname
hostname = socket.gethostname()

# Get ip addr
ip_addr = socket.gethostbyname(hostname)

# Print the hostname
print(f"Hostname = {hostname}")
print(f"IP Address = {ip_addr}")
