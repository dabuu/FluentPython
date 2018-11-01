# coding:utf-8
"""
@file: decorator_time_watch_exmaple.py
@time: 2018/10/30 16:38
@contact: dabuwang
@desc: todo
"""
__author__ = 'dabuwang'
import os
import time
import functools

cost_time = 0

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global cost_time
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        cost_time = (te - ts)
        # print "costtime: %s " % cost_time
        return result
    return wrapper

@timeit
def run_time():
    os.system('ping localhost -n 5')

if __name__ == '__main__':
    run_time()
    print "cost time: ", cost_time
