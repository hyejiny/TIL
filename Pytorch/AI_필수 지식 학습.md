#### 머신러닝의 유형

> 지도학습, 비지도학습, 강화학습

* 머신러닝이란? 
  * 데이터로부터 일반화된 규칙을 찾도록하는 것
  * classification, clustering, regression&prediction, 특징 추출
* 머신러닝 과정
  * 학습데이터 -> 전처리 -> (여기부터 머신러닝) 특징 추출 -> 학습 -> 결정함수 -> 분류/ 예측 / 군집화
* 지도학습 : Target Output이 있음 (classification,regression)
* 비지도학습 : Target Output이 없음 (Clustering)

#### Neural Networks 

> 생물학적 신경회로망을 모델링 한 수학적 함수

* 학습방식(데이터 분석 용도)에 따라 다양한 모델 존재
* 구성요소
  * Neuron,Node,Unit (신경세포)
  * Network Structure (신경망 구조)
  * Leargin Algorithm (학습 알고리즘)
* 인공신경망의 학습
  * 가중치(w)를 조정하는 것
  * 학습 데이터를 활용하여 가중치 변화량을 결정

#### Multi-Layer Perceptron

* Perceptron : 기본적인 신경망 구조

  * single layer neural network

* Multi-Layer Perceptron : perceptron을 다중으로 쌓은 것

* 학습법 예시

  * 기울기 강하 학습법 (Gradient Descent Method) 

    * 오차함수의 기울기를 이용하여 감소하는 방향으로 이동
    * 학습률(변화 폭 결정)은 오류역전파 알고리즘으로 계산

    



#### Convolutional Neural Network(CNN)



#### 이미지 캡셔닝(Image Captioning)

> 이미지를 입력으로 받아 이에 대한 적절한 설명을 텍스트로 출력하는 기술

* step1. 이미지 입력이 들어오면, 이미지에서 의미 있는 물체들의 후보를 나열함. (CNN기반)
* step2. 의미있는 물체 후보들을 RNN을 통해 문장으로 변환