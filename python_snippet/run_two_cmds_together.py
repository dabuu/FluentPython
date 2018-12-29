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
import time

__author__ = 'dabuwang'

import subprocess
import thread
import os
import signal
from threading import Timer
from threading import Thread

def test_main():
    test_cmd = r'ping localhost -n 100'
    main_ps = subprocess.Popen(test_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
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


def run_cmd(cmd, time_wait=-1):
    subp = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    if time_wait <= 0:
        subp.wait()
    else:
        time.sleep(time_wait)
    out, err = subp.communicate()
    return out, err





if __name__ == '__main__':
    test_main()
