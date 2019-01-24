# coding:utf-8
"""
@file: open_modify_file_one_handle.py
@time: 2019/1/10 11:17
@contact: dabuwang
@desc:  when change the content in one file, we can read + write the file by one file handle
"""
__author__ = 'dabuwang'

import io


def modify_file(file_fpath, old_content, new_content):
    with io.open(file_fpath, 'r+', encoding='utf-8') as hnd:
        temp = hnd.read()
        temp = temp.replace(old_content, new_content)
        hnd.seek(0)  # 定位到文档开头
        hnd.write(temp)  # 写入替换后内容
        hnd.truncate()  # 截断后续内容
        # hnd.truncate(len(temp.encode('utf-8')))   # 注意：len(temp) is not recommendation, it should be "bytes" len of content, not "str" len
        hnd.flush()
        hnd.close()
