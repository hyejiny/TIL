## oop

#### 1. 객체

> 모든 객체는 타입, 속성, 조작법(method)를 가진다.



#### 2. 타입과 인스턴스

> 타입 : 공통된 속성과 조작법을 가진 객체들의 분류
>
> ex) int, str, list, dict
>
> 인스턴스 : 특정 타입의 실제 데이터 예시
>
> 파이썬에서 모든 것은 객체이고, 모든 객체는 특정 타입의 인스턴스이다.

```python
type()
isinstance(a,int)
```



#### 3. 속성과 메서드

> 속성 : 객체의 상태
>
> 메서드 : 특정 객체에 적용할 수 있는 행위



#### 4. 클래스와 객체

> type : 공통 속성을 가진 객체들의 분류
>
> class : 객체들의 분류(class)를 정의할 때 쓰이는 키워드

* 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 정의된 함수는 매서드로 불린다.



#### 5. 인스턴스 생성

> 정의된 클래스에 속하는 객체를 해당 클래스의 인스턴스라고 한다. 

* type() 함수를 통해 생성된 객체의 클래스를 확인할 수 있다. 



#### 6. 메서드 정의

> 특정 데이터 타입(또는 클래스)의 객체에 공통적으로 적용 가능한 행위들을 의미한다. 



-------------



```python
class Calculator:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def sum:

a = Calculator(10,20)
a.sum()
```

* calculator 클래스에 인자를 바로 넘기기 위해서 생성자 메서드 활용
* self : 객체 a에서 메소드를 호출할 때는 객체 스스로를 가리키는 인자가 필요함. 

#### 7. 생성자 메서드

> 인스턴스 객체가 생성될 때 호출되는 함수(클래스의 메모리에 객체 생성)

인스턴스가 생성될 때 인스턴스의 속성을 정의할 수 있다.

```python
def __init__(self):
    
```



#### 8. 소멸자 메서드

> 인스턴스 객체가 소멸되기 직전에 호출되는 함수

```python
def __del__(self):
    
```



#### 9. 속성 정의

> 특정 데이터 타입의 객체들이 가지게 될 상태를 의미한다. 





-----------------

#### 1. 인스턴스 변수

```python
class Person:
    def __init__(self,name): # 인스턴스 생성자 메서드
        self.name = name #인스턴스 변수

a = Person('john')
print(a.name) #인스턴스 변수
```



#### 2. 클래스 변수

```python
class Person:
    species = 'human'
    
    def __init__(self,name):
        self.name = name
        
john = Person('john')
eric = Person('eric')

print(Person.species) #human
print(john.species) #human
john.species = 'developer'
print(john.species) #developer
print(eric.species) #human
```



#### 3. 인스턴스&클래스간의 이름공간

* 이름 탐색 순서 : 인스턴스 -> 클래스->상위 클래스

```python
class Person:
    name = '김싸피'
    
    def __init__(self,name = 'ssafy'):
        self.name = name
        
    def talk(self):
        return f'안녕, 나는 {self.name}'
    
Person.name #클래스 변수에 접근
p1 = Person()
p1.talk #ssafy가 변수로 전달됨

p1.name = 'john'
p1.talk #john이 변수로 전달됨

# 그러나, p2를 새로 생성해서 name을 조회하면 ssafy가 출력됨.
```



#### 4. 인스턴스 메서드

* 첫번째 인자로 인스턴스 자기자신 self가 전달됨



#### 5. 클래스 메서드

* @classmethod 사용해서 정의
* 호출시, 첫번째 인자로 클래스 cls가 전달됨
* 클래스/ 인스턴스 변수 두가지로 호출 가능
* 인스턴스 변수일 때, 수정 가능(우선시 됨)



#### 6. 스태틱 메서드

* @classmethod 사용해서 정의
* 호출시, 어떠한 인자도 전달되지 않음

```python
@classmethod
def info():
    return ' '
```

* 클래스 / 인스턴스 변수 두가지로 호출 가능



#### 7. 인스턴스와 메서드

* 인스턴스는 3가지 종류의 메서드 모두에 접근 가능
* 그러나, 인스턴스에서 클레스/스태틱 메서드 호출하지 말아야 한다.
* 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정지어 설계한다.



#### 8. 클래스와 메서드

* 클래스 또한 3가지 종류의 메서드 모두에 접근 가능
* 그러나, 클래스에서 인스턴스 메서드는 호출하지 않음
* 클래스 자체와 그 속성에 접근할 필요가 있다면, 클래스 메서드로 정의한다.
* 클래스와 클래스 속성에 접근할 필요가 없다면 정적 메서드로 정의한다.



#### 9. 클래스메서드와 정적메서드

* 클래스 메서드와 정적 메서드는 인스턴스 없이 호출할 수 있다는 점은 같다.
* 하지만, 클래스 메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 대 사용하며, 그렇지 않을 경우 정적 메서드를 사용한다. 



----------

#### 1. 상속

> 클래스가 가지고 있는 기능
>
> 부모 클래스의 모든 속성이 자식 클래스에게 상속되므로 코드 재사용성이 높아진다.

```python
issubclass(a,b) #클래스 상속 검사
```

* super()

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
      
    
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        self.student_id = student_id
    #상속 받았음에도 동일한 코드가 반복된다.
    def __init__(self, name, age, number, email, student_id):
        super().__init__(self, name, age, number, email)
        self.student_id = student_id
        
p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('김싸피', 20, '12312312', 'student@naver.com', '190000')
```



#### 2. 메서드 오버라이딩

> 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것.
>
> 상속 받은 클래스에서 같은 이름의 메서드로 덮어쓴다.



#### 3. 상속관계에서의 이름공간

> 인스턴스 -> 자식클래스 -> 부모클래스 -> 전역



#### 4. 다중 상속

> 두개 이상의 클래스를 상속 받는 경우 
>
> 상속 순서가 중요하다 (왼->오)

