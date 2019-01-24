# coding:utf-8
"""
@file: re_hypothesis_test.py
@time: 2018/12/3 10:32
@contact: dabuwang
@desc: todo
"""
__author__ = 'dabuwang'

from hypothesis_regex import regex

# re_pattern = r'(\w{4})(\d{3})'
# re_pattern = r'/setup=[a-z]\&s=\d\&r=\d{5}$/Ui'
re_pattern = r'/appendChild\x28\s*document\x2ecreateElement\x28\s*[\x22\x27]button[\x22\x27].*?outerText\s*=\s*[\x22\x27]{2}/smi'

print regex(re_pattern).example(100)