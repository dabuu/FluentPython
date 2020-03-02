# coding:utf-8
"""
@file: url_encode_usage.py
@time: 2019/9/26 18:15
@contact: dabuwang
@desc: only python2.7

python 2.x  vs python 3.x refer: https://blog.csdn.net/IMW_MG/article/details/78555375
"""
__author__ = 'dabuwang'


def dict_encode():
    from urllib import urlencode
    data = {
        'a': 'test',
        'name': 'dabu'
    }
    print urlencode(data)


def str_encode():
    from urllib import quote
    data = '{"a":1,"field":["age"],"minute":120}'
    print quote(data)
    safe_data = 'a//b'
    print quote(safe_data, safe='')
    safe_data = 'a//bb\\c&'
    print quote(safe_data, safe='/,&')


def url_decode():
    from urllib import unquote
    data = '%7B%22a%22%3A1%2C%22field%22%3A%5B%22age%22%5D%2C%22minute%22%3A120%7D'
    print unquote(data)


if __name__ == '__main__':
    dict_encode()
    str_encode()
    url_decode()
