# coding:utf-8
"""
@file: t_requests.py
@time: 11/17/2019 10:57 PM
@contact: dabuwang
"""

import requests
import json


def basic_usage():
    url = "http://www.python.org"
    response = requests.get(url)
    print "Headers response: "
    for header, value in response.headers.items():
        print header, '-->', value

    print "Headers request: "
    for header, value in response.request.headers.items():
        print header, '-->', value


def get_usage():
    response = requests.get("http://httpbin.org/get", timeout=20)
    # we then print out the http status_code
    print("HTTP Status Code: " + str(response.status_code))
    print(response.headers)
    if response.status_code == 200:
        results = response.json()
        for result in results.items():
            print(result)

        print("Headers response: ")
        for header, value in response.headers.items():
            print(header, '-->', value)

        print("Headers request : ")
        for header, value in response.request.headers.items():
            print(header, '-->', value)
        print("Server:" + response.headers['server'])
    else:
        print("Error code %s" % response.status_code)


def post_usage():
    data_dictionary = {"id": "0123456789"}
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    url = "http://httpbin.org/post"
    response = requests.post(url, data=data_dictionary, headers=headers)
    print response.json()

def proxy_except_usage():
    http_proxy = "http://<ip_address>:<port>"
    proxy_dictionary = {"http": http_proxy}
    response = requests.get("http://example.org", proxies=proxy_dictionary)

    response.raise_for_status()

if __name__ == '__main__':
    # basic_usage()
    # get_usage()
    post_usage()
