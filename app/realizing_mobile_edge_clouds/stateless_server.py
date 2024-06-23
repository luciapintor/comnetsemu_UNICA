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
        server_data = str(count)
        rx_socket.sendto(server_data.encode(), (addr[0], 8008))
        print(count)
        count = count + 1
        time.sleep(1)
