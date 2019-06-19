# coding:utf-8
"""
@file: call_funcs_by_string.py
@time: 2019/1/15 16:31
@contact: dabuwang
@desc: Python: Call Functions by String

refer link: https://arithxu.com/2017/10/14/Python-Call-Functions-by-String/
"""
__author__ = 'dabuwang'


def test_call_fun_by_dict():
    def _ssh(hostname, port):
        print "ssh", hostname, port

    def _telnet(hostname, port):
        print "telnet", hostname, port

    protocols = {
        'ssh': _ssh,
        'telnet': _telnet
    }

    # call your function by string
    hostname = 'localhost'
    port = '22'
    protocol = 'ssh'
    protocols[protocol](hostname, port)


def test_exec():
    """
    No return value
    """
    def my_exec(arg1, arg2):
        print(arg1, arg2)
        return arg1 + arg2
    # The return value of exec() is None
    exec ('my_exec(1, 2)')

def test_eval():
    def my_eval(arg1, arg2):
        print(arg1, arg2)
        return arg1 + arg2

    # The return value of exec() is None
    r = eval('my_eval(1, 2)')
    print(r)
    r = eval('1 == 2')
    print(r)

def test_locals():
    def my_locals(arg1, arg2):
        print(arg1, arg2)
        return arg1 + arg2

    r = locals()['my_locals'](3, 4)
    print(r)


class KlsTest:
    def __init__(self):
        self.__class__.__dict__["gene_test1"].__func__(4, "b")
        self.__class__.__dict__["gene_test2"].__func__()
        self.__class__.__dict__["gene_test3"](self)
        fun_object = self.__class__.__dict__.get("gene_test1", None)
        fun_object.__func__(3, "a")
        fun_object = self.__class__.__dict__.get("gene_test4", None)
        print fun_object
        # fun = [key for key in self.__class__.__dict__.keys() if key.startswith("gene_test")]
        # print fun

    @staticmethod
    def gene_test1(x,y):
        print "gene_test1", x, y
    @staticmethod
    def gene_test2():
        print "gene_test2"
    def gene_test3(self):
        print "gene_test3"


if __name__ == '__main__':
    KlsTest()
    # test_locals()
