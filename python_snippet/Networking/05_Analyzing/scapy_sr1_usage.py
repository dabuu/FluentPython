# coding:utf-8
"""
@file: scapy_sr1_usage.py
@time: 11/19/2019 10:13 PM
@contact: dabuwang
"""

from scapy.all import sr1, IP, TCP, UDP

"""
the usage is for sr1
"""


OPEN_PORTS = []

def analyze_port(host, port):
    """
    Function that determines the status of a port: Open / closed
    :param host: target
    :param port: port to test
    :type port: int
    """
    print "[ii] Scanning port %s" % port
    res = sr1(IP(dst=host) / TCP(dport=port), verbose=False, timeout=0.2)
    if res is not None and TCP in res:
        if res[TCP].flags == 18:
            OPEN_PORTS.append(port)
            print "Port %s open" % port


def analyze_port_test():
    for x in xrange(0, 80):
        analyze_port("domain", x)
    print "[*] Open ports:"
    for x in OPEN_PORTS:
        print " - %s/TCP" % x


def traceroute_domain(hostname="google.com"):
    for i in range(1, 28):
        pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
        # Send package and wait for an answer
        reply = sr1(pkt, verbose=0)
        if reply is None:
            # No reply
            print "No reply"
            break
        elif reply.type == 3:
            # the destination has been reached
            print "Done!", reply.src
            break
        else:
            # We’re in the middle communication
            print "%d hops away: " % i, reply.src


if __name__ == '__main__':
    analyze_port_test()
