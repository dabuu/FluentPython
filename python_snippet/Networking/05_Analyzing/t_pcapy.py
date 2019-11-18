# coding:utf-8
"""
@file: t_pcapy.py
@time: 11/18/2019 10:29 PM
@contact: dabuwang
"""

import pcapy
from struct import *


def capture_flow():
    devs = pcapy.findalldevs()
    print(devs)
    #  device, bytes to capture per packet, promiscuous mode, timeout (ms)
    cap = pcapy.open_live("eth0", 65536 , 1 , 0)
    count = 1
    while count:
        (header, payload) = cap.next()
        print(header, payload)
        count += 1


def read_headers_from_packets():
    cap = pcapy.open_live("eth0", 65536, 1, 0)
    while 1:
        (header, payload) = cap.next()
        l2hdr = payload[:14]
        l2data = unpack("!6s6sH", l2hdr)
        srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (
        ord(l2hdr[0]), ord(l2hdr[1]), ord(l2hdr[2]), ord(l2hdr[3]), ord(l2hdr[4]), ord(l2hdr[5]))
        dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (
        ord(l2hdr[6]), ord(l2hdr[7]), ord(l2hdr[8]), ord(l2hdr[9]), ord(l2hdr[10]), ord(l2hdr[11]))
        print("Source MAC: ", srcmac, " Destination MAC: ", dstmac)
        # get IP header from bytes 14 to 34 in payload
        ipheader = unpack('!BBHHHBBH4s4s', payload[14:34])
        timetolive = ipheader[5]
        protocol = ipheader[6]
        print("Protocol ", str(protocol), " Time To Live: ", str(timetolive))