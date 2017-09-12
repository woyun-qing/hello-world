import builtwith
import urllib2
import re
def download(url,user_agent = 'wswp',num_retries = 2):
	print 'Downloading',url
	headers = {'User-agent':user_agent}
	request = urllib2.Request(url,headers = headers)
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'Download error',e.reason
		html = None
		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				return download(url,num_retries-1)
	return html

def link_crawler(seed_url,link_regex):
	crawl_queue = [seed_url]
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)
		for link in get_links(html):
			if re.match(link_regex,link):
				crawl_queue.append(link)

def get_links(html):
	webpage_regex = re.compile()


