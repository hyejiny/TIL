import requests
from bs4 import BeautifulSoup
url = 'https://finance.naver.com/sise/'
response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

select = data.select_one('#KOSPI_now')
#select 는 여러개를 리스트 형태로 반환
print(select.text)