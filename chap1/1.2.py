# coding:utf-8
"""
@file: 1.2.py
@time: 2018/8/16 10:02
@contact: dabuwang
"""
__author__ = 'dabuwang'

from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x , self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


def test():
    v1 = Vector(2,4)
    v2 = Vector(2,1)
    print v1+v2

    v3 = Vector(3,4)
    print "v3: %r" % v3
    print "abs(v3) result: %r" % abs(v3)
    print "(v3 * 2) result: %s" % (v3 * 2)  # dabu:  "% vs. *", % is same as * , so % operator will run firstly if without ()
    print "bool(v3) result: %s" % bool(v3)


if __name__ == '__main__':
    test()