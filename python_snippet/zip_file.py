# coding:utf-8
"""
@file: zip_file.py
@time: 2018/9/19 10:19
@contact: dabuwang
"""
__author__ = 'dabuwang'

import os
import zipfile
import collections


def zip_one_dir_recursion(dir_full_path, to_zipped_full_path, exclude_dirs=None):
    try:
        zipped_path, zipped_name = os.path.split(to_zipped_full_path)
        if not os.path.exists(zipped_path):
            os.makedirs(zipped_path)

        with zipfile.ZipFile(to_zipped_full_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for root_dir, sub_dirs, files in os.walk(dir_full_path):
                if exclude_dirs is not None and isinstance(exclude_dirs, collections.Iterable):
                    sub_dirs[:] = [d for d in sub_dirs if d not in exclude_dirs]
                if root_dir != dir_full_path:
                    zf.write(root_dir, os.path.relpath(root_dir, dir_full_path))
                for filename in files:
                    file_full_path = os.path.join(root_dir, filename)
                    zf.write(file_full_path, os.path.relpath(file_full_path, dir_full_path))
            return True
    except Exception as ex:
        print "Warning: zip_one_dir_recursion: %s" % ex
        return False


def unzip_file_to_path(zipfile_full_path, local_extract_path, include_func=None):
    try:
        with zipfile.ZipFile(zipfile_full_path, 'r') as zip_ref:
            zip_ref.extractall(path=local_extract_path,
                               members=filter(include_func, zip_ref.namelist()) if callable(include_func) else None)
        return True
    except Exception as ex:
        print "Warning: unzip_file_to_path: %s" % ex
        return False

if __name__ == '__main__':
    print "usage as following:"
    # r = zip_one_dir_recursion(
    #     r'D:\Code\',
    #     r"D:\test\test5.zip",
    #     ['exe']
    # )

    # r = unzip_file_to_path(r"D:\Code\test.zip",
    #                    r"D:\test\\",
    #                    lambda x: x.startswith("node")
    # )
