# coding:utf-8
"""
@file: fun_map_filter_reduce.py
@time: 2018/9/20 16:06
@contact: dabuwang
"""
__author__ = 'dabuwang'


def test_map():
    td = ['aa', '123']
    # ts = "fjsadluovx123fsfjouvxabc aa"
    ts = "fjsadluovx123fsfjouvxabc"
    ret = map(lambda x: x in ts, td)
    print "map check rst: ", ret

    ret = reduce(lambda x,y: x & y, ret)
    print "reduce map rst: ", ret


def test_filter():
    print filter(None, ["", "123", "1235", "4123", ""])
    pass


def test_reduce():
    """
    自带的递归逻辑函数
    :return:
    """
    n = 3
    print reduce(lambda x, y: x * y, range(1, n))
    # 这里的 {1: {2: "b"}} 可以理解为 x的初始值， 具体对比 可以看 python_snippet/get_value_in_deep_dict.py
    print reduce(lambda x, y: x.get(y) if x else None, range(1, n), {1: {2: "b"}})


if __name__ == '__main__':
    test_map()
    test_filter()
    # test_reduce()
