#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Mar 20 19:50 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

import logging
from treehole.renren import RenRen
from treehole.settings import COOKIE, PAGE_ID
import os
from ipaddr import IPNetwork, IPAddress

def checkIP(addr):
    IPS = (
            IPNetwork('59.66.0.0/16'), 
            IPNetwork('166.111.0.0/16'), 
            IPNetwork('101.5.0.0/16'), 
            IPNetwork('219.223.160.0/19'), 
            # private address
            IPNetwork('127.0.0.0/8'), 
            IPNetwork('10.0.0.0/8'), 
            IPNetwork('192.168.0.0/16'), 
            )
    return any([IPAddress(addr) in x for x in IPS])

def postStatu(status, number):
    text = '#' + str(number) + ' ' + status
    r = RenRen(PAGE_ID)
    r.loginByCookie(COOKIE)
    r.setStatu(text)

MSG = {
        'IP_NOT_VALID': '不允许您的IP发布', 
        'CONTENT_TOO_LONG': '状态长度应该在6-100字之间', 
        'TOO_MANY_TIMES': '每个IP相邻发布时间不能小于30分钟', 
        'PUBLISH_ERROR': '服务器错误，发布失败', 
        'PUBLISH_OK': '发布成功！'}

PLACEHOLDERS = (
        'Lolita, light of my life, fire of my loins, my sin, my soul.  --纳博科夫《洛丽塔》', 
        'I wish I knew how to quit you. --《断背山》', 
        '看着我吧，不要说话。 --幸福大街《粮食》', 
        '只要恋人的脸熟记于心，世界就还是我的家。 --帕慕克《我的名字叫红》', 
        '草在结它的种子，风在摇它的种子。我们站着，不说话，就十分美好。 --顾城《门前》', 
        '从此飘蓬十年后，可能重对旧梨涡。 --黄景仁《绮怀》', 
        '命运将我们两个互不相干的生命，丝丝缕缕编成一个血红的图案。 --王尔德《自深深处》', 
        )
