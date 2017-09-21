#-*- coding:utf-8 -*-
import requests
import urllib2
import os
import re
import sys
url_begin = 'https://mm.taobao.com/self/model_album.htm?spm=719.7800510.a312r.16.OHCak4&user_id=290551947'
url_eg = 'https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20=695679842'
def DownloadUrl(url):
	r = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"})
	r.raise_for_status
	r.encoding = r.apparent_encoding
	return r.text.encode('utf-8')

def ReHtml(html):
	re1 = r'''<h4><a href="(.+?)" target="_blank">'''
	re2 = re.findall(re1,html)
	return re2

def DownloadUrl2(url):
	q = urllib2.request(url)
	q.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
	m = urllib2.urlopen(q)
	return m.read()

def SaveFile(html):
	path = '/mnt/d/库文件/工作区/缓存/git/hello-world/study/11.txt'
	if os.path.exists(path):
		os.remove(path)
		print 'rm the file'
	with open(path,'wb') as f:
		while(1):
			f.write(html.pop()+'\n')
			if html == []:
				break
		f.close()
		print 'file is saved successfully'

if __name__ == '__main__':
	print sys.getdefaultencoding()
	reload(sys)
	sys.setdefaultencoding('utf-8')
	print sys.getdefaultencoding()
	html = DownloadUrl(url_eg)
	re2 = ReHtml(html)
	print type(re2)	
	print re2
	re3 = []
	for item in re2:
		re3.append('http:'+item)
	print re3
	SaveFile(re2)
	re3 = ReHtml(html)


