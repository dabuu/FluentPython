# coding:utf-8
"""
@file: 9.1-5.py
@time: 6/22/2019 9:15 AM
@contact: dabuwang
"""

# region section9_1

"""
__repr__, repr() :    以便于开发者理解的方式返回对象的字符串表示形式。

__str__, str() : 　　以便于用户理解的方式返回对象的字符串表示形式。

__bytes__, bytes():    函数调用它获取对象的字节序列表示形式。

 和 __format__, format():   而 __format__ 方法会被内置的 format() 函数和 str.format() 方法调用，
                            使用特殊的格式代码显示对象的字符串表示形式。
"""

# endregion section9_1

# region section9_2     vector class
import math
from array import array


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):    # known issue: Vector(3, 4) == [3, 4]）
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # notice: memoryview(o).cast only work @ python 3.x
    # @classmethod
    # def frombytes(cls, octets):
    #     typecode = chr(octets[0])
    #     memv = memoryview(octets[1:]).cast(typecode)
    #     return cls(*memv)

# endregion vector class

# region section9_4     classmethod vs. staticmethod

class Demo:
    @classmethod
    def klassmeth(*args):
        return args, map(type, args)
    @staticmethod
    def statmeth(*args):
        return args, map(type, args) if args else ''

def section9_4():
    """
    classmethod 和 staticmethod 的行为做对比。
    classmethod 最常见的用途是定义备选构造方法
    :return:
    """
    print "Demo, type(Demo)\t", Demo, type(Demo)
    print "Demo().klassmeth()\t", Demo().klassmeth()
    print "Demo().klassmeth('spam')\t", Demo().klassmeth('spam')
    print "Demo().statmeth()\t", Demo().statmeth()
    print "Demo().statmeth('spam')\t", Demo().statmeth('spam')
# endregion section9_4

# region section9_5     格式化显示内置的 format() 函数和 str.format()


def section9_5_0x01():
    print "'{:02x}'.format(15):\t",'{:02x}'.format(15)
    print "format(31, '02x'):\t",format(31, '02x')
    print "-"*20
    print "format(1/2.43, '0.4f'):\t", format(1/2.43, '0.4f')
    print '1 BRL = {rate:0.2f} USD'.format(rate=1/2.43)
    print "-"*20
    print "format(42, 'b'):\t", format(42, 'b')
    print "format(2/3.0, '.1%'):\t", format(2/3.0, '.1%')   # 原书这里是 format(2/3, '.1%')， python2.7 fail
    print "-"*20
    from datetime import datetime
    now = datetime.now()
    print "format(now, '%H:%M:%S'):\t", format(now, '%Y-%m-%d %H:%M:%S')
    print "It's now format(now):\t{:%I:%M %p}".format(now)
    print "-"*20
    print "format_doc redict to:\thttps://docs.python.org/2/library/string.html#formatspec"

class Vector2d01(Vector2d):
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

def section9_5_0x02():
    """

    :return:
    """
    vector = Vector2d01(3,4)
    print format(vector, 'p')
    print format(vector, '.3ep')
    print format(vector, '0.5fp')
    print format(vector, '0.1f')

# endregion section9_5

if __name__ == '__main__':
    # vector = Vector2d(3, 4)
    # print repr(vector)
    # section9_4()
    section9_5_0x01()
    # section9_5_0x02()