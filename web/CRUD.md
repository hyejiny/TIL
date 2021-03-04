#### TEMPLATE확장 사용하기



base.html 생성하고 원하는 위치에 templates 폴더 안에 위치시킨다.

* base.html에는 기본 html DOM트리를 구성한다.
* bootstrap CDN을 복붙 해준다.
* block을 body 안에 적절한 곳에 위치 시켜준다.

settins.py에 base.html의 경로를 등록한다.

* templates라는 곳에 있는 dirs에 그 경로를 추가해 준다. 

* base.html이 있는 경로를 base_dir로 부터 설정해주면 된다.

* dirs : [base_dir / 'workshop_sol'/'templates'] : django 3.xx 사용

  

확장하고 사용한다. 

1. 가장 첫번째 줄에 {% extends 'base.html' %}을 해준다.
2. 그 다음 block을 위치 시키고 block  안에 적절히 꾸며 주면 된다. 



-----------------

### CRUD

#### read

* DB에 전체 글 목록을 가져와서 page에 보여주자.
* Article.object.all()의 QuerySet을 그대로 context에 담아서 template 파일에 전달
* template은 for 문으로 하나씩 db값을 접근 가능하고, `.`연산자를 이용해서 값에 접근도 가능.



### create

* form 태그에서 데이터를 전달하고, 
* 그 데이터를 3가지 저장 방법 중 1개의 방법으로 db에 저장하면 끝!!
* GET/POST
  * GET : 주소줄에 쿼리 스트링 형식으로 데이터가 전달. 전달 하는 길이가 한계가 있음(255자)
    * 주로 데이터 정보를 가져올 때 사용(즉, 데이터를 조회 할 때 이용)
  * POST : 패킷 바디 안에 데이터가 전달. 좀 더 많은 양의 데이터를 전달 할 수 있음.
    * 주로 데이터의 정보를 생성, 수정, 삭제 할 때 사용.
  * GET/article/ : article의 정보를 조회
  * POST/article/ : article을 생성.
  * POST/article/1 : article을 수정.
  * REST API : 나중에 수업할 예정.



* method 를 POST로 변경 할 때 해야할 일!
  * CSRF : Form tag 사이에 {% csrf_token %} 추가.
  * request.GET을 request.POST로 변경
* Redirect() : 이미 만들어진 페이지로 경로 재설정





---------------------

### UPDATE

* 글 제목을 클릭 했을 때 해당 글만 보여지는 페이지
* detail 페이지를 먼저 만들자!
  * 어떠한 글의 detail 페이지인지 해당 글의 정보(pk)가 필요함.
  * 글의 정보를 동적 라우팅 방법으로 주소로 전달. 
  * 주소로 전달 받은 글의 pk값을 가지고 DB에서 데이터를 가져옴.
  * 가져온 데이터를 template 파일에서 보여주면 그것이 detail page!!
* detail페이지 하단에 수정하기 링크를 만들어 준다. 
  * 수정하기 링크는 edit하는 페이지를 보여주면 된다. 
  * create 방법과 유사하게 form을 보여주는데
  * 차이점은 해당 글의 data 를 같이 넘겨주고 그 데이터를 같이 보여주는게 차이점. 
  * 수정하기 최종 버튼을 눌렀으면 post 방식으로 DB에 적용을 시켜주면 끝
  * 이 때 필요한 정보(PK)도 주소 줄을 이용해서 전달한다.
* DB에 적용시키는 방법은
  * 해당 pk를 가지는 데이터를 불러오고
  * 값을 수정하고
  * save 한다. 
* 끝나면 detail page로 redirect 시키면 끝!!



---------------------

#### DELETE

* 삭제하기 버튼을 누르면 삭제할 글의 PK가 같이 주소로 전달되고 
* view.py에서 해당 pk 값의 정보를 가져온 다음에 delete 함수를 호출하면 끝!