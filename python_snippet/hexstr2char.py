# coding:utf-8
"""
@file: hexstr2char.py
@time: 2019/1/24 14:33
@contact: dabuwang
@desc:

want to transfer | 00 EF| = \x00\xef

"""
__author__ = 'dabuwang'

def hex2char_itiswrong():
    input_str1 = '00'
    input_str2 = 'FF'

    print chr(int(input_str1, 16))
    print repr(chr(int(input_str1, 16)))

    print chr(int(input_str2, 16))
    print repr(chr(int(input_str2, 16)))

def str2hex():
    input_str = '00'
    hex_value= input_str.decode('hex')
    print "input_str:{0}, convert to hex: {1}, repr val: {2}".format(input_str, hex_value, repr(hex_value))

def hexstr2int():
    hex_str = "AF"
    hex_int = int(hex_str, 16)
    print "hex_str:'{0}', convert to int: {1}".format(hex_str, hex_int)

def int2hexstr():
    import random
    rint = random.randint(0,255)
    hex_str = '{:02x}'.format(rint)
    print "rint:'{0}', convert to hex: {1}".format(rint, hex_str)


if __name__ == '__main__':
    # str2hex()
    # hexstr2int()
    int2hexstr()