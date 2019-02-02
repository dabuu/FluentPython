# coding:utf-8
"""
@file: replace_chars_in_string_byindex.py
@time: 2019/2/2 15:40
@contact: dabuwang
@desc:
ss = 'abcdefghijklmn'
update 'abcdefghijklmn' => 'a23defghijklmn' by index

========= below is error =======
ss[1:3] = '23'
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'str' object does not support item assignment

"""

__author__ = 'dabuwang'


def replace_string_by_index():
    ss = 'abcdefghijklmn'
    print ss

    ss_bt = bytearray(ss)
    ss_bt[1:3] = '23'
    ss_replace = str(ss_bt)
    print ss_replace

if __name__ == '__main__':
    replace_string_by_index()
