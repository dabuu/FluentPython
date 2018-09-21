# coding:utf-8
"""
@file: find_latest_file.py
@time: 2018/9/19 10:19
@contact: dabuwang
"""
__author__ = 'dabuwang'

import glob
import os

def find_latest_file(fpath, pattern="*"):
    if not os.path.isdir(fpath):
        return None
    ret = [x for x in glob.glob(os.path.join(fpath, pattern)) if os.path.isfile(x)]
    if ret:
        return sorted(ret, key=lambda f: os.path.getmtime(f), reverse=True)[0]
        # return ret[0] 默认是按名字排序
    return None


if __name__ == '__main__':
    path = r"D:\test\test_pdf"
    ret = find_latest_file(path, "*.exe")
    print ret