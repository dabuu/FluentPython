# coding:utf-8
"""
@file: fun_map_filter_reduce.py
@time: 2018/9/20 16:06
@contact: dabuwang
"""
__author__ = 'dabuwang'


def test_map():
    pass


def test_filter():
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
    test_reduce()
