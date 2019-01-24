# coding:utf-8
"""
@file: 4.5.py
@time: 2019/1/7 13:19
@contact: dabuwang
@desc: 4.5 handle txt file
Unicode 三明治：
1. bytes -> str
2. 100% str
3. str -> bytes

=========
示例 test_default_encoding 中有 4 种不同的编码。

如果打开文件时没有指定 encoding 参数，默认值由 locale.getpreferredencoding() 提供（在示例 4-12 中是 'cp1252'）。

如果设定了 PYTHONIOENCODING 环境变量，sys.stdout/stdin/stderr 的编码使用设定的值；否则，继承自所在的控制台；如果输入 / 输出重定向到文件，则由 locale.getpreferredencoding() 定义。

Python 在二进制数据和字符串之间转换时，内部使用 sys.getdefaultencoding() 获得的编码；Python 3 很少如此，但仍有发生。这个设置不能修改。

sys.getfilesystemencoding() 用于编解码文件名（不是文件内容）。把字符串参数作为文件名传给 open() 函数时就会使用它；如果传入的文件名参数是字节序列，那就不经改动直接传给 OS API。“Unicode HOWTO”一文中说：“在 Windows 中，Python 使用 mbcs 这个名称引用当前配置的编码。”MBCS 是 Multi Byte Character Set（多字节字符集）的首字母缩写，在 Windows 中是陈旧的变长编码，如 gb2312 或 Shift_JIS，而不是 UTF-8。 [关于这个话题，Stack Overflow 中有一个很好的回答，“Difference between MBCS and UTF-8 on Windows”。]

"""
__author__ = 'dabuwang'

import io
import os
import sys
import locale


def only_read_here4python27():
    """
    >>> '中'   # ide环境是 utf8
    '\xe4\xb8\xad'
    >>> '中'.decode('utf8')  # decode to unicode
    u'\u4e2d'

    >>> ('中'.decode('utf8')).encode('gbk')   # unicode 编码成 gbk
    '\xd6\xd0'
    >>> ('中'.decode('utf8')).encode('utf8')  # unicode 编码成 gbk
    '\xe4\xb8\xad'
    >>> u"中".encode('gbk')
    '\xd6\xd0'
    >>> u"中".encode('utf8')
    '\xe4\xb8\xad'
    :return:
    """
    pass



def test_simple():
    """
    注意 这里 是 Python 2.7 , 要使用 io.open; 如果是 Python3.x， 直接 open() 就ok。
    :return:
    """
    # num1 = open('cafe.txt', 'w', encoding='utf-8').write('café')  # python 3.x
    num1 = io.open('cafe.txt', 'w', encoding='utf-8').write(u'café')    # python 2.7
    print num1

    print io.open('cafe.txt', 'r', encoding='cp1252').read()
    with io.open('cafe.txt') as fp2:
        print fp2.encoding
        print fp2.read()
    with io.open('cafe.txt', 'rb') as fp21:
        print fp21.read()

    print "=====  open "
    with open('cafe.txt') as fp3:
        print fp3.encoding
        print fp3.read()
    with open('cafe.txt','rb') as fp31:
        print fp31.read()

    print os.stat('cafe.txt').st_size

def test_default_encoding():
    expressions = """
            locale.getpreferredencoding()
            type(my_file)
            my_file.encoding
            sys.stdout.isatty()
            sys.stdout.encoding
            sys.stdin.isatty()
            sys.stdin.encoding
            sys.stderr.isatty()
            sys.stderr.encoding
            sys.getdefaultencoding()
            sys.getfilesystemencoding()
        """
    # my_file = open('dummy', 'w')
    my_file = io.open('dummy', 'w')

    for expression in expressions.split():
        value = eval(expression)
        print(expression.rjust(30), '->', repr(value))


if __name__ == '__main__':
    """
    C:\Users\dabuwang>chcp
    活动代码页: 936
    """



    # test_simple()
    """
    4
    cafÃ©
    cp936
    caf茅
    café
    =====  open 
    None
    café
    café
    5
    """

    test_default_encoding()
    """
    (' locale.getpreferredencoding()', '->', "'cp936'")
    ('                 type(my_file)', '->', "<type '_io.TextIOWrapper'>")
    ('              my_file.encoding', '->', "'cp936'")
    ('           sys.stdout.isatty()', '->', 'False')
    ('           sys.stdout.encoding', '->', "'UTF-8'")
    ('            sys.stdin.isatty()', '->', 'False')
    ('            sys.stdin.encoding', '->', "'UTF-8'")
    ('           sys.stderr.isatty()', '->', 'False')
    ('           sys.stderr.encoding', '->', "'UTF-8'")
    ('      sys.getdefaultencoding()', '->', "'ascii'")
    ('   sys.getfilesystemencoding()', '->', "'mbcs'")
    """
