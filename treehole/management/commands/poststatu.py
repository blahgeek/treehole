#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 06 21:48 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from argcmd.management.base import BaseCommand
from argcmd import make_option
from treehole.utils import postRawStatu, postStatu

class Command(BaseCommand):

    arg_list = BaseCommand.arg_list + (
            make_option('-r', '--raw', 
                    action='store_true', 
                    help='Post without number, nor saving to database.'), 
            make_option('content', metavar='CONTENT', 
                    type=str, help='Post statu.'), 
            )

    def handle(self, *v, **u):
        args = self.arguments
        
        assert(args.content)
        if args.raw:
            postRawStatu(args.content)
        else:
            postStatu(args.content)
