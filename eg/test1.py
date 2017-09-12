import urllib2
import lxml.html
import re
f = file('html2.txt','r')
html = f.read()
f.close
'''
tree = lxml.html.fromstring(html)
fixed_html = lxml.html.tostring(tree,pretty_print=True)
print fixed_html
tree1 = lxml.html.fromstring(fixed_html)
td = tree1.cssselect('title')[0]
print td
text2 = td.text_content()
print text2.encode('UTF-8')
'''

ans = re.findall('S0,P(.+?)\(Bp.+?faulted due to SFP validation failure.',html)
print ans
list1 = list(ans)
list2 = set(list1)
print len(list1)
print len(list2)
print list2

