#!/usr/bin/env python
# -×- coding:utf-8 -*-

import urllib2,urllib3

def getUrlList():
    html = urllib2.urlopen('https://mm.taobao.com/search_tstar_model.htm?spm=5679.126488.640745.2.b17c0adm32BOO')
    print html.read().decode('gbk').encode('utf-8')

getUrlList()
