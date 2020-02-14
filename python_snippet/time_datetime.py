# coding:utf-8
"""
@file: time_datetime.py
@time: 2/14/2020 9:32 PM
@contact: dabuwang
"""

import time
from datetime import datetime

"""
python中时间日期格式化符号：
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身
"""


def time_func():
    print('当前时间戳：', time.time())
    # 当前时间戳： 1529908783.3990765
    print('获取当前本地时间：', time.localtime())
    # 获取当前本地时间： time.struct_time(tm_year=2018, tm_mon=6, tm_mday=25, tm_hour=14, tm_min=39, tm_sec=43, tm_wday=0, tm_yday=176, tm_isdst=0)
    print('格式化可读时间模式：', time.asctime())
    # 格式化可读时间模式： Mon Jun 25 14:39:43 2018
    print('格式化日期：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    t = time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
    print t


def datetime_func():
    datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
    datetime.now().strptime("2020-02-14T20:20:10.610000", '%Y-%m-%dT%H:%M:%S.%f')
