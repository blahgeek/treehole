#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Apr 18 14:50 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')


from django.core.management.base import BaseCommand
from treehole.settings import PAGE_ID, COOKIE
from treehole.renren import RenRen

class Command(BaseCommand):

    def handle(self, *v, **u):
        r = RenRen(PAGE_ID)
        r.loginByCookie(COOKIE)
