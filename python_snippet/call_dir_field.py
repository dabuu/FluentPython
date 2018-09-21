# coding:utf-8
"""
@file: call_dir_field.py
@time: 2018/9/21 16:47
@contact: dabuwang
@desc: just test example for dir and how to callable the field by myself
"""
__author__ = 'dabuwang'

SOCKET_ALERT = "/tmp/alert.unixsocket"
SOCKET_EVE_JSON = "/tmp/files-json.unixsocket"
SOCKET_TI_ALERT = "/tmp/ti_alert.unixsocket"
SOCKET_EVE_FLOW = "/tmp/eve_flow.unixsocket"
SOCKET_EVE_STATUS = "/tmp/eve_stats.unixsocket"
SOCKET_LOG = "/tmp/logs_6.unixsocket"

if __name__ == "__main__":
    print dir()[0]
    print eval(dir()[0])