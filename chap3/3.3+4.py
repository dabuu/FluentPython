# coding:utf-8
"""
@file: 3.3+4.py
@time: 2018/9/30 16:38
@contact: dabuwang
@desc:
3.3 dict, defaultdict, OrderedDict: 后两个是前者的特殊变种。
区别： defaultdict 在其初始化中 需要显示定义默认值
OrderedDict 是有序的dict

3.4 映射的弹性键查询： two options:
a. default dict
b. dict subclass, implementation method: __missing__
"""
__author__ = 'dabuwang'

import re
import collections

# import this  # which would show the ZEN of python
zen_text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


def not_setdefault_test_1():
    global zen_text
    WORD_RE = re.compile("\w+")
    index = dict()

    for line_no, line in enumerate(zen_text.split('\n'), 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

    for word in sorted(index, key=str.upper):
        print (word, index[word])


def use_setdefault_test_2():
    global zen_text
    WORD_RE = re.compile("\w+")
    index = dict()

    for line_no, line in enumerate(zen_text.split('\n'), 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # occurrences = index.get(word,[])
            # occurrences.append(location)
            # index[word] = occurrences

            # updated: 上面3行被替换成下面一行
            index.setdefault(word, []).append(location)

    for word in sorted(index, key=str.upper):
        print (word, index[word])


def use_defaultdict_test_3():
    global zen_text
    WORD_RE = re.compile("\w+")
    index = collections.defaultdict(list)

    for line_no, line in enumerate(zen_text.split('\n'), 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # occurrences = index.get(word,[])
            # occurrences.append(location)
            # index[word] = occurrences

            # updated: 上面3行被替换成下面一行
            # index.setdefault(word, []).append(location)

            # updated: dict -> defaultdict， default value is list. so append 'location' directly
            index[word].append(location)

    for word in sorted(index, key=str.upper):
        print (word, index[word])


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


def use_missing_in_subdict_test_4():
    td = dict([("2", "two"), ("4", "four")])
    print td["2"]
    try:
        print td[4]

    except KeyError, ke:
        print "Warning: td[4] raise error: %s" % ke
    print '"4" in td', "4" in td
    print '2 in td', 2 in td

    print "=============="

    skd = StrKeyDict0([("2", "two"), ("4", "four")])
    print skd["2"]
    print skd[4]
    print skd.get(2)
    print skd.get(1, 'None')

    print '"2" in skd', "2" in skd
    print '4 in skd', 4 in skd


if __name__ == '__main__':
    # not_setdefault_test_1()
    # use_setdefault_test_2()
    # use_defaultdict_test_3()
    use_missing_in_subdict_test_4()
