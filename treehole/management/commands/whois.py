#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Jun 11 18:17 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from argcmd.management.base import BaseCommand
from argcmd import make_option
from treehole.models import ContentModel

class Command(BaseCommand):
    arg_list = BaseCommand.arg_list + (
            make_option('id', type=int), )
    def handle(self, *v, **u):
        args = self.arguments
        assert(args.id)
        print ContentModel.objects.get(id=args.id).ip
