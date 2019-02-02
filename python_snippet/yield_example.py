# coding:utf-8
"""
@file: yield_example.py
@time: 2018/12/3 11:52
@contact: dabuwang
@desc: test keyword: yield
https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/
https://www.pythoncentral.io/python-generators-and-yield-keyword/
"""
__author__ = 'dabuwang'

def cg():
    for x in range(4):
        try:
            yield x/(2-x)
        except:
            continue

def test_yield():
    for y in cg():
        print ""
        print y

if __name__ == '__main__':
    test_yield()