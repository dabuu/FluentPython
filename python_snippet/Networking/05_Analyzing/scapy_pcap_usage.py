# coding:utf-8
"""
@file: scapy_pcap_usage.py
@time: 11/19/2019 10:39 PM
@contact: dabuwang
"""

from scapy.all import rdpcap, wrpcap, sniff
import os


def read_pcap_to_packets(pcap):
    if not os.path.isfile(pcap):
        return
    p_packets = rdpcap(pcap)
    print p_packets.summary()
    print p_packets.sessions()
    print p_packets.show()


def write_packet_to_pcap(pcap):
    packets = sniff(filter='tcp port 21')
    file = wrpcap(pcap, packets)


def sniff_pcap_to_packets(pcap):
    if not os.path.isfile(pcap):
        return
    p_packets = sniff(offline=pcap)


def sniff_output_format():
    sniff(filter="tcp and (port 443 or port 80)",
          prn=lambda x: x.sprintf("%.time% %-15s,IP.src% -> %-15s,IP.dst% %IP.chksum% %03xr, IP.proto% %r,TCP.flags%"))
