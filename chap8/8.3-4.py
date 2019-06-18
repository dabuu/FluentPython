# coding:utf-8
"""
@file: 8.3-4.py.py
@time: 6/13/2019 10:22 PM
@contact: dabuwang
"""


# region section8_3_0x01 默认的浅拷贝
def section8_3_0x01():
    """
    list() or [:] 默认是浅拷贝
    http://www.pythontutor.com/  python 交互动画
    :return:
    """
    l1 = [3, [55, 44], (7, 8, 9)]
    l2 = list(l1)  # l1[:]
    print "l2 == l1", l2 == l1
    print "l2 is l1", l2 is l1
    print "l2[1] is l1[1]", l2[1] is l1[1]
    print "l2's value is same as l1, but l2 is not l1."
    print "\033[0;31;47m*Notice*: l1[1] is l2[1], which would cause bugs!\033[0m"

    print "-" * 20
    print "l2: ", l2
    l1.append(100)
    print "l1.append(100): ", l1
    l1[1].remove(55)
    print "l1[1].remove(55): ", l1
    print "l2 now:", l2

    print "-" * 30
    print "id(l1[1]),id(l2[1])", id(l1[1]), id(l2[1])
    l2[1] += [33, 22]
    print "l2[1] += [33,22], id(l1[1]),id(l2[1]):  ", id(l1[1]), id(l2[1])
    print "l2[1] += [33,22], l1, l2:  ", l1, l2

    print "id(l1[2]),id(l2[2])", id(l1[2]), id(l2[2])
    l2[2] += (10, 11)
    print " l2[2] += (10, 11), id(l1[2]),id(l2[2]):  ", id(l1[2]), id(l2[2])
    print "l2[2] += (10, 11), l1, l2:  ", l1, l2
    print "\033[0;31;47m*Notice*: list1 += list2, the id(list1) is NOT change! \
     But it will FAIL when '+=' using at tuple! Details: chap2:2.5+6.py\033[0m"


# endregion

# region  section8_3_0x02  为任意对象做深复制和浅复制
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
        print "bus's passengers init: %s" % self.passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def section8_3_0x02():
    """
    为任意对象做深复制和浅复制
    :return:
    """
    import copy
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)

    print "id(bus1),id(bus2),id(bus3): ", id(bus1), id(bus2), id(bus3)

    bus1.drop("Bill")
    print "bus1.passengers: ", bus1.passengers
    print "bus2.passengers: ", bus2.passengers
    print "bus3.passengers: ", bus3.passengers
    # 审查 passengers 属性后发现，bus1 和 bus2 共享同一个列表对象，因为 bus2 是 bus1 的浅复制副本
    print "id(bus1),id(bus2),id(bus3): ", id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)

    print "-" * 20
    print "深复制不是件简单的事。如果对象有循环引用，那么这个朴素的算法会进入无限循环。\
    deepcopy 函数会记住已经复制的对象，因此能优雅地处理循环引用"
    a = [10, 20]
    b = [a, 30]
    a.append(b)  # 循环引用
    print "a, which call loop: ", a
    c = copy.deepcopy(a)
    print "c = copy.deepcopy(a): ", c


# endregion


# region section8_4_0x00
def section8_4_0x00():
    """
    函数*可能会修改*作为参数传入的可变对象
    但是*无法修改*那些对象的标识（即不能把一个对象替换成另一个对象）
    :return:
    """

    def f(a, b):
        a += b
        print "fun a: ", a
        return a

    x, y = 1, 2
    print "init: x,y: ", x, y
    f(x, y)
    print "run F(x,y): ", x, y
    print "-" * 20
    x, y = [1], [2]
    print "init: x,y: ", x, y
    f(x, y)
    print "run F(x,y): ", x, y
    print "-" * 20
    x, y = (3, 5), (4, 6)
    print "init: x,y: ", x, y
    f(x, y)
    print "run F(x,y): ", x, y


# endregion section8_4_0x01


# region section8_4_0x01
# **不要使用可变类型作为参数的默认值**
class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    def __init__(self, passengers=[]):
        """
        Pycharm IDE notice: Default argument value is mutable 默认参数可变
        :param passengers:
        """
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def section8_4_0x01():
    bus1 = HauntedBus(['Alice', 'Bill'])
    print "bus1.passengers: ", bus1.passengers
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print "pick('Charlie'),drop('Alice') - bus1.passengers: ", bus1.passengers
    print "-" * 20, "bus1 is normal!"

    bus2 = HauntedBus()
    print "bus2.passengers: ", bus2.passengers
    bus2.pick('Carrie')
    print "pick('Carrie') - bus2.passengers: ", bus2.passengers

    bus3 = HauntedBus()
    print "bus3.passengers: ", bus3.passengers
    bus3.pick('Dave')
    print "pick('Dave') - bus3.passengers: ", bus3.passengers
    print "bus2.passengers is bus3.passengers: ", bus2.passengers is bus3.passengers
    print "bus2.passengers is bus1.passengers: ", bus2.passengers is bus1.passengers


# endregion section8_4_0x01

# region section8_4_0x02
# **防御可变参数 - 传入的可变参数 要做copy处理**
class TwilightBus:
    """让乘客销声匿迹的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers
            # self.passengers = list(passengers) # this is CORRECT way to use refer value

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def section8_4_0x02():
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
    bus = TwilightBus(basketball_team)
    bus.drop('Diana')
    bus.drop('Pat')

    print "drop('Diana'),drop('Pat') - bus.passengers: ", bus.passengers
    print "basketball_team players: ", basketball_team


# endregion section8_4_0x02

if __name__ == '__main__':
    section8_3_0x01()
    section8_3_0x02()
    print "#" * 40
    section8_4_0x00()
    print "#" * 40
    section8_4_0x01()
    print "#" * 40
    section8_4_0x02()
