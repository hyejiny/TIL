## Module

* 모듈 : 특정 기능을 하는 변수, 함수, 클래스 코드를 .py나 스크립트 단위로 작성
* 패키지 : 특정 기능과 관련된 여러 모듈의 집합. (서브 패키지를 포함할 수 있음)
* 라이브러리 : 모듈과 패키지들의 집합(파이썬 표준 라이브러리 PSL)
* 패키지 관리자(pip) :  외부 패키(pypi)를 설치할 수 있도록 도와주는 패키지



#### 모듈의 활용

* `import`를 통해서 모듈을 이름 공간으로 가져와야 한다.
* `import 모듈명`
* `from 모듈명 import  변수, 함수, 클래스`
* `from 모듈명 import *`



### 패키지

* 점(.)으로 구분된 모듈 이름(패키지명.모듈명)을 써서 모듈을 구조화 하는 방법
* ` from 패키지명 import 모듈명` 
  * 모듈명.변수명,  모듈명.함수명, 모듈명.클래스명

* `form 패키지명 import 모듈명 as 별명`
  * 별명.변수명, 별명.함수명, 별명.클래스명

* `from 패키지명.모듈명 import 변수명, 함수명, 클래스명`
  * 변수명, 함수명, 클래스명
* `from 패키지명.모듈명 import *`

```python
import datetime #모듈
print(datetime.datetime.now()) #모듈.클래스.변수

from datetime import datetime
print(datetime.now())

from datetime.datetime import now # error 매서드는 불러올 수 없다. (함수는 불러올 수 있음)

```



#### 모듈을 찾는 순서

1. 실행하는 파일의 경로에서 import하는 모듈을 검색
2. 파이썬에서 제공하는 경로에서 모듈을 검색
3. 외부 패키지에서 모듈을 검색



