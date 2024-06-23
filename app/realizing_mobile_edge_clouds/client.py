import socket
import time
import json
import random
import os.path

path = "/tmp/client.txt"

# import subprocess

# _ = subprocess.call("route add 10.255.255.255 dev client1-eth0", shell=True)
# _ = subprocess.call("route add 10.255.255.255 dev client1-eth1", shell=True)
# _ = subprocess.call("ifconfig client1-eth1 10.0.0.10 netmask 255.0.0.0 broadcast 10.255.255.255", shell=True)

tx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tx_socket.bind(("", 8008))  # only to prevent icmp "not reachable"



rx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#rx_socket.connect(("10.255.255.255", 8016))

cnt: int = 0
loop: int = 0
data = []
for i in range(0, 20):
    data.append(random.randint(a=0, b=1000))
_: str = ""
file = None

srv_map = {"1": "10.0.0.21", "2": "10.0.0.22", "3": "10.0.0.23", "4": "10.0.0.24"}
mig = False
print(f"starting client, {_}")
mig_index = 0
mig = False
while True:
    try:
        data, addr = tx_socket.recvfrom(4096)   # will stuck here until receive some data
        data = data.decode()
        if data == "ready":
            if not mig_index:
              print("Start...")
            else:
                 if not mig:
                    mig = True 
                    print("Migrating...")
            rx_socket.connect((addr[0], 8016))
            mig_index = mig_index + 1
        else:
            mig = False
            print(data)
        msg = "request"
        rx_socket.sendall(msg.encode())
        #time.sleep(5)
    except Exception:
        if not mig:
           print("Migrating...")


