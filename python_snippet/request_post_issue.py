# coding:utf-8
"""
@file: request_post_issue.py
@time: 11/22/2019 10:08 PM
@contact: dabuwang
"""

import requests
import json


def post_issue():
    # def post(url, data=None, json=None, **kwargs):
    requests.post('fake_url', data='', json='')

    # When post data is dict etc, there are 4 situations

    # S1:
    post_data_1 = {'id':1, 'name':'a', 'list':[]}
    requests.post('fake_url', data=post_data_1, json='')
    # request:   data convert to 'id=1&name=a',  NOTICE: list is NOT convert.

    # S2:
    post_data_2 = json.dumps({'id':1, 'name':'a', 'list':[]})
    requests.post('fake_url', data=post_data_2, json='')
    # request:   data is {'id':1, 'name':'a', 'list':[]},
    # response:  MAYBE the  server CANNOT be recognized the format.

    # S3:
    post_data_3 = {'id':1, 'name':'a', 'list':[]}
    requests.post('fake_url', data='', json=post_data_3)
    # request:   data is {'id':1, 'name':'a', 'list':[]},
    # response:  MAYBE the server ONLY recognize this JSON format. Such as Ant.Design.

    # S4:
    post_data_4 = json.dumps({'id':1, 'name':'a', 'list':[]})
    requests.post('fake_url', data='', json=post_data_4)
    # Error: format is wrong


if __name__ == '__main__':
    post_issue()