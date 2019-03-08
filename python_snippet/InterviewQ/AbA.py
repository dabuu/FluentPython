# coding:utf-8
"""
@file: AbA.py.py
@time: 2019/3/8 10:01
@contact: dabuwang
@desc: handle string , remove "xYx" or "yxy" string,
"ghiuAbAccDcaaeae" -> ghiucae

"""
__author__ = 'dabuwang'


def xYxHandle(i_str):
    print "=" * 15
    if len(i_str) < 3:
        print "result:", i_str
        return

    str_len = len(i_str)
    n_str = list(i_str[:2])
    for i in range(2, str_len):
        n_str.append(i_str[i])
        if len(n_str) < 3:
            continue
        if n_str[-1] == n_str[-3] and n_str[-1] != n_str[-2]:
            print "rm xYx:", "".join(n_str[-3:])
            n_str = n_str[:-3]

    print "result:", "".join(n_str)


if __name__ == '__main__':
    xYxHandle("ghiucAbAcDcaaeae")
    xYxHandle("ghiudEAbAcDcaaeaE")
    xYxHandle("ghiudEAAAcDcaaeaE")
    xYxHandle("ABA")
    xYxHandle("ABAaXa")
    xYxHandle("AA")
    xYxHandle("")

