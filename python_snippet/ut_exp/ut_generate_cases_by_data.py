# coding:utf-8
"""
@file: ut_generate_cases_by_data.py
@time: 2018/10/29 15:29
@contact: dabuwang
@desc: todo
"""
__author__ = 'dabuwang'

import unittest


def __specific_case(key, value):
    tlist = ['a', 'b', 'c']
    return tlist[key - 1] == value


def detail_generator(d_key):
    def test_case(self):
        self.assertTrue(__specific_case(d_key, TestGenerator.test_data[d_key]))
    return test_case

def _cases_generator():
    for tkey in TestGenerator.test_data.keys():
        test_fn_name = "test_file_%s" % tkey

        # def test_case(self):
        #     self.assertTrue(__specific_case(tkey, TestGenerator.test_data[tkey]))
        test_fn = detail_generator(tkey)
        setattr(TestGenerator, test_fn_name, test_fn)


class TestGenerator(unittest.TestCase):
    """
    SIZE: 50m
    FILE type: exe, dll, script, zip, pdf, doc
    """
    test_data = {
        1: "a",
        2: "b",
        3: "d"
    }


if __name__ == '__main__':
    _cases_generator()
    unittest.main(verbosity=2)
