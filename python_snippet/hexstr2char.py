# coding:utf-8
"""
@file: hexstr2char.py
@time: 2019/1/24 14:33
@contact: dabuwang
@desc:

want to transfer | 00 EF| = \x00\xef

"""
__author__ = 'dabuwang'

def hex2char():
    input_str1 = '00'
    input_str2 = 'FF'

    print chr(int(input_str1, 16))
    print repr(chr(int(input_str1, 16)))

    print chr(int(input_str2, 16))
    print repr(chr(int(input_str2, 16)))


if __name__ == '__main__':
    hex2char()