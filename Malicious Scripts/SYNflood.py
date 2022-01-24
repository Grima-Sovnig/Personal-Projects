from scapy.all import *


# Target IP (Can be a router or a specific machine), required to be manually entered as of now.
target_ip = "192.168.1.1"
# Target Port (Here are some common ports: 20,21=FTP, 80=HTTP, 443=HTTPS, 3389=RDP)
target_port = 80

# This creates a packet with the target IP as the destination IP address
ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)


