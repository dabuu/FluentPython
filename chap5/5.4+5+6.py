# coding:utf-8
"""
@file: 5.4+5+6.py
@time: 2/10/2019 6:14 PM
@contact: dabuwang
@content:
5.4: callable object
5.5 callable objects which user custom
"""

# region 5.4  total 7 SEVEN callable objects
"""
用户定义的函数:   使用 def 语句或 lambda 表达式创建。

内置函数:   使用 C 语言（CPython）实现的函数，如 len 或 time.strftime。

内置方法:   使用 C 语言实现的方法，如 dict.get。

方法:     在类的定义体中定义的函数。

类：      调用类时会运行类的 __new__ 方法创建一个实例，然后运行 __init__ 方法，初始化实例，最后把实例返回给调用方。因为 Python 没有 new 运算符，所以调用类相当于调用函数。（通常，调用类会创建那个类的实例，不过覆盖 __new__ 方法的话，也可能出现其他行为。19.1.3 节会见到一个例子。）

类的实例：  如果类定义了 __call__ 方法，那么它的实例可以作为函数调用。参见 5.5 节。

生成器函数：  使用 yield 关键字的函数或方法。调用生成器函数返回的是生成器对象。
（生成器函数在很多方面与其他可调用对象不同，详情参见第 14 章。生成器函数还可以作为协程，详情参见第 16 章。）

"""
# endregion

# region 5.5 user custom the callable objects
"""
需要实现 __call__ 方法
"""
import random

class BingoCage:

    def __init__(self, items):
        self.i_items = list(items)
        random.shuffle(self.i_items)    # shuffle 把list中元素打乱

    def pick(self):
        try:
            return self.i_items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

def test55():
    bingo = BingoCage(range(3))
    print bingo.i_items
    print "bingo.pick()", bingo.pick()
    print bingo.i_items
    print "call bingo()", bingo()
    print bingo.i_items
# endregion

# region 5.6 函数内省
"""
*下面重点说明函数专有而用户定义的一般对象没有的属性。*
"""
class C():
    pass
def func():
    pass

def test56():
    c_obj = C()
    print dir(func)
    print dir(c_obj)
    print '=========='
    print sorted(set(dir(func)) - set(dir(c_obj)))

    print "python2.7 运行的结果 跟书中的不一致，可能是python版本的缘故，主要是展示 用户自定义的对象 不包括哪些属性"

# endregion

if __name__ == '__main__':
    # test55()
    test56()
