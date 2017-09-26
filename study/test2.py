import requests
import sys
import json
import chardet
def ChangeType():
	print sys.getdefaultencoding()
	reload(sys)
	sys.setdefaultencoding('utf-8')
	print sys.getdefaultencoding()

ChangeType()
url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
html = requests.get(url)
html.encoding = html.apparent_encoding
print type(html.text)
html1 = html.text.encode('utf-8')
js1 = json.loads(html1,encoding='utf-8')['data']['searchDOList']
for i in js1:
	print i['userId']
print len(js1)
'''
#print chardet.detect(js2)
with open('html.txt','wr') as f:
	json.dump(js1,f)
	f.close()

case_list_righ = str(case_list).replace('u\'','\'')
print case_list_righ.decode("unicode-escape")
'''
