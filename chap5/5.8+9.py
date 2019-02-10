# coding:utf-8
"""
@file: 5.8+9.py
@time: 2/10/2019 9:17 PM
@contact: dabuwang
@content:
5.8:    获取关于参数信息
5.9：    函数注解 ， 仅python3 支持
"""
from clip import clip
"""
def clip(text, max_len=80):
    
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()
"""

def test58_1():
    """
    函数对象有个 __defaults__ 属性，它的值是一个元组，里面保存着定位参数和关键字参数的默认值。
    仅限关键字参数的默认值在 __kwdefaults__ 属性中。
    然而，参数的名称在 __code__ 属性中，它的值是一个 code 对象引用，自身也有很多属性。
    参数名称在 __code__.co_varnames 中，不过里面还有函数定义体中创建的局部变量。
    因此，参数名称是前 N 个字符串，N 的值由 __code__.co_argcount 确定。
    :return:
    """
    print clip.__defaults__
    print clip.__code__
    print clip.__code__.co_varnames
    print clip.__code__.co_argcount

def test58_2():
    # from inspect import signature   # not find in python2.7
    # sig = signature(clip)
    # print str(sig)
    # for name, param in sig.parameters.items():
    #     print(param.kind, ':', name, '=', param.default)

    # python 2.7 , added by dabu
    from inspect import getargs   # not find in python2.7
    args = getargs(clip.__code__)
    print args

def test59():
    """
    主要看 clip.py中 clip_cmt:

    :return:
    """
    pass

if __name__ == '__main__':
    # test58_1()
    test58_2()