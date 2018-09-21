# coding:utf-8
"""
@file: 2.4.py
@time: 2018/9/21 下午10:11
@contact: dabuwang
"""

def slice_test_1():
    """
    为什么切片和区间会忽略最后一个元素
    """
    pass

def slice_test_2():
    """
    seq[start:stop:step]
    :return:
    """
    s = "bicycle"
    print s
    print s[::3]
    print s[::-1]
    print s[::-2]
    pass


def slice_test_3():
    """
    多维切片和省略
    1. 二维的 numpy.ndarray 就可以用 a[i, j] 这种形式来获取，抑或是用 a[m:n, k:l] 的方式来得到二维切片。
    2. 省略（ellipsis）的正确书写方法是三个英语句号（...），而不是 Unicdoe 码位 U+2026 表示的半个省略号（...）。
    在 NumPy 中，... 用作多维数组切片的快捷方式。如果 x 是四维数组，那么 x[i, ...] 就是 x[i, :, :, :] 的缩写。
    """
    pass

def slice_test_4():
    """
    assign value for slice
    :return:
    """
    l = list(range(10))
    print l
    l[2:5] = [30]
    print l
    del l[5:7]
    print l
    l[3::2] = [10,20]
    print l

if __name__ == '__main__':
    slice_test_2()
    slice_test_4()