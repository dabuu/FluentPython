# coding:utf-8
"""
@file: udp_server.py
@time: 11/16/2019 11:15 PM
@contact: dabuwang
"""

import socket, sys

buf = 4096
host = "127.0.0.1"
port = 6789
address = (host, port)
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server.bind(address)

while True:
    data, addr = socket_server.recvfrom(buf)
    data = data.strip()
    print "received from: ", addr
    print "message: ", data
    try:
        response = "Hi %s" % sys.platform
    except Exception, e:
        response = "%s" % sys.exc_info()[0]
    print "Response", response
    socket_server.sendto("%s " % response, addr)
    if 'quit' in data:
        break
socket_server.close()
