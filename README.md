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

### 06.10
###### 프리티가 변종이 많고 다른 것과 유사한 점이 많아서 빼고 다른 데이터 셋 추가
장미허브 - Vicks

##### (test img: 레티지아/ result: 레티지아, 라울) 🔺 정확도 상승 But 잘 못 잡는 부분이 있음
![image](https://github.com/harinme/plant-project/assets/152590695/9b63bc3e-426b-4782-be3a-1669dc775062)
문제점: 레티지아와 라울이 같이 잡힘(라울은 사진 내 x)
원인 분석: 데이터 셋 부족
개선 부분: 데이터 셋 추가(레티지아, 라울 각 20장씩)

##### (test img: 레티지아/ result: 레티지아, 미니염자) 🔺 정확도 상승 But 잘 못 잡는 부분이 있음(개선은 됨)
![image](https://github.com/harinme/plant-project/assets/152590695/1e30a865-0063-4ace-82a2-352527543f8b)
문제점: 레티지아와 라울이 같이 잡힘(라울은 사진 내 x)
원인 분석: 데이터 셋 부족
개선 부분: 데이터 셋 추가(미니염자, 청옥 20장씩)

### 06.12 Lucky hunt(네잎 클로버 분류 모델링)
##### V1
![image](https://github.com/harinme/plant-project/assets/152590695/5434591b-fd82-47ab-8482-bf03328dfa86)
Roboflow 활용하여 데이터 전처리 / Colab에서 학습
문제점: 네잎 클로버 인식 불가

##### V2 데이터 추가 및 전처리
![image](https://github.com/harinme/plant-project/assets/152590695/e78eec1f-7a96-4fa3-83ad-9d74b6c1c059)
![image](https://github.com/harinme/plant-project/assets/152590695/cad83f3d-a9b1-46d2-8954-45d327635dbf)
문제점: 네잎 클로버 인식은 하지만 제대로 되지 않음.

##### V3 오픈 데이터 셋 활용
open data 활용(https://www.gperezs.com/projects/flc.html)
데이터 셋 이미지로 Colab에서 학습

### 프로젝트 UI에 삽입 될 img
![image](https://github.com/harinme/plant-project/assets/152590695/f3d07ac9-1958-4c68-ac1e-302ee9376e72)

### 06.13
###### UI 구상
###### 대표 색 4가지
![image](https://github.com/harinme/plant-project/assets/152590695/5204e8fe-acf3-405d-9ffb-800a979179d0)

##### V4 데이터셋 추가

![image](https://github.com/harinme/plant-project/assets/152590695/2f77e73f-19e0-41c3-bf97-6e760d8ff32b)

##### 웹캠으로 인식 test

![image](https://github.com/harinme/plant-project/assets/152590695/2b92b772-f962-4028-8d9e-a9ce19c86ef1)

### 06.14
##### 질병 분류는 데이터도 부족으로 모델링의 어려움이 有 / 질병 분류 대신 다육이 종류 추가(괴마옥, 축전, 모닐리포메)
##### 각 25개씩 데이터 추가
###### 괴마옥 - Euphorbia

![image](https://github.com/harinme/plant-project/assets/152590695/00635d29-623b-4da4-835c-84108ed774a0)

###### 축전 - Conophytum

![image](https://github.com/harinme/plant-project/assets/152590695/473a2081-37a9-423c-a4c3-ad2a5b62b411)

###### 모닐라리아 모닐리포메 - moniliformis

![image](https://github.com/harinme/plant-project/assets/152590695/9d98da9e-1558-4bea-bc88-70767561fb37)


### 06.18 
##### 최종 모델 best_8.pt
총 8가지 라울, 레티지아, 미니 염자, 청옥, 괴마옥, 장미허브, 모닐리포메, 축전

라울 - LumiRose
미니염자 - Crassula
레티지아 - Letizia
청옥 - Sedum
축전 - Conophytum
괴마옥 - Euphorbia
모닐라리아 모닐리포메 - moniliformis
장미허브 - Vicks

식물별 설명화면 제작
![화면 캡처 2024-06-20 124452](https://github.com/harinme/plant-project/assets/152591270/63d00651-ac61-4ad7-83a6-c509961a4943)

###### APP 알고리즘 구상
![image](https://github.com/harinme/plant-project/assets/152590695/7b9f4e6a-c33a-4712-bdf0-bc964c61f309)


### 06.25
##### flutter 화면 구현(windows)
![image](https://github.com/harinme/plant-project/assets/152590695/1e1dc67a-852d-4f12-8350-6ffd4fcdbcf9)


### 06.26
##### flutter 구현(라이브러리 추가, flask 서버 연결-이미지 분석용 서버)
![image](https://github.com/harinme/plant-project/assets/152590695/db3f16a1-07aa-41cb-96b3-99afe2eed70b)
![image](https://github.com/harinme/plant-project/assets/152590695/295c6ff5-281f-4a22-a10f-26043391e6c9)

![image](https://github.com/harinme/plant-project/assets/152590695/9a1d98a7-3136-4445-bdd2-2a020a8e1027)

### 06.28
##### flutter 구현(식물찾기 부분 화면)
![KakaoTalk_20240627_161843814_03](https://github.com/harinme/plant-project/assets/152591270/136b15ce-df8e-489b-a3c1-a338edaf03e9)
![KakaoTalk_20240627_161843814_04](https://github.com/harinme/plant-project/assets/152591270/c98e1c19-6526-40b5-9844-f42ac47f8043)
![KakaoTalk_20240627_161843814](https://github.com/harinme/plant-project/assets/152591270/a467c410-ebbf-49ef-b4c1-06bdda6f0a91)
![KakaoTalk_20240627_161843814_01](https://github.com/harinme/plant-project/assets/152591270/dcc31541-dd88-4cc7-962c-7ea1c48eedc4)
![KakaoTalk_20240627_161843814_02](https://github.com/harinme/plant-project/assets/152591270/26ea0e58-ae88-40cf-a193-863353acf6e6)



# 추가
- 클로버를 아시나요? 
- ![image](https://github.com/harinme/plant-project/assets/152591273/1e79e301-b689-4c27-8782-42a5ebe3a671)
- 클로버에는 세잎 , 네잎이 있지만 네잎이 행운을 뜻합니다
- 모든 사람들은 행운을 원하고 저도 마찬가지였습니다
- 그래서 행운을 찾을수 있도록 핸드폰만 있으면 모두 행운을 찾을수 있게 도와주는 기능을 추가했습니다.

https://github.com/user-attachments/assets/497612ba-c0f2-4ba8-9cd9-96a3cb15b291


