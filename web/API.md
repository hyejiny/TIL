* 컴퓨터와 컴퓨터를 연결하기

* 내컴퓨터 -요청(request)->  하면 상대방 컴퓨터에서 -응답(response)>
* 우리가 사용하는 요청 프로그램 : 웹브라우저, 크롬 등



### API

> 사용자가 서버로부터 데이터를 보다 편리하게 가져올 수 있도록 만들어주는 인터페이스

URL =  어디로

요청 파라미터 = 무엇을 가지고



* 인터페이스 

  * 요청

  * 응답

```text
- http : http방식으로 보낼 것이다.

- www. kobis.or.kr 주소

- 여러개의 / 통해 단어들이 등장 

- ? 기준으로 끊어 읽을 수 있다.  어디로 ->?->무엇을

- key와 value 쌍은 &로 구분된다. 
```





* 파이썬 코드를 통해서 요청을 보내기 위해 requests 라이브러리 활용

pip install requests

```python
import requests
url = 주소
payload = ?이후의 값을 가져와서 딕셔너리로 만들어주기
response = requests.get(url,params = payload)
reponse.json() # 이것의 타입은 딕셔너리이다. 

print(response.url) # url 받아오기
print(respense.text) #json구조로 받아옴 / 이것의 타입은 str이다. 
```

```python
#kobis.py
class URLMaker:
    url = 공통으로 가진 부분까지의 주소
    
    def __init__(self, key):
        self.key = key
        
    def get_url(self, category, feature):
        return f'{self.url}/{category}/{feature}.json?key={self.key}'
    
url_maker = URLMaker('키 값')
url_maker.get_url('boxoffice','serch~~~')
print(url_maker.key)
```





## 실습

```python
import requests
from kobis import URLMaker

def sales():
    
#url 생성(첫번째 방법)  
url_maker = URLMaker('키값')
url = url_maker.get_url('boxoffice','serch~~~')

payload = {
    'targetDt':'~~'
}
r = requests.get(url, params=payload)
print(r) #reponse 객체 출력
movies_dict = r.json()
print(r.url) #경로 출력됨. -> 크롬에서 확인 가능

#url 생성(두번째 방법)
url_1 = f'{url}&peopleNm={people}&filmoNames={movie}'


movies = movies_dict.get('1번째 경로').get('2번째 경로') #json 통해 경로 파악
result = []
for movie in movies:
    result.append(movie.get('salesamt'))
    
return result
    
```



* cf ) 프로젝트 예시 확인하기