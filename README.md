# History of Meme

## 프로젝트 계획 동기
> 인터넷 밈(Meme), 혹은 줄여서 밈은 인터넷 곳곳에서 재미있는 사진과 글이 합쳐져 유행처럼 퍼져 나가는 2차 창작물 등을 일컫는 단어다. 밈은 단순한 유행에서 그치지 않고, 인터넷의 거대한 문화 중 하나로 자리잡았다. 대중문화, 시사, 정치, 경제 등 여러 분야에 막대한 영향을 끼치는 밈은 사회역사적인 가치를 지니고 있으며, 특정 밈이 내포하고 있는 의미 뿐만 아니라 밈의 전체적인 흐름을 분석해야할 이유는 충분하다. 따라서, 우리는 밈의 시대적 흐름을 분석하기 위해 밈 사진을 딥러닝 기반 이미지 분류 시스템을 이용하여 인식하고 구분하는 연구를 진행하기로 결정했다. 

## 프로젝트 목표
1. 인터넷에 퍼져있는 최대한 다양하고 많은 양의 밈을 모은다.
  1. 이미지는 이미지 파일과 이미지가 업로드된 날짜가 레이블 되어있다.
2. 이미지 분류 시스템을 통해 밈의 짜임새와 구조를 파악하고 구분한다.
3. 실험셋을 통해 시스템이 제 역할을 수행하는지 확인한다.
4. 밈 이미지의 짜임새와 생성된 날짜의 연관성의 여부를 확인한다.

## 프로젝트 구성
### 데이터셋 
웹 스크래핑을 이용하여 이미지 데이터셋을 구축한다. 소스는 구글, Imgur, Reddit, 9gag 등 다양한 곳에서 밈 이미지를 수집한다. 총 이미지 수는 5,000장을 목표로 한다. 이 중 3,500장을 훈련셋, 1,500장을 시험셋으로 나눈다. 만에 하나 이미지 분류 시스템이 특별한 성과를 보이지 못할 경우, 이미지를 추가로 수집한다. 이미지의 규격은 전부 정사각형으로 크롭한 뒤, 128x128 픽셀 단위로 리사이즈한다. 훈련 과정에서 과도한 시간이 요구될 경우, 정사각형 비율은 유지하나 사진 규격을 축소한다. 이미지는 모두 컬러 상태(3채널)로 입력한다 (원본이 흑백인 경우 제외). 

### 이미지 분류 시스템
Tensorflow 패키지를 이용한다. 그 중에서 Convolutional Neural Network(CNN)을 이용한 머신 러닝 기법을 이용한다. 정확도 향상을 위해 원본 이미지로부터 data augmentation을 이용해 이미지 샘플을 만들어 내는 Keras의 ImageDataGenerator 모듈을 사용한다. 약 3,500장의 훈련셋 이미지를 n개의 Convolutional Layer에 통과시킨다 (정확한 층수는 데이터 수집 단계 후 직접 실험을 통해 결정한다). 층 가운데에 n x n Max Pooling을 통해 Overfitting을 방지한다 (n 역시 실험을 통해 그 수를 정한다). Convolutional Layer에 통과시킨 후 n개의 Fully Connected Dense Layer에 Max Pooling한 픽셀의 값을 넘긴다. 마지막 Dense Layer의 활성함수는 n개의 다른 이벤트의 확률을 계산하는 softmax를 활용한다. ![image](https://user-images.githubusercontent.com/46840483/134803750-d99cb185-ad94-4959-a02e-1d5dbf02b348.png)

###### 프로그램의 구조를 이런 그림으로 나타낼 것입니다. 사진은 예시입니다.

### 결과 가시화
훈련을 마친 시스템을 1,500장의 실험셋을 통해 accuracy, precision, recall, F1 Score를 confusion matrix로 나타낸다. matplotlib 혹은 seaborn을 통해 결과를 그래프로 나타낸다. 실험셋을 통해 로그램의 높은 정확도 (최소 93%)를 확인한 경우, 실험셋의 이미지가 생성된 날짜와 그 짜임새에 연관성이 있는지 확인한다. 마찬가지로 matplotlib 혹은 seaborn을 이용해 두 가지 데이터를 그래프로 나타낸 뒤, 연관성의 여부를 판단한다. 
