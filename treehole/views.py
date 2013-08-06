#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Mar 20 18:38 by BlahGeek@Gmail.com

import sys
import logging
import random
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.views.decorators.cache import cache_page
from django.contrib import messages
from treehole.models import ContentModel, PlaceholderModel
from treehole.utils import checkIP, postStatu, MSG, COLORS
from treehole.utils import needRecaptchar, validRecaptcha
from treehole.settings import LINKS
from treehole.settings import RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY

@cache_page(60 * 60)
def chart_day(req):
    now = datetime.now()
    today = datetime(now.year, now.month, now.day)
    data = {}
    for i in range(1, 30):
        start = today - timedelta(days=i)
        data[start.strftime('%Y-%m-%d 00:00:00 +0800')] = ContentModel.objects.filter(time__range=\
                (start, start+timedelta(days=1))).count()
    return render_to_response('chart.html', 
            {'data': data, 'TITLE': '树洞过去一个月发布统计', 
                'TIME': now.strftime('%Y-%m-%d %H:%M')}, 
            context_instance=RequestContext(req))

@cache_page(60 * 15)
def chart_hour(req):
    now = datetime.now()
    today = datetime(now.year, now.month, now.day, now.hour)
    data = {}
    for i in xrange(1, 24):
        start = today - timedelta(hours=i)
        data[start.strftime('%Y-%m-%d %H:00:00 +0800')] = ContentModel.objects.filter(time__range=\
                (start, start+timedelta(hours=1))).count()
    return render_to_response('chart.html', 
            {'data': data, 'TITLE': '树洞过去一天发布统计', 
                'TIME': now.strftime('%Y-%m-%d %H:%M')}, 
            context_instance=RequestContext(req))

def index(req):
    ipaddr = req.META.get('REMOTE_ADDR', '')
    _content = ''
    _need_recaptcha = False
    if req.method == 'POST':
        _content = req.POST.get('content', '')
        _need_recaptcha = needRecaptchar(ipaddr, _content)
        if _need_recaptcha and len(req.POST.get('recaptcha_challenge_field', '')) == 0:
            messages.error(req, MSG['RECAPTCHA_NEEDED'])
        elif _need_recaptcha and not validRecaptcha(
                req.POST.get('recaptcha_challenge_field', ''), 
                req.POST.get('recaptcha_response_field'), 
                RECAPTCHA_PRIVATE_KEY, ipaddr):
            messages.error(req, MSG['RECAPTCHA_INCORRECT'])
        elif not checkIP(ipaddr):
            messages.error(req, MSG['IP_NOT_VALID'])
        elif not (len(_content) < 120 and len(_content) > 5):
            messages.error(req, MSG['CONTENT_TOO_LONG'])
        elif ContentModel.objects.filter(ip=ipaddr, time__range=\
                (datetime.now()-timedelta(minutes=30), datetime.now())).count() > 0:
            messages.error(req, MSG['TOO_MANY_TIMES'])
        else:
            try:
                postStatu(_content, ipaddr)
            except:
                messages.error(req, MSG['PUBLISH_ERROR'])
                logging.error('Error in ' + str(ContentModel.objects.count()))
            else:
                messages.success(req, MSG['PUBLISH_OK'])
                _content = ''

# for doreamon icon
    try:
        icon = int(req.path[1:])
    except ValueError:
        icon = 0
    tourl = ''
    if icon == 0 or req.session.get('redirect', 0) == 0:
        req.session['redirect'] = 1
        tourl = '/' + str(random.randint(1, 16))
    else:
        req.session['redirect'] = 0
    isIphone = ('iPhone' in req.META.get('HTTP_USER_AGENT', '') and req.method == 'GET')
    return render_to_response('index.html', \
            {'ICO_NUM': icon, 'TOURL': tourl, 'ISIPHONE': isIphone, 
                'LINKS': LINKS, 
                'PLACEHOLER': PlaceholderModel.objects.order_by('?')[0].content, 
                'content': _content, 
                'RECAPTCHA_PUBLIC_KEY': RECAPTCHA_PUBLIC_KEY, 
                'need_recaptcha': _need_recaptcha, 
                'COLOR': random.choice(COLORS)}, 
            context_instance=RequestContext(req))
