# coding:utf-8
"""
@file: 8.5-7.py
@time: 6/19/2019 10:36 PM
@contact: dabuwang
"""
import weakref


# region section8_5 del和垃圾回收
def bye(o):
    print('Gone with the wind...: ', repr(o))


def section8_5():
    """
    对象绝不会自行销毁；然而，无法得到对象时，可能会被当作垃圾回收。
    > del 语句删除名称，而不是对象。
    > del 命令可能会导致对象被当作垃圾回收，但是仅当删除的变量保存的是对象的最后一个引用，或者无法得到对象时。
    > 重新绑定也可能会导致对象的引用数量归零，导致对象被销毁。
    :return:
    """
    s1 = {1, 2, 3}
    s2 = s1

    ender = weakref.ref(s2, bye)
    print "ender: ", ender
    del s1
    print "-" * 10
    print "ender: ", ender
    print "-" * 20
    s2 = "spam"
    print "-" * 30
    print "ender: ", ender


# endregion section8_5 del和垃圾回收

# region section8_6 弱引用
def section8_6_0x01():
    """
    >>>import weakref
    >>>a_set = {0, 1}
    >>>wref = weakref.ref(a_set)
    >>>wref()   # 调用 wref() 返回的是被引用的对象，{0, 1}。因为这是控制台会话，所以 {0, 1} 会绑定给 _ 变量。
    set([0, 1])
    >>>a_set = {2,3}
    >>>wref()
    set([0, 1])
    >>>wref() is None
    False
    >>>wref() is None
    True
    :return:
    weakref 模块的文档指出，weakref.ref 类其实是低层接口，供高级用途使用，多数程序最好使用 weakref 集合和 finalize。
    也就是说，应该使用 WeakKeyDictionary、WeakValueDictionary、WeakSet 和 finalize（在内部使用弱引用），
    不要自己动手创建并处理 weakref.ref 实例。
    """

    print "code work only @ console, not script"
    a_set = {0, 1}
    wref = weakref.ref(a_set)
    print "a_set: ", a_set
    print "wref(): ", wref()
    a_set = {2, 3, 4}
    print "set another value: ", a_set
    print "wref(): ", wref()  # wref() is None at script
    print "wref() is None:  ", wref() is None
    print "wref() is None:  ", wref() is None


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


def section8_6_0x02():
    """
    WeakValueDictionary 类实现的是一种可变映射，里面的值是对象的弱引用。
    被引用的对象在程序中的其他地方被当作垃圾回收后，对应的键会自动从 WeakValueDictionary 中删除。
    因此，WeakValueDictionary 经常用于缓存。
    :return:
    """
    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

    for cheese in catalog:
        stock[cheese.kind] = cheese

    print "sorted(stock.keys()): ", sorted(stock.keys())

    del catalog
    print "[del catalog]\tsorted(stock.keys()): ", sorted(stock.keys())

    del cheese
    print "[del cheese]\tsorted(stock.keys()): ", sorted(stock.keys())
    print "临时变量引用了对象，这可能会导致该变量的存在时间比预期长。" \
          "通常，这对局部变量来说不是问题，因为它们在函数返回时会被销毁。" \
          "但是在上面例子中，for 循环中的变量 cheese 是全局变量，除非显式删除，否则不会消失。"

"""
## 弱引用的局限 ##
不是每个 Python 对象都可以作为弱引用的目标（或称所指对象）。基本的 list 和 dict 实例不能作为所指对象，但是它们的子类可以轻松地解决这个问题：

class MyList(list):
    "list的子类，实例可以作为弱引用的目标"

a_list = MyList(range(10))

# a_list可以作为弱引用的目标
wref_to_a_list = weakref.ref(a_list)
"""

# endregion

# region section8_7 Python对不可变类型施加的把戏

def section8_7():
    print """共享字符串字面量是一种优化措施，称为驻留（interning）。
CPython 还会在小的整数上使用这个优化措施，防止重复创建“热门”数字，如 0、-1 和 42。
包括 frozenset.copy() 的行为，是“善意的谎言”，能节省内存，提升解释器的速度。
别担心，它们不会为你带来任何麻烦，因为只有不可变类型会受到影响。
"""
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    t3 = t1[:]
    print "t1 is:\tt1 = (1, 2, 3)"
    print "t2 is:\tt2 = tuple(t1)"
    print "t3 is:\tt3 = t1[:]"
    print "t1 is t2:\t", t1 is t2
    print "t3 is t2:\t", t3 is t2

    print "-"*20
    t11 = (1, 2, 3)
    t33 = (1, 2, 3)
    print "t11 is: t11 = (1, 2, 3), and t33 is: t33 = (1, 2, 3)"
    print "t11 is t33:\t", t11 is t33


# endregion section8_7 Python对不可变类型施加的把戏

if __name__ == '__main__':
    # section8_5()
    # section8_6_0x01()
    # section8_6_0x02()
    section8_7()
