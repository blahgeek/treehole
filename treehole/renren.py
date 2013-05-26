#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 26 10:07 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

import os
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run
import httplib2
import requests
from .settings import DJANGO_ROOT_DIR, FLOW, CRE_STORAGE

class RenRen:

    def __init__(self, pageid):
        self.pageid = pageid
        self.storage = Storage(CRE_STORAGE)
        self.cre = self.storage.get()

    def auth(self):
        run(FLOW, self.storage)

    def postStatus(self, text):
        assert(self.cre is not None)
        if self.cre.access_token_expired:
            # refresh token
            http = httplib2.Http()
            http = cre.authorize(http)
            self.cre.refresh(http)
        r = requests.post('https://api.renren.com/restserver.do', 
                {
                    'v': '1.0', 
                    'access_token': self.cre.access_token, 
                    'format': 'json', 
                    'method': 'pages.setStatus', 
                    'page_id': str(self.pageid), 
                    'status': text
                    })
        # for different versions of requests
        j = r.json() if hasattr(r.json, '__call__') else r.json
        assert(j['result'] == 1)
