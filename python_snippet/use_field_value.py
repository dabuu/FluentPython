# coding:utf-8
"""
@file: use_field_value.py
@time: 2019/1/2 9:31
@contact: dabuwang
@desc: how to get field's name and field's value in .py
"""
__author__ = 'dabuwang'

PATH = '/root/dabu'
NAME = 'dabuwang'


if __name__ == "__main__":
    print dir()
    print dir()[0]
    print eval(dir()[0])
    print __file__
