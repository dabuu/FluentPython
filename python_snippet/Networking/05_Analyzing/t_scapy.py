# coding:utf-8
"""
@file: t_scapy.py
@time: 11/18/2019 10:36 PM
@contact: dabuwang
"""

from scapy.all import *


def print_packet(packet):
    ip_layer = packet.getlayer(IP)
    print("[!] New Packet: {src} -> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))


def packet_sniff(interface="eth0"):
    print("[*] Start sniffing...")
    # sniff(iface="eth0", filter="tcp", prn=lambda x: x.summary())
    sniff(iface=interface, filter="ip", prn=print_packet)
    print("[*] Stop sniffing")

# custom custom packet sniffer action method
def sniffPackets(packet):
    if packet.haslayer(IP):
        pckt_src=packet[IP].src
        pckt_dst=packet[IP].dst
        pckt_ttl=packet[IP].ttl
        print "IP Packet: %s is going to %s and has ttl value %s" (pckt_src,pckt_dst,pckt_ttl)

def main():
    print "custom packet sniffer"
    #call scapy’s sniff method
    sniff(filter="ip",iface="wlan0",prn=sniffPackets)

def arpDisplay(pkt):
    if pkt[ARP].op == 1: #request
       x= "Request: {} is asking about {} ".format(pkt[ARP].psrc,pkt[ARP].pdst)
       print x
    if pkt[ARP].op == 2: #response
        x = "Response: {} has address {}".format(pkt[ARP].hwsrc,pkt[ARP].psrc)
        print x

def arp_sniff():
    sniff(filter="ARP", prn=arpDisplay, store=0, count=10)


DNS_QUERIES=0
def count_dns_request(package):
   global DNS_QUERIES
   if DNSQR in package:
       DNS_QUERIES +=1

def udp_sniff():
    sniff(filter="UDP and port 53", count=100, prn=count_dns_request)