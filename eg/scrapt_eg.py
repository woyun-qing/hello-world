import builtwith
import urllib2
import sys
import urlparse
import re

def download(url,user_agent='wswp',num_tries=2):
	print 'downloading url:',url
	headers = {'User_agent':user_agent}
	request = urllib2.Request(url,headers=headers)
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'download error:',e.error
		html = None
		if num_tries > 0:
			if hasattr(e,'code') and 500 <= e.code <600:
				return download(url,num_tries-1)
	return html

def crawl_sitemap(url):
	sitemap = download(url)
	links = re.findall('<loc>(.*?)</loc>',sitemap)
	for link in links:
		html = download(link)

def link_crawler(seed_url,link_regex):
	crawl_queue = [seed_url]
	seen = set(crawl_queue)
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)
		for link in get_link(html):
			if re.match(link_regex,link):
				link = urlparse.urljoin(seed_url,link)
				if link not in seen:
					seen.add(link)
					crawl_queue.append(link)

def get_link(html):
	

print download('http://www.baidu.com')
