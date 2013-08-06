#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 26 10:07 by BlahGeek@Gmail.com

import os
import httplib2
import requests
from bs4 import BeautifulSoup
from .settings import COOKIR_PATH

BASE_URL = 'http://3g.renren.com/status/newstatus.do'

class RenRen:

    def __init__(self):
        self.session = requests.Session()
        cookie = open(COOKIR_PATH).read()
        cookie = [x.strip() for x in cookie.split(';') if x]
        cookie = map(lambda x: x.split('=', 1), cookie)
        cookie = dict(cookie)
        self.session.cookies = requests.utils.cookiejar_from_dict(cookie)

    def postStatus(self, text):
        soup = BeautifulSoup(self.session.get(BASE_URL).content)
        form = soup.find('form')
        assert(form is not None)
        values = map(lambda x: (x['name'], x['value']), form.findAll('input', type='hidden'))
        data = {'status': text}
        data.update(dict(values))
        req = self.session.post(form['action'], data)
        # save cookie
        with open(COOKIR_PATH, 'w') as f:
            cookie = requests.utils.dict_from_cookiejar(self.session.cookies)
            cookie = '; '.join([k+'='+v for k, v in cookie.items()])
            f.write(cookie)
