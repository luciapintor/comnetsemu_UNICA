import socket
import time
import json
import random
import cmath
from typing import List

import os.path
import re

path = "/tmp/server.txt"

# import select
# try:
#     import numpy as np
# except:
#     pass


# def fft(x=None):  # @TODO : check if ledgit
#     """perform dft"""
#     N = x.size
#     n = np.arange(N)
#     k = n.reshape((N, 1))
#     e = np.exp(-2j * np.pi * k * n / N)
#     return np.dot(e, x)


rx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
rx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
rx_socket.bind(("", 8016))

# actual rx for data
#actual_rx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#rx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#rx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#actual_rx_socket.bind(("", 8098))


client = "10.0.0.10"

count = 0
print("starting server")
while True:
        if not count:
           msg = "ready"
           rx_socket.sendto(msg.encode(), (client, 8008))
        raw_data, addr = rx_socket.recvfrom(1024)
        if not count:
            # in case of migration
            if os.path.isfile(path):
                 state_file = open("/tmp/server.txt", "r")
                 last_line = state_file.readlines()[-1]
                 count = int(re.findall("\d+", last_line)[0])
                 count = count + 1
        server_data = str(count)
        rx_socket.sendto(server_data.encode(), (addr[0], 8008))
        try: 
           if not os.path.isfile(path):
               file = open("/tmp/server.txt", "w")
           else:
               file = open("/tmp/server.txt", "a")
           file.write(server_data +  "\n")
           file.close()
        except Exception:
               pass
        print(count)
        count = count + 1
        time.sleep(1)
