# coding:utf-8
"""
@file: 4.1.py
@time: 1/2/2019 12:11 AM
@contact: dabuwang
"""

"""
字符的标识，即码位，是 0~1 114 111 的数字（十进制），在 Unicode 标准中以 4~6 个十六进制数字表示，而且加前缀“U+”。例如，字母 A 的码位是 U+0041，欧元符号的码位是 U+20AC，高音谱号的码位是 U+1D11E。在 Unicode 6.3 中（这是 Python 3.4 使用的标准），约 10% 的有效码位有对应的字符。

字符的具体表述取决于所用的编码。编码是在码位和字节序列之间转换时使用的算法。在 UTF-8 编码中，A（U+0041）的码位编码成单个字节 \x41，而在 UTF-16LE 编码中编码成两个字节 \x41\x00。再举个例子，欧元符号（U+20AC）在 UTF-8 编码中是三个字节——\xe2\x82\xac，而在 UTF-16LE 中编码成两个字节：\xac\x20。

把码位转换成字节序列的过程是编码；把字节序列转换成码位的过程是解码。
从 Python 3 的 str 对象中获取的元素是 *Unicode* 字符，这相当于从 Python 2 的 unicode 对象中获取的元素，而不是从 Python 2 的 str 对象中获取的原始字节序列。
"""
def test_encode_decode():
    s = 'café'  # dabu: if py is 3.x, 'café' is unicode already.
    s = u'café' # dabu: if py is 2.7, MUST be start with u'xx' as unicode
    print repr(s), len(s)
    b = s.encode('utf8')
    print repr(b),  len(b)
    print repr(b.decode('utf8'))

if __name__ == '__main__':
    test_encode_decode()