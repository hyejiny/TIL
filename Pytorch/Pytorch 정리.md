## Tensor

* pytorch의 자료 형
* 단일 데이터 타입으로 된 자료들의 다차원 행렬

* GPU(cuda명령어)로 연산 가능

* 생성

  ```python
  import torch
  
  torch.Tensor(크기)
  ```

  * random 선언

    ```python
    torch.rand()
    torch.randn() #normal distribution random값
    ```

  * 형태 변환(view)

  * 합치기(cat)

  * 더 많은 함수 사용 가능 (공식 홈페이지 참조)

    

### Backpropagation

* Autograd : 미분값을 자동으로 계산해줌
* 자동 계산을 위해서 사용하는 변수는 Variable
  * data
  * grad : data가 거쳐온 layer에 대한 미분값이 축적됨
  * grad_fn : 미분 값을 계산한 함수에 대한 정보



### nn& nn.functional

* nn.Conv2d
  * w를 직접 선언하지 않음
  * 자동으로 w 설정해줌
  * input, ouput, 커널 크기
  * 자동으로 bias 값 가지고 있음 (bias=None)설정해주면됨
* nn.functional.Conv2d
  * input과 w를 선언해주어야함
  * 따라서, 외부에서 만든 필터를 넣어줘야함



### nn.**MaxPool2D**

* 정해진 filter크기 안에서 가장 큰 값만 뽑아낸다



📌 실습

```python
# 데이터 입력
Variable
# 입력의 크기 파악
torch.Size([배치,채널,height,width])
#conv2d에 적용
outchannel은 필터 갯수랑 동일하다고 보면 된다.
kernel = filter
kernel size = n*n
```



위의 실습을 하나하나씩 하는 것이 아니라 한꺼번에 하는 것

= 분류기 모델 설계



