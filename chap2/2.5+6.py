# coding:utf-8
"""
@file: 2.5+6.py
@time: 2018/9/23 下午11:04
@contact: dabuwang
@desc: use "+", "*", "+=" for list
use "+", "*" operate will create a new list
"""


def list_add_test_1():
    al = [1, 2, 3]
    bl = [4, 5, 6]
    print al + bl
    pass


def list_mul_test_1():
    ml = list(range(1, 4, 1))
    print ml
    print ml * 3

    ml_str = 'abcd'
    print ml_str
    print 3 * ml_str

    pass


def list_mul_test_2():
    """
    create list array for list
    建立由列表组成的列表
    :return:
    """
    # wrong way
    print "===== wrong way ====="
    wboard = [['_'] * 3] * 3
    print wboard
    wboard[1][2] = 'x'
    print wboard

    w_row = ["_"] * 3
    wboard = []
    for i in range(3):
        wboard.append(w_row)
    print wboard
    wboard[1][2] = 'x_2'
    print wboard

    # correct way
    print "===== correct way ====="
    cboard = [['_'] * 3 for i in range(3)]
    print cboard
    cboard[1][2] = "y"
    print cboard

    cboard = []
    for i in range(3):
        cboard.append(["_"] * 3)
    print cboard
    cboard[1][2] = "y_2"
    print cboard


def list_augmented_assignment_test_1():
    """
    增量赋值 调用方法 __iadd__, __imul__
    :return:
    """
    mul_list = [1, 2, 3]
    print mul_list
    print id(mul_list)
    mul_list *= 2
    print mul_list
    print id(mul_list)
    print "==== list's id is same, tuple's id is changed ===="
    mul_tuple = (4, 5, 6)
    print mul_tuple
    print id(mul_tuple)
    mul_tuple *= 2
    print mul_tuple
    print id(mul_tuple)


def list_augmented_assignment_test_2():
    """
    >> dis.dis('s[a] += b')
  1           0 LOAD_NAME                  0(s)
              3 LOAD_NAME                  1(a)
              6 DUP_TOP_TWO
              7 BINARY_SUBSCR                      ➊
              8 LOAD_NAME                  2(b)
             11 INPLACE_ADD                        ➋
             12 ROT_THREE
             13 STORE_SUBSCR                       ➌
             14 LOAD_CONST                 0(None)
             17 RETURN_VALUE
➊ 将 s[a] 的值存入 TOS（Top Of Stack，栈的顶端）。
➋ 计算 TOS += b。这一步能够完成，是因为 TOS 指向的是一个可变对象（也就是示例 2-15 里的列表）。
➌ s[a] = TOS 赋值。这一步失败，是因为 s 是不可变的元组（示例 2-15 中的元组 t）。

    STRANGE question for +=
    BTW, Python Tutor是一个对 Python 运行原理进行可视化分析的工具
    =========
    至此我得到了 3 个教训。
    不要把可变对象放在元组里面。
    增量赋值不是一个原子操作。我们刚才也看到了，它虽然抛出了异常，但还是完成了操作。
    查看 Python 的字节码并不难，而且它对我们了解代码背后的运行机制很有帮助。
    :return:
    """
    st = (1, 2, [30, 40])
    print st
    try:
        st[2] += [50, 60]
    except Exception as ex:
        print "throw wrong %s" % ex
    print "strange result??"
    print st

    try:
        st[2].extend([70, 80])
    except Exception as ex:
        print "throw wrong again %s" % ex
    print "hope result"
    print st


if __name__ == '__main__':
    # list_add_test_1()
    # list_mul_test_1()
    # list_mul_test_2()
    # list_augmented_assignment_test_1()
    list_augmented_assignment_test_2()
