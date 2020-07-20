# python 기초

> 파이썬에서 제공하는 스타일 가이드 [PEP-8](https://www.python.org/dev/peps/pep-0008/) 참고할 것



## 1. 기초 문법(Syntax)

* **주석(Comment)**

  * 한 줄 주석은 `#`

  * 여러 줄의 주석은 `""" 또는 '''`

* **코드 라인**
  * `1줄에 1문장`이 원칙이다.
  * `[]` `{}` `()`는 `\` 없이도 여러 줄 작성이 가능하다.



## 2. 변수(Variable)

#### 2.1 할당 연산자 :  `=`

* 변수는 =을 통해 할당(assignment)된다.
* `type()` : 데이터 타입 확인
* `id()` : 해당 값의 메모리 주소 확인 (컴퓨터 공간 안의 주소)

```python
# 같은 값 동시에 할당
x = y = 'ssafy'

# 다른 값 동시에 할당 (변수, 값의 개수 동일해야 함)
a, b = 2020, 4

# 서로 값 바꾸기 활용
a, b = 1, 2
a, b = b, a
```

#### 2.2 식별자(Identifiers)

> 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름이다.

* 영문알파벳, 밑줄(_),숫자로 구성

* 대소문자 구별

* 예약어 사용 불가

  ```python
  #예약어 확인
  import keyword
  print(keyword.kwlist)
  ```

* 내장함수나 모듈 등의 이름으로도 만들면 안된다. 

  ```python
  print = 'hi' 
  # 이후에 print는 'hi'라는 값으로 인식되어 이전의 기능을 수행하지 못한다.
  ```



## 3. 데이터 타입

#### 3.1 숫자(Number) 타입

​	**(1) int (정수, ingteger)**

​	cf ) 파이썬에서 표현할 수 있는 가장 큰 수 

​           : arbitrary-precision arithmetic를 사용하기 때문에 정수 자료			형에서 오버플로우가 없다.

* 오버플로우

  - 데이터 타입 별로 사용할 수 있는 메모리의 크기가 제한되어 있다.
  - 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면, 기대했던 값이 출력되지 않는 현상, 즉 메모리가 차고 넘쳐 흐르는 현상

* arbitrary-precision arithmetic

  * [파이썬에서 아주 큰 정수를 표현할 때 사용하는 메모리의 크기 변화](https://mortada.net/can-integer-operations-overflow-in-python.html)
  * 사용할 수 있는 메모리양이 정해져 있는 기존의 방식과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태
  * 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 더 부족하면 6바이트까지 사용할 수 있게 유동적으로 운용

  ``` python
  import sys #가장 큰 숫자
  print(sys, maxsize)
  
  binart_number = 0b10 #0b = 이진수
  octal_number = 0o10 #팔진수
  hexadecimal_number = 0x10 #16진수
  ```



​	**(2) float(부동소수점, 실수)**

> 컴퓨터는 실수를 표현할 때(2진수 사용) 부동소수점을 사용하기 때문에, 항상 같은 값으로 일치되지 않는다. 

```python
3.5 - 3.2 == 0.3 #False
round(3.5 - 3.2,2) == 0.3 #True

a = 3.5-3.2
b = 0.3
a==b #False
```

`round() ` : round() 는 0~4는 내림, 5는 동일하게 작동하지 않고 반올림 방식에 따라 다르다. (짝수에서 5는 내림 / 홀수에서 5는 올림)



* 실수를 근삿값으로 표현하기 때문에 부동소수점 반올림 오차가 발생한다. 따라서, 실수를 비교할 때는 연산한 값과 비교할 값의 차이를 구한 뒤 `sys.float_info.epsilon`보다 작거나 같은지 판단해야 한다. 
* 파이썬 3.5 이상부터는 두 실수가 같은지 판단할 때 `math.isclose` 함수를 사용

```python
#sys 모듈 사용
import sys
print(sys.float_info.epsilon)

abs(a-b) <= 1e - 10
# 1e - 10 = sys.float_info.epsilon 비교 기준으로 삼는 매우 작은 수 
#차이가 저것 보다 작으면 같다고 생각

#math 모듈 사용
import math
math.isclose(a,b)
```



​	**(3) complex(복소수)**

```python
a = 3 + 4j
type(a)

b = complex('3+4j') # 문자열을 복소수로 변환
c = complex('3 + 4j') #에러 뜸 #연산자 주위에 공백 X

```





#### 3.2 문자(String) 타입

```python
number = input('숫자를 입력해주세요 :') 
print(number*2)  #같은 str 반복함
type(number)     # 입력받은 것은 str이다. 

print(int(number)*2) #숫자 연산
```

* 따옴표 사용

```python
"he's cool"
'그의 이름은 "ssafy"다.'     #같은 부호를 사용하면 안됨.
"그의 이름은\"ssafy\"다."   #같은 부호 사용하려면 "앞에 \ 
```

* `+`연산자로 이어붙이고, `*` 연산자로 반복시킬 수 있다.

```python
'hello' + ' ' + 'ssafy' 
'hello ' + 'ssafy' 
'hello ' *3

name = 'john'
'my name is' + name
name *2

'hello''ssafy' #잘 안씀
```



* 이스케이프 시퀀스

| <center>예약문자</center> |    내용(의미)     |
| :-----------------------: | :---------------: |
|            \n             |      줄 바꿈      |
|            \t             |        탭         |
|            \r             |    캐리지리턴     |
|            \0             |     널(Null)      |
|           \\\\            |        `\`        |
|            \\'            | 단일인용부호(`'`) |
|            \\"            | 이중인용부호(`"`) |

```python
# %-formatting 활용
print('내 이름은 %s 입니다.' % name)

# str.format() 활용
print('내 이름은 {} 입니다.'.format(name))

# f-string 활용
print(f'내 이름은 {name} 입니다.')

# 여러줄 문자열에서도 사용 가능
print(f"""
내 이름은
{name}
입니다.
""")
```



cf ) `f-strings` 

```python
# 형식 지정 가능
import datetime
now = datetime.datetime.now()
print(now)

now.today() #년 월 일만 뽑아내고 싶을 때
f'이번년은 {now:%y} 이번달은 {now:%m}월 오늘은 {now:%d}일' #Y는 2020

# 연산과 출력형식 지정 가능
pi = 3.141592
r = 10
print(f'{pi:.2} 넓이는 : {pi*r*r:.3}') #2번째자리에서 반올림

```



#### 3.4 참/거짓(Boolean)타입

`false` = 0, 0.0, (), [], {}, '', None

(나머지는 true!)

```python
bool(0)
bool([])
```

* none 타입

  ```python
  a= None
  print(a)
  bool(a)
  ```



## 4. 형변환



#### 4.1 암시적 형변환

> 사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우

```python
# boolean과 integer
True + 3
int(True) #불리형은 정수형으로 형변환이 가능한데 암시적으로 파이썬이 해줌
False + 3

None + 3 #에러
```

```python
#더 포괄적인 수의 방식으로 형변환이 일어난다.
int_number = 2020
float_number = 3.14
complex_number = 2 + 3j

int_number + float_number #float 를 기준으로 형변환
int_number + complex_number #complex를 기준으로 형변환
```



#### 4.2 명시적 형변환

> 위의 상황을 제외하고는 모두 명시적으로 형 변환을 해주어야한다.
>
> - string -> intger : 형식에 맞는 숫자만 가능
> - integer -> string : 모두 가능



`int()` : string, float를 int로 변환

`float()` :  string, int를 float로 변환

`str()` : int, float, list, tuple, dictionary를 문자열로 변환



```python
# int + str
1 + '등'      #에러 
str(1) + '등'

float('3.5') #문자인 숫자를 숫자자료형으로 가능

# string 3.5를 int로 변환할 수는 없다. 
int(float('3.5')) 

# float 3.5는 int로 변환이 가능 
# float 3.5 를 int로 변환할 수 없다. 
```



## 5. 연산자

#### 5.1 산술 연산자

| 연산자 |      내용      |
| :----: | :------------: |
|   +    |      덧셈      |
|   -    |      뺄셈      |
|   *    |      곱셈      |
|   /    |     나눗셈     |
|   //   |       몫       |
|   %    | 나머지(modulo) |
|   **   |    거듭제곱    |

```python
#나누기는 float 타입으로 반환
5/2

#몫은 int 타입으로 변환
5//2 

#divmod 함수
divmod(5,2) #결과 값 = (2,1)
a,b = divmod(5,2)

#음수 양수 표현
num=2020
-num
```



#### 5.2 비교 연산자

| 연산자   | 내용                   |
| -------- | ---------------------- |
| `<`      | 미만                   |
| `<=`     | 이하                   |
| `>`      | 초과                   |
| `>=`     | 이상                   |
| `==`     | 같음                   |
| `!=`     | 같지않음               |
| `is`     | 객체 아이덴티티        |
| `is not` | 부정된 객체 아이덴티티 |

```python
3 == 3.0 #True
'hello' == 'Hello' #false #대소문자!
```



#### 5.3 논리 연산자

| 연산자  | 내용                         |
| ------- | ---------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a 와 b 모두 False시만 False  |
| not a   | True -> False, False -> True |

```python
'a' and 'b'  #b
'a' or 'b'  #a
5 and 0  #0
5 or 0   #5
```

* `and` 는 둘 다 True일 경우만 True이기 때문에 첫번째 값이 True라도 두번째 값을 확인해야 하기 때문에 'b'가 반환된다.
* `or` 는 하나만 True라도 True이기 때문에 True를 만나면 해당 값을 바로 반환한다.



#### 5.4 복합 연산자

| 연산자  | 내용       |
| ------- | ---------- |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |
| a **= b | a = a ** b |



#### 5.4 기타 주요 연산자

(1) convatenation

```python
[1,2,3] + [4,5,6]
```



(2) containment test

`in` 연산자 : 요소가 속해있는지 여부 확인 가능

```python
'a' in 'hello'
0 in [1,3,5,7]
45 in range(0,45)
```



(3) identity

`is` 연산자 : 동일한 object인지 확인 가능

```python
id(5)

a = [1, 2, 3]
b = [1, 2, 3]

print(a==b) 
# true
print(a is b) #a와 b의 id가 같은지 물어보는 것
#false
```



(4) indexing / slicing

`[]`를 통한 값을 접근하고, `[:]`을 통해 리스트를 슬라이싱할 수 있다.



#### 5.5 표현식과 문장

