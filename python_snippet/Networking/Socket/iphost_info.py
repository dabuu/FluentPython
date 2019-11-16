# coding:utf-8
"""
@file: iphost_info.py
@time: 11/16/2019 11:42 PM
@contact: dabuwang
"""
import sys
import socket
from threading import Thread
import optparse


def socket_scan_port(host, port):
    try:
        c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # result = c_sock.connect_ex((ip,port))
        c_sock.connect((host, port))
        results = c_sock.recv(100)
        print '[+] %d/tcp open, recv result: "%s" \n' % (port, str(results))
    except:
        print '[-] %d/tcp closed \n' % port
    finally:
        c_sock.close()


def scanning_ports(host, ports):
    try:
        ip = socket.gethostbyname(host)
    except:
        print "[-] Cannot resolve '%s': Unknown host" % host
        return
    try:
        name = socket.gethostbyaddr(ip)
        print '\n[+] Scan Results for: ' + name[0]
    except:
        print '\n[+] Scan Results for: ' + ip

    for port in ports:
        t = Thread(target=socket_scan_port, args=(host, int(port)))
        t.start()


def _all_info():
    print socket.gethostbyname('qq.com')  # '111.161.64.40'

    print socket.gethostbyname_ex('qq.com')  # ('qq.com', [], ['111.161.64.40', '111.161.64.48'])

    print socket.getfqdn('qq.com')  # 'qq.com'

    print socket.gethostbyaddr('8.8.8.8')  # ('dns.google', [], ['8.8.8.8'])

    print socket.getservbyname('http')  # 80
    print socket.getservbyname('smtp', 'tcp')  # 25

    print socket.getservbyport(80)  # http
    print socket.getservbyport(23)  # telnet

    print socket.getaddrinfo('www.qq.com', socket.SOCK_STREAM)
    # [(2, 0, 0, '', ('183.192.170.139', 1)), (2, 0, 0, '', ('183.192.170.170', 1))]


def main():
    parser = optparse.OptionParser('socket_portScan -H <Host> -P <Port>')
    parser.add_option('-H', dest='host', type='string', help='specify host')
    parser.add_option('-P', dest='port', type='string', help='specify port[s] separated by comma')

    (options, args) = parser.parse_args()
    print "options: %s,\t args: %s" % (repr(options), repr(args))
    host = options.host
    ports = str(options.port).split(',')

    if (host == None) | (len(ports) == 0):
        print parser.usage
        exit(0)
    scanning_ports(host, ports)


if __name__ == '__main__':
    main()
