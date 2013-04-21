#-*-coding:utf-8-*-

import requests
import simplejson
import re
import random
import urllib
import os
import sys


class RenRen:

    def __init__(self, pageid):
        self.session = requests.Session()
        self.token = {}
        self.pageid = pageid

    def loginByCookie(self, cookie_path):
        with open(cookie_path) as fp:
            cookie_str = fp.read()
            cookie_dict = dict([v.strip().split('=', 1) for v in cookie_str.strip().split(';')])
            self.session.cookies = requests.utils.cookiejar_from_dict(cookie_dict)
        self.getToken()

    def getToken(self):
        p = re.compile("get_check:'(.*)',get_check_x:'(.*)',env")
        r = self.get('http://page.renren.com/%s/fdoing' % self.pageid)
        result = p.search(r.text)
        self.token = {
            'requestToken': result.group(1),
            '_rtk': result.group(2)
        }

    def request(self, url, method, data={}):
        if data:
            data.update(self.token)
        if method == 'get':
            return self.session.get(url, data=data)
        elif method == 'post':
            return self.session.post(url, data=data)

    def post(self, url, data={}):
        return self.request(url, 'post', data)

    def get(self, url, data={}):
        return self.request(url, 'get', data)

    def setStatu(self, text):
        try:
            response = self.post('http://page.renren.com/doing/update', 
                    {'pid': self.pageid, 'c': text}).json()
            assert(response['code'] == 0)
        except (AssertionError, simplejson.JSONDecodeError):
            raise RuntimeError('Set status error')

    def postWallStatu(self, text, wallid):
        try:
            response = self.post('http://w.renren.com/wall/%s/publish' % str(wallid), 
                    {'channel': '0', 
                     'content': text, 
                     'isSync': '1', 
                     'referId': '', 
                     'hasImage': '0'}).json()
        except (AssertionError, simplejson.JSONDecodeError):
            raise RuntimeError('Set status error')


if __name__ == '__main__':
    r = RenRen('601677049')
    r.loginByCookie('cookie.txt')
    print r.postWallStatu(sys.argv[1], sys.argv[2])
