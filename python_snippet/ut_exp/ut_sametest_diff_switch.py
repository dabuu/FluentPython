# coding:utf-8
"""
@file: ut_sametest_diff_switch.py
@time: 2018/9/27 18:04
@contact: dabuwang
"""
__author__ = 'dabuwang'

import unittest

class TestSequense(unittest.TestCase):
    ss = 0

    @classmethod
    def setUpClass(cls):
        cls.ss = 0


    def test_123(self):
        self.assertTrue(self.ss == 0)


class TestSequenseChild(TestSequense):
    @classmethod
    def setUpClass(cls):
        cls.ss = 1


if __name__ == '__main__':
    unittest.main(verbosity=2)