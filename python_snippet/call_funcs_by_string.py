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


if __name__ == '__main__':
    test_locals()
