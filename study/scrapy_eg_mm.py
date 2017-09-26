#-*- coding:utf-8 -*-
import requests
import urllib2
import os
import re
import sys
url_begin = 'https://mm.taobao.com/self/model_album.htm?spm=719.7800510.a312r.16.OHCak4&user_id=290551947'
url_eg = 'https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20=695679842'
url_pic = r'https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id=695679842&album_id=10000269840&top_pic_id=0&cover=%2F%2Fimg.alicdn.com%2Fimgextra%2Fi1%2F695679842%2FTB1N7JyIpXXXXblaXXXXXXXXXXX_!!695679842-0-tstar.jpg&page=1&_ksTS=1506008049827_154&callback=jsonp155'
#下载网页
def DownloadUrl(url):
	r = requests.get(url)
	r.raise_for_status
	r.encoding = r.apparent_encoding
	return r.text.encode('utf-8')
#正则筛选链接
def ReHtml(html):
	re1 = r'''<h4><a href="(.+?)" target="_blank">'''
	re2 = re.findall(re1,html)
	return re2
#urllib2下载网页
def DownloadUrl2(url):
	q = urllib2.request(url)
	q.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
	m = urllib2.urlopen(q)
	return m.read()
#保存网址到11.txt文件中
def SaveFile(list1):
	path = '/home/roy/Desktop/git/hello-world/study/11.txt'
	if os.path.exists(path):
		os.remove(path)
		print 'rm the file'
	with open(path,'wb') as f:
		while(1):
			f.write(list1.pop()+'\n')
			if list1 == []:
				break
		f.close()
		print 'file is saved successfully'

def SaveFile1(str):
	path = '/home/roy/Desktop/git/hello-world/study/12.txt'
	if os.path.exists(path):
		os.remove(path)
		print 'rm the file'
	with open(path,'wb') as f:
		r = requests.get(str)
		r.encoding = r.apparent_encoding
		f.write(r.text)
		f.close
		print 'save successful'

#调整系统字符
def ChangeType():
	print sys.getdefaultencoding()
	reload(sys)
	sys.setdefaultencoding('utf-8')
	print sys.getdefaultencoding()
#格式化抓取信息
def HttpAdd(re):
	re1 = []
	for item in re:
		re1.append('http:'+item)
	return re1
#主程序
if __name__ == '__main__':
	ChangeType()
	html = DownloadUrl(url_eg)
	re2 = ReHtml(html)
	list1 = HttpAdd(re2)
	SaveFile1(list1.pop())

	


