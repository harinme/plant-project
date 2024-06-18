import cv2
from ultralytics import YOLO
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import colorsys  # 추가된 부분

# YOLO 모델 로드
model = YOLO('./best_8.pt')

# 웹캡 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 예측 임계값 설정
conf_threshold = 0.5

# 클래스별 색상 생성 함수 (HSV 색상 공간 이용)
def get_class_color(class_id):
    hsv_color = (class_id * 30 % 360 / 360.0, 1.0, 1.0)  # 각 클래스에 고유한 색상 할당 (30도씩 차이)
    rgb_color = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(*hsv_color))
    return rgb_color

# 클래스명 매핑 딕셔너리 (원래 클래스명 -> 원하는 출력명)
class_name_mapping = {
    'Conophytum': '축전',
    'Euphorbia': '괴마옥',
    'Vicks': '장미허브',
    'LumiRose': '라울',
    'Crassula': '미니염자',
    'Letizia': '레티지아',
    'Sedum': '청옥',
    'Moniliformis': '모닐라리아 모닐리포메'
    # 필요한 클래스명 매핑 추가
}

# 한글 폰트 로드 (사용할 폰트 파일 경로를 설정)
font_path = "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf"  # 굵은 폰트 파일 경로
font = ImageFont.truetype(font_path, 18)  # 폰트 크기 증가

def draw_text_with_outline(draw, text, position, font, text_color, outline_color, outline_width):
    x, y = position
    # Draw outline
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
    # Draw text
    draw.text(position, text, font=font, fill=text_color)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # YOLO 모델로 예측
    results = model.predict(frame, conf=conf_threshold)
    
    # 결과 표시
    for result in results:
        for bbox in result.boxes:
            # bounding box 좌표 가져오기
            x1, y1, x2, y2 = bbox.xyxy[0].tolist()
            conf = bbox.conf[0]  # 첫 번째 값을 가져옵니다
            
            # 예측 신뢰도가 임계값보다 큰 경우에만 그리기
            if conf > conf_threshold:
                # 라벨 가져오기
                class_id = int(bbox.cls[0])  # 클래스 ID 가져오기
                original_class_name = model.names[class_id]  # 클래스 이름 가져오기
                
                # 클래스명 매핑
                class_name = class_name_mapping.get(original_class_name, original_class_name)
                color = get_class_color(class_id)  # 클래스에 따른 색상 가져오기
                
                # bounding box 그리기
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                
                # PIL을 이용한 텍스트 그리기
                img_pil = Image.fromarray(frame)
                draw = ImageDraw.Draw(img_pil)
                label = f'{class_name}: {conf:.2f}'
                text_color = color  # 클래스에 따른 폰트 색상
                outline_color = (255, 255, 255)  # 흰색 테두리
                draw_text_with_outline(draw, label, (int(x1), int(y1) - 30), font, text_color, outline_color, 2)

                # OpenCV 형식으로 다시 변환
                frame = np.array(img_pil)
    
    # 프레임 출력
    cv2.imshow('YOLO Prediction', frame)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
