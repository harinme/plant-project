# plant-project(제 3차 프로젝트)
### 간단 개요:
## [식집사(식물관리 프로그램)]
- 다육(가정에서 흔하게 기르는 식물)의 사진을 찍으면 종류를 분류(총 5가지 프리티, 라울, 레티지아, 미니 염자, 청옥)
  
- 다육의 흔한 질병 인식 및 해결책 제시(총 4가지 무름병, 쟃빛곰팡이병, 탄저병, 노균병)
  * 1차적으로 다육의 종류 및 질병 인식 후 완성되면 추가하여 개선
    
- 습도 센서(물 준 날짜 기록용)를 사용하여 데이터베이스에 저장 후 특정 날짜가 지나면 알람(Web-tts / APP-application 알람)
  * 다육의 경우 기르기 쉬운 식물로 알려져 있지만 잘 기르려면 습도 조절이 필요함
  
## 알고리즘
![image](https://github.com/harinme/plant-project/assets/152590695/b0bb4c4e-7a4d-4954-9cb3-a08c4fa9572c)

## 진행과정:
### 06.04 식집사 프로젝트 시작
- 데이터 수집을 위해 다육이 모델 선정(프리티, 라울, 레티지아, 미니 염자, 청옥)
- 다육이 질병(무름병, 쟃빛곰팡이병, 탄저병, 노균병)

#### 데이터 셋 수집 분배
- 유나: 프리티, 레티지아
- 혜정: 미니 염자, 라울
- 현희: 청옥

### 06.05
#### 데이터 셋 라벨링(Roboflow)
- 수집한 데이터 셋 라벨링(1차 프리티, 라울, 레티지아, 미니 염자/ 2차 프리티, 라울, 레티지아, 미니 염자, 청옥 )
![image](https://github.com/harinme/plant-project/assets/152590695/06cf4236-3506-4634-b049-a0ae364f519c)
![image](https://github.com/harinme/plant-project/assets/152590695/3259afe1-e0a3-4fd2-ade8-913b36ee27a5)


### 데이터 학습 및 결과 확인(Colab-학습, vs code-결과 확인
##### 1차 모델 테스트 
##### (test img: 미니염자/ result: 라울) ❌
![image](https://github.com/harinme/plant-project/assets/152590695/bd144029-5630-4aff-9c27-f974a4ad2a77)

##### (test img: 레티지아/ result: 라울) ❌
![image](https://github.com/harinme/plant-project/assets/152590695/7f7de55f-b619-4b13-98ad-be5b1d712955)

문제점: 인식을 제대로 못함.
원인 분석: 
- yaml 파일에 저장된 분류가 1개 뿐이고 그마저도 '-'로 되어있음.
![image](https://github.com/harinme/plant-project/assets/152590695/593cfec0-aea1-4d34-b7fb-4d8f7361bbfe)
- 기존 라벨링 당시 class 명을 한글로 한 것이 문제라고 추측
![image](https://github.com/harinme/plant-project/assets/152590695/6711e64e-1b93-4250-9e86-f62746811d21)
개선할 부분: 1차에 빠진 청옥 데이터 셋 추가 / class 명 영어로 수정

##### 2차 모델 테스트 - 1차 개선
라울 - LumiRose
미니염자 - Crassula
프리티 - Rezry
레티지아 - Letizia
청옥 - Sedum
![image](https://github.com/harinme/plant-project/assets/152590695/e5a28ba9-5c80-492f-aa61-bc9d9f5be169)

##### (test img: 레티지아/ result: 레티지아) ⭕
![image](https://github.com/harinme/plant-project/assets/152590695/6874c04f-aad4-4f2c-8ccd-90473a993b7a)

##### (test img: 미니염자/ result: 미니염자) ⭕
![image](https://github.com/harinme/plant-project/assets/152590695/8dad985d-e815-4e74-a7ba-52942f071125)

##### (test img: 청옥/ result: 청옥) ⭕
![image](https://github.com/harinme/plant-project/assets/152590695/f204d280-b410-4798-8fb8-a319e63bc0d3)

##### (test img: 라울/ result: 라울) ⭕
![image](https://github.com/harinme/plant-project/assets/152590695/c28530d4-9bce-4850-8504-4dc99728dc96)

---------------------
 
##### (test img: 프리티/ result: 레티지아, 미니염자, 청옥) ❌ -- conf:0.1
![image](https://github.com/harinme/plant-project/assets/152590695/74e6534d-9343-4e10-87f9-530d4fbca3ac)

##### (test img: 프리티/ result: 프리티) ⭕ But 정확도 낮은 게 多
![image](https://github.com/harinme/plant-project/assets/152590695/84c4f814-8f82-43b5-aabc-dfc120009a7b)

문제점: 프리티가 유독 정확도도 낮고 인식이 제대로 안됨
원인 분석: 다른 종과 유사하기 때문에 더 많은 데이터셋 있어야함 / 낮은 학습량:50번
개선 부분: 데이터 셋 추가 및 학습량 늘려보기

# 추가
- 클로버를 아시나요? 
- 클로버에는 세잎 , 네잎이 있지만 네잎이 행운을 뜻합니다
- 모든 사람들은 행운을 원하고 저도 마찬가지였습니다
- 그래서 행운을 찾을수 있도록 핸드폰만 있으면 모두 행운을 찾을수 있게 도와주는 앱을 만들었습니다.
- ![image](https://github.com/harinme/plant-project/assets/152591273/1e79e301-b689-4c27-8782-42a5ebe3a671)
