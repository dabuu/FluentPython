# coding:utf-8
"""
@file: run_two_cmds_together.py
@time: 2018/10/25 16:15
@contact: dabuwang
@desc: sometimes  we meet below test scenario:
run one cmd, and check result by another socket client's output.
====
solution snippet like below
"""
__author__ = 'dabuwang'

import subprocess
import thread
import os
import signal
from threading import Timer


def test_main():
    socket_client_check_msg = r'ping localhost -n 100'
    main_ps = subprocess.Popen(socket_client_check_msg, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    my_timer = Timer(5, lambda ps: os.killpg(os.getpgid(ps.pid), signal.SIGTERM) , [main_ps])
    try:
        thread.start_new_thread(test_thread, ())
        print "1"
        my_timer.start()
        print "2"
        stdout, stderr = main_ps.communicate()
        print "3"
    finally:
        my_timer.cancel()
    print stdout
    print stderr


def test_thread():
    os.system("ping localhost -n 2")
    os.system("calc.exe")


if __name__ == '__main__':
    test_main()
