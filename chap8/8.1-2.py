# coding:utf-8
"""
@file: 8.1-2.py.py
@time: 6/11/2019 11:07 PM
@contact: dabuwang
"""


# region section 8.1: 变量不是盒子，是标注
def section8_1():
    a = [1, 2, 3]
    b = a
    print "a, b", a, b
    a.append(4)
    print "a, b", a, b
    print "id(a), id(b)", id(a), id(b)

    class Gizmo:
        def __init__(self):
            print('Gizmo id: %d' % id(self))

    x = Gizmo()
    try:
        y = Gizmo() * 10
    except Exception, e:
        print "Error: y can't assign: %s" % e


# endregion


# region section 8.2
def section8_2_0x01():
    """
    '==' vs 'is', '==' meaning the value is same, and 'is' meaning the id is same
    == 运算符比较两个对象的值（对象中保存的数据），而 is 比较对象的标识。
    is 运算符比 == 速度快，因为它不能重载，所以 Python 不用寻找并调用特殊方法，而是直接比较两个整数 ID。
    而 a == b 是语法糖，等同于 a.__eq__(b)。继承自 object 的 __eq__ 方法比较两个对象的 ID，结果与 is 一样。
    但是多数内置类型使用更有意义的方式覆盖了 __eq__ 方法，会考虑对象属性的值。
    相等性测试可能涉及大量处理工作，例如，比较大型集合或嵌套层级深的结构时。
    :return:
    """
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    print "lewis is charles: ", lewis is charles, lewis
    print "id(lewis), id(charles): ", id(lewis), id(charles)
    charles['balance'] = 1000
    print "charles['balance'] = 1000, and lewis' value: ", lewis

    # ------------
    print "-" * 20

    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 1000}
    print "alex == lewis: ", alex == lewis
    print "alex is not lewis: ", alex is not lewis


def section8_2_0x02():
    """
    元组的相对不可变性
    元组与多数 Python 集合（列表、字典、集，等等）一样，保存的是对象的引用。
    如果引用的元素是可变的，即便元组本身不可变，元素依然可变。
    也就是说，元组的不可变性其实是指 tuple 数据结构的物理内容（即保存的引用）不可变，与引用的对象无关。
    :return:
    """
    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])
    print "t1, t2, t1 == t2: ", t1, t2, t1 == t2

    print "t1[-1]'s id: ", id(t1[-1])
    t1[-1].append(50)
    print "t1, t2, t1 == t2: ", t1, t2, t1 == t2  # t1[-1] 的标识没变，只是值变了。
    print "t1[-1]'s id: ", id(t1[-1])


# endregion

if __name__ == '__main__':
    # section8_1()
    # section8_2_0x01()
    section8_2_0x02()
