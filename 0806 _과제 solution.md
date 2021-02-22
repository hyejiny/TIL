#### 0806 _과제 solution

```python
for i in range(len(arr)):
    for j in range(len(i))
```

```python
# 가로 세로 대각 총합중 최대값 출력

T = 10
for tc in range(1,T+1):
    tn = int(input())
    numbers = [list(map(int,input().split())) for _in range(100)] 
    #변수 쓰지 않을 때 (_)사용
    
    for row in numbers:
            
     #가로 합, 세로합, 대각합(위,아래) 을 저장하는 배열
    max_number = [0]*4
    
    #가로합
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += number[i][j]
            #반복문 안에서는 합
        #반복이 끝나면, 가로합의 최대값 구하기(이전의 최대값과 비교)
        if max_number[0] < row_sum:
            max_number[0] = row_sum
    
    #세로합
    for i in range(100): #칼럼의 인덱스
        col_sum = 0
        for j in range(100): #로우의 인덱스
            col_sum += number[j][i]
        if col_sum > max_number[1]:
            max_number[1] = col_sum
    
    #대각합(상)

    for i in range(100):
        for j in range(100):
            if i+j ==99:
                max_number[2] +=numbers[i][j]
                
    for i in range(100):
        for j in range(100):
            if i==j:
                max_number[3] +=number[i][j]
    
    result = max_number[0]
    for i in range(len(max_number)):
        if result < max_number[i]:
            result = max_number[i]
    
    print("#%d" %tn, result)
```







