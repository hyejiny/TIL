쿼리 : 데이터 베이스에 보내는 명령어

데이터 베이스는 테이블들의 집합



열 = 필드

행 = 레코드



### model

* DB에 데이터를 저장하고 가져오는 것

* SQL

* ORM

  * 쿼리를 python 에서 object로 사용할 수 있게 해줌.

* `models.py`에 모델 클래스를 정의 해서 사용 할 수 있음.

  * class 테이블명(models.Model)

    title =  models.CharField(max_length=100):

    * 자주 사용하는 필드명 : charfield/datetimefield/textfield/integerfield/booleanfield/...
    * django 공식 문서 model field라고 구글링하면 찾을 수 있음.



#### db 생성

* 클래스를 다 정의를 하면 해야만 하는 일!!!
  * makemigrations
    * python manage.py makemigrations (app 이름)
    * DB에 적용하기 위한 설계도를 제작
    * app 이름을 뒤에 적으면 해당 app에 있는 models.py의 내용만 설계도를 만듦.
  * migrate
    * python manage.py migrate
    * 만들어진 설계도를 가지고 DB에 테이블을 생성
    * app 이름을 적으면 해당 app에 있는 migration 파일을 db에 적용시킴
  * showmigrations
  * sqlmigrate



#### db 사용

* db api

  ```select
  모델클래스이름.objects.QuerySetAPI
  
  Article(class).objects(manager).all(queryset api)()
  *objects s까먹지 말기!!
  ```



pip install ipython django-extensions



INSTALLED_APPS = [

  'articles',

  'django_extensions'



$ python manage.py shell

$ python manage.py shell_plus



Article.objects.all()  : 데이터 베이스 조회

여기서 object를 읽을 수 있게 설정하는 방법: modes.py에서 클래스 안에서

def  __ str __(self):

return self.title / return f'{slef.pk}번 글의 제목은{self.title}'

데이터 베이스 설계도에 영향을 주지는 않음. 그래서 makemigrations필요 없음.

db api로 crud를 할 것이다. read = 조회

create 생성 read읽기 update갱신 delete삭제 (기본적인 데이터 처리 기능)



article = Article()

article 객체 생성



article.title = 'first'

article.content = 'django!'

article.save() : 반드시 해야 데이터 베이스 테이블에 작성이 됨.



#두번째 방법

article = Article(title='second',content='django!')



article.pk #2

article.title

article.content



#세번째 방법

Article.objects.create(title='third',content='django!!')

save 안해도 create가 해줌 



.get : 보통 pk조회 할 때

.filter : 조건 맞으면 조회



admin page 조작

python manage.py createsuperuser

python ma~ runserver

앱에 admin.py 들어가서 

from models import Article #명시적 상대경로 표현

admin.site.register(모델명Ariticle)

