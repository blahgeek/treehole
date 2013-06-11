#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Jun 11 18:17 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from argcmd.management.base import BaseCommand
from argcmd import make_option
from treehole.models import BlockIpModel

class Command(BaseCommand):
    arg_list = BaseCommand.arg_list + (
            make_option('ip', type=str), 
            make_option('-r', '--remove', action='store_true', help='Delete this entry'))
    def handle(self, *v, **u):
        args = self.arguments
        assert(args.ip)
        if args.remove:
            BlockIpModel.objects.filter(ip=args.ip).delete()
        else:
            new_entry = BlockIpModel(ip=args.ip)
            new_entry.save()
