from bs4 import BeautifulSoup
import requests
url = 'http://www.baidu.com'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,'html.parser')
print soup.title

