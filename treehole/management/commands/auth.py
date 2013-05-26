#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 26 11:58 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from argcmd.management.base import BaseCommand
from treehole.renren import RenRen
from treehole.settings import PAGE_ID

class Command(BaseCommand):
    def handle(self, *v, **u):
        r = RenRen(PAGE_ID)
        r.auth()
