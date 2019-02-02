# coding:utf-8
"""
@file: re_hypothesis_test.py
@time: 2018/12/3 10:32
@contact: dabuwang
@desc: todo
"""
__author__ = 'dabuwang'

# from hypothesis_regex import regex
from hypothesis.strategies import from_regex
import random
# re_pattern = r'(\w{4})(\d{3})'
# re_pattern = r'setup=[a-z]\&s=\d\&r=\d{5}$'
re_pattern = r'setup=[a-z]\&s=\d\&r=\d{5}$'
re_pattern1 = r'/Ui'
# re_pattern = r'/setup=[a-z]\&s=\d\&r=\d{5}$/Ui'
# re_pattern = r'appendChild\x28\s*document\x2ecreateElement\x28\s*[\x22\x27]button[\x22\x27].*?outerText\s*=\s*[\x22\x27]{2}/smi'
# re_pattern = r'/^..[^\x00]+\x00/Rs'
re_pattern2 = '^[a-z0-9]{23}[a-f0-9]{33}.\x00\x00\x01\x00\x01'
re_pattern3 = '[a-z0-9]{23}[a-f0-9]{33}.\x00\x00\x01\x00\x01'
re_pattern4 = '[\x20-\x7E]+(sh|nc|wget|curl|echo|cat|id|uname)'

# print regex(re_pattern).example()

fr = from_regex(re_pattern4, True)
eg = fr.example()
print eg
print repr(eg)