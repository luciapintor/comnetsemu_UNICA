#!/usr/bin/python

"""
Description

ensure that mininet is configured to only assign IPv4 addresses to Hosts,
see: https://github.com/mininet/mininet/issues/454
"""

import time
import socket

from comnetsemu.net import Containernet
from comnetsemu.cli import CLI
from comnetsemu.node import DockerHost, APPContainer

from mininet.node import RemoteController
from mininet.log import setLogLevel, info
from mininet.link import TCLink  # import last to avoid collision


def start() -> None:
    net = Containernet(build=False, controller=RemoteController, link=TCLink, xterms=False)
    cnt: int = 0
    active_container: bool = False
    full_tree: bool = False

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info("\n*** Adding Hosts\n")
    h1: DockerHost = net.addDockerHost(
        "h1",
        dimage="simple_host",
        ip="10.0.0.1/24",
        mac="00:00:00:00:00:01",
        docker_args={"volumes": {"/tmp": {"bind": "/tmp", "mode": "rw"}}},
    )
    h2: DockerHost = net.addDockerHost(
        "h2",
        dimage="simple_host",
        ip="10.0.0.2/24",
        mac="00:00:00:00:00:02",
        docker_args={"cpuset_cpus": "0", "cpu_quota": 25000},
    )
    h3: DockerHost = net.addDockerHost(
        "h3",
        dimage="simple_host",
        ip="10.0.0.3/24",
        #mac="00:00:00:00:00:03",
        docker_args={"cpuset_cpus": "0", "cpu_quota": 25000},
    )

    info("\n*** Adding Switches\n")
    s1 = net.addSwitch("s1")
    

    info("\n*** Adding Links\n")
    net.addLink(node1=s1, node2=h1)
    net.addLink(node1=s1, node2=h2)
    net.addLink(node1=s1, node2=h3)
    #net.addLink(node1=switch1, node2=probe1, delay="50ms", use_htb=True)
    
    info("\n*** Starting Network\n")
    net.build()   # totology
    net.start()

    time.sleep(3)


    # time.sleep(2)
    CLI(net)
    
    info("\n*** Stopping Network\n")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    start()

