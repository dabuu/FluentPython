# coding:utf-8
"""
@file: get_option.py
@time: 2019/1/9 10:08
@contact: dabuwang
@desc:

getopt vs. argparse


-- getopt
    refer:  1. https://pymotw.com/2/getopt/
            2. https://docs.python.org/2/library/getopt.html

    [short term]   abc:d:e, meaning: "c & d" with specific input info,  a / b / e just switch(without specific input)
    [long term]    ["version", 'output='],  meaning:  version is switch ;  ""

    "gnu_getopt" is same as getopt, This means that option and non-option arguments may be intermixed.

-- argparse
    refer:  1. https://docs.python.org/2/library/argparse.html#module-argparse

    usage is more complex, not do example here
"""
__author__ = 'dabuwang'

import sys
import getopt


def getopt_eg_short(argv):
    try:
        opts, args = getopt.getopt(argv, "hl:i:")
        print opts
        print args
    except getopt.GetoptError as ex:
        print "Warning: GetoptError %s" % ex

def getopt_eg_long(argv):
    try:
        opts, args = getopt.getopt(argv, "", ["version", 'output='])
        print opts
        print args
    except getopt.GetoptError as ex:
        print "Warning: GetoptError %s" % ex

if __name__ == '__main__':
    # main(sys.argv[1:])
    short_argv = "-h -i interface -l 1.1.1.1 2.2.2.2".split()
    # short_argv = '-a -b -cfoo -d bar a1 a2'.split()
    getopt_eg_short(short_argv)

    long_argv = "--version --output a".split()
    getopt_eg_long(long_argv)