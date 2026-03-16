#!/usr/bin/env python

"""
Simple example of building a single switch topology
"""

from sys import argv

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI


net = Mininet(controller=Controller)
net.addController('c0')

#  netwrok devices
s1=net.addSwitch("s1")
#  netwrok devices
s2=net.addSwitch("s2")

h1=net.addHost("h1")
net.addLink(s1,h1)

h2=net.addHost("h2")
net.addLink(s1,h2)

net.start()

CLI(net)
net.stop()