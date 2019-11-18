# coding:utf-8
"""
@file: udp_client.py
@time: 11/16/2019 11:15 PM
@contact: dabuwang
"""

import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT = 6789
buf = 4096
address = (UDP_IP_ADDRESS, UDP_PORT)
socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = raw_input('?: ').strip()
    socket_client.sendto("%s" % message, address)
    response, addr = socket_client.recvfrom(buf)
    print "=> %s" % response
    if message == "quit":
        break
socket_client.close()
