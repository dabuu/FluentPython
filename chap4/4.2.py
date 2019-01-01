# coding:utf-8
"""
@file: 4.2.py
@time: 1/2/2019 12:26 AM
@contact: dabuwang
"""

"""
新的二进制序列类型在很多方面与 Python 2 的 str 类型不同。
首先要知道，Python 内置了两种基本的二进制序列类型：Python 3 引入的不可变 bytes 类型和 Python 2.6 添加的可变 bytearray 类型。
（Python 2.6 也引入了 bytes 类型，但那只不过是 str 类型的别名，与 Python 3 的 bytes 类型不同。）
[*dabu: 2.7 vs. 3.x 中 bytes类型的 定义完全不同*]

bytes 或 bytearray 对象的各个元素是介于 0~255（含）之间的整数，而不像 Python 2 的 str 对象那样是单个的字符。然而，二进制序列的切片始终是同一类型的二进制序列，包括长度为 1 的切片，
"""

def test_bytes_bytearray():
    # cafe = bytes(u'café', encoding='utf_8')   # python 3.x code
    cafe = bytes(u'café'.encode('utf-8'))       # python 2.7 code
    print repr(cafe[0])     # python 3.x Would return Int, value must be 99. python 2.7 return a byte
    print repr(cafe[:1])    # slice return a bytes object
    cafe_arr = bytearray(cafe)
    print repr(cafe_arr)
    print repr(cafe_arr[-1:])   # slice return a bytearray object

    # region python 2.7 return results
    """
    'c'
    'c'
    bytearray(b'caf\xc3\xa9')
    bytearray(b'\xa9')
    """
    # endregion

def test_fromhex():
    # bytes.fromhex('31 4B CE A9')  # 3.x only
    pass

def test_gif():
    """
    使用缓冲类对象创建 bytes 或 bytearray 对象时，始终复制源对象中的字节序列。
    与之相反，memoryview 对象允许在二进制数据结构之间共享内存。
    如果想从二进制序列中提取结构化信息，struct 模块是重要的工具。
    :return:
    """
    import struct
    fmt = '<3s3sHH'
    with open('smile2.gif', 'rb') as fp:
        # img = memoryview(fp.read())
        img = fp.read()
    header = img[:10]
    print repr(header)
    print bytes(header)
    ret = struct.unpack(fmt, header)
    print ret
    del header
    del img

if __name__ == '__main__':
    # test_bytes_bytearray()
    test_gif()