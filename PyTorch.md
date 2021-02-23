## PyTorch



### #1. Tensor Manipulation



#### 1. 백터, 행렬, 텐서

* 백터 : 1차원
* 행렬 : 2차원
* 텐서 : 3차원



```text
주로 3차원 이상을 텐서라고 하긴 하지만, 1차원 벡터나 2차원인 행렬도 텐서라고 표현하기도 합니다. 같은 표현입니다. 1차원 벡터 = 1차원 텐서, 2차원 행렬 = 2차원 텐서. 그리고 3차원 텐서, 4차원 텐서, 5차원 텐서 등...
```



#### 2. **PyTorch Tensor Shape Convention**

* 2D Tensor

  `|t| = (Batch size, dim)`

* 3D Tensor

  `|t| = (batch size, width, height)`

  ex ) 여러장의 이미지(가로,세로)

  `|t| = (batch size, length, dim)`

  ex ) 자연어 처리 / 문장 길이

