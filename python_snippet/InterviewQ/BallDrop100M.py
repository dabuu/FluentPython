# coding:utf-8
"""
@file: BallDrop100M.py
@time: 8/19/2019 11:44 PM
@contact: dabuwang
"""


def drop_ball(rebounce, top=100):
    sum_d, now_d = 0, 0
    while rebounce > 0:
        rebounce -= 1
        now_d = top / 2.0
        sum_d += top + now_d
        top = now_d

    print "10 times: sum: %s, now top: %s" %(sum_d, now_d)

def fun2():
    sum, j = 100.0, 50.0
    for i in range(2, 11, 1):
        sum += j * 2
        j = j/2
    print "10 times: sum: %s, now top: %s" % (sum, j)

if __name__ == '__main__':
    # drop_ball(10)
    fun2()
