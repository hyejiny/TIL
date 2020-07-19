import requests
from bs4 import BeautifulSoup

url = 'https://www.daum.net/'

req = requests.get(url)

data = BeautifulSoup(req.content,'html.parser')


select = data.select_one('#wrapSearch > div.slide_favorsch > ul:nth-of-type(1) > li:nth-of-type(1) > a')
select2 = data.select('#wrapSearch > div.slide_favorsch')

print(select)
print(select2)