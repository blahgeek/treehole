#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Apr 28 16:06 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')


from argcmd.management.base import BaseCommand
from treehole.models import PlaceholderModel
from datetime import datetime
from argcmd import make_option

class Command(BaseCommand):
    'Placeholer manager.'

    arg_list = BaseCommand.arg_list + (
            make_option('-l', '--list', 
                    action='store_true', 
                    help='List all placeholers.'), 
            make_option('-a', '--add', 
                    type=str, help='Add a placeholer.', 
                    default=''), 
            make_option('-d', '--delete', 
                    type=int, help='Delete the oldest N placeholders.', 
                    default=0), 
            )

    def handle(self, *v, **u):
        args = self.arguments

        if args.list:
            for i in PlaceholderModel.objects.order_by('time').all():
                print i.content

        if args.add:
            m = PlaceholderModel(content=args.add, 
                                 time=datetime.now())
            m.save()

        if args.delete:
            for i in PlaceholderModel.objects.order_by('time')[:args.delete]:
                i.delete()
