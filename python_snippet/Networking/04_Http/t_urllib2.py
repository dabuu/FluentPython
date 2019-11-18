# coding:utf-8
"""
@file: t_urllib2.py
@time: 11/17/2019 9:47 PM
@contact: dabuwang
"""

import re
import urllib2
from urllib2 import HTTPError, URLError
from HTMLParser import HTMLParser


def urllib2_get_response():
    """
    urlopen
    response method: read(), status, code
    :return:
    """
    try:
        # response = urllib2.urlopen("http://www.python.org")  # response is http.client.HTTPResponse class
        response = urllib2.urlopen("http://www.sohu.com")  # response is http.client.HTTPResponse class
        print response.code
        # print response.headers

        print response.info()  # same to headers
        print response.info().keys()
        print response.info()['x-from-sohu']

        print response.read()
        response.close()
    except HTTPError, e:
        print '[-]\t http error: %s' % e.code
    except URLError, e:
        print '[-]\t url error: %s ' % e.reason


def urllib2_custom_request():
    # url = "http://www.python.org"
    url = "https://www.packtpub.com/books/info/packt/terms-and-conditions"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'}
    request = urllib2.Request(url, headers=headers)
    # ↑↑  before urlopen method, add headers in request
    # urlopen not open a url, rather than one Request Class

    response = urllib2.urlopen(request)
    if response.code == 200:
        print(response.headers)

    # use regex to find email address
    content = response.read()
    pattern = re.compile(r"[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+")
    mails = pattern.findall(content)
    print "mails:\t %s" % repr(mails)


class UrlParser(HTMLParser):

    all_urls = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        for k,v in attrs:
            if k == 'href' and v.find('http') >= 0:
                print(v)
                self.all_urls.append(v)

    # def handle_starttag(self, tag, attrs):
    #     if tag == "a":
    #         for a in attrs:
    #             if a[0] == 'href' and a[1]:
    #                 link = a[1]
    #                 if (link.find('http') >= 0):
    #                     print(link)
    #                     self.all_urls.append(link)
                        # newParse = UrlParser()
                        # newParse.feed(link)


def html_parser():
    # url = "http://www.python.org"
    url = "http://www.sohu.com"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    parser = UrlParser()
    parser.feed(response.read().decode('utf-8'))
    print "count: %d" % len(parser.all_urls)


if __name__ == '__main__':
    # urllib2_get_response()
    # urllib2_custom_request()
    html_parser()