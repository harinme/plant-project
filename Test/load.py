import cv2
from ultralytics import YOLO
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import colorsys
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# YOLO 모델 로드
model = YOLO('./best_8.pt')

# 예측 임계값 설정
conf_threshold = 0.5

# 파일 선택 대화상자를 통해 이미지 파일 선택
Tk().withdraw()  # Tkinter 창을 열지 않음
image_path = askopenfilename()  # 파일 선택 대화상자 열기

# 이미지 로드
frame = cv2.imread(image_path)
if frame is None:
    raise ValueError("Image not found or path is incorrect")

# 클래스별 색상 생성 함수
def get_class_color(class_id):
    hsv_color = (class_id * 30 % 360 / 360.0, 1.0, 1.0)
    rgb_color = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(*hsv_color))
    return rgb_color

# 클래스명 매핑
class_name_mapping = {
    'Conophytum': '축전',
    'Euphorbia': '괴마옥',
    'Vicks': '장미허브',
    'LumiRose': '라울',
    'Crassula': '미니염자',
    'Letizia': '레티지아',
    'Sedum': '청옥',
    'Moniliformis': '모닐라리아 모닐리포메'
}

# 한글 폰트 로드
font_path = "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf"
font = ImageFont.truetype(font_path, 18)

# 텍스트에 외곽선을 추가하는 함수
def draw_text_with_outline(draw, text, position, font, text_color, outline_color, outline_width):
    x, y = position
    # 텍스트 외곽선 그리기
    draw.text((x - outline_width, y - outline_width), text, font=font, fill=outline_color)
    draw.text((x + outline_width, y - outline_width), text, font=font, fill=outline_color)
    draw.text((x - outline_width, y + outline_width), text, font=font, fill=outline_color)
    draw.text((x + outline_width, y + outline_width), text, font=font, fill=outline_color)
    draw.text((x - outline_width, y), text, font=font, fill=outline_color)
    draw.text((x + outline_width, y), text, font=font, fill=outline_color)
    draw.text((x, y - outline_width), text, font=font, fill=outline_color)
    draw.text((x, y + outline_width), text, font=font, fill=outline_color)
    # 텍스트 본문 그리기
    draw.text(position, text, font=font, fill=text_color)

# 클래스별 예측값 저장을 위한 딕셔너리 초기화
class_confidences = {name: [] for name in class_name_mapping.values()}

# 이미지에 객체 검출 수행
results = model.predict(frame, conf=conf_threshold)

# 결과 표시
img_pil = Image.fromarray(frame)
draw = ImageDraw.Draw(img_pil)
for result in results:
    for bbox in result.boxes:
        x1, y1, x2, y2 = bbox.xyxy[0].tolist()
        conf = bbox.conf[0]
        if conf > conf_threshold:
            class_id = int(bbox.cls[0])
            original_class_name = model.names[class_id]
            class_name = class_name_mapping.get(original_class_name, original_class_name)
            color = get_class_color(class_id)
            label = f'{class_name}: {conf:.2f}'
            text_color = color
            outline_color = (255, 255, 255)
            # 바운딩 박스 그리기
            draw.rectangle([(x1, y1), (x2, y2)], outline=color, width=2)
            draw_text_with_outline(draw, label, (int(x1), int(y1) - 30), font, text_color, outline_color, 2)
            # 클래스별 예측값 저장
            class_confidences[class_name].append(conf)

# OpenCV 형식으로 다시 변환
frame = np.array(img_pil)

# 결과 이미지 출력
cv2.imshow('YOLO Prediction', frame)
cv2.waitKey(0)  # 유저가 키를 누를 때까지 기다림
cv2.destroyAllWindows()

# 각 클래스의 최소값과 최대값 출력
for class_name, confidences in class_confidences.items():
    if confidences:  # 해당 클래스의 예측값이 있는 경우에만 출력
        min_conf = min(confidences)
        max_conf = max(confidences)
        print(f"{class_name}: {min_conf:.2f} ~ {max_conf:.2f} 이 식물은 '{class_name}' 입니다.")
