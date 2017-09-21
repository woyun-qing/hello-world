import requests
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
	r = requests.get(url)
	r.raise_for_status
	r.encoding = r.apparent_encoding
	print r.text[:1000]
except:
	print 'scrapy fault'

'''
r = requests.get(url)
print r.status_code
r.encoding = r.apparent_encoding
print r.text

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print r.encoding
except:
    print 'scrapy fault'
'''