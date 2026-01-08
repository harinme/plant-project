from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image, UnidentifiedImageError
import io

# YOLOv8 모델 로드
model = YOLO('4.pt')  # YOLOv8 모델을 ultralytics에서 로드합니다.

app = Flask(__name__)

def preprocess_image(image_data):
    try:
        image = Image.open(io.BytesIO(image_data))
        return image
    except UnidentifiedImageError:
        raise ValueError("Invalid image data")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file'}), 400
        
        image_file = request.files['image']
        image_data = image_file.read()
        
        # 이미지를 전처리합니다.
        image = preprocess_image(image_data)
        
        # YOLO 모델을 실행합니다.
        results = model(image)
        
        # 결과를 JSON 형식으로 변환합니다.
        results_json = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                result_dict = {
                    "xmin": box.xyxy[0][0].item(),
                    "ymin": box.xyxy[0][1].item(),
                    "xmax": box.xyxy[0][2].item(),
                    "ymax": box.xyxy[0][3].item(),
                    "confidence": box.conf[0].item(),
                    "class": box.cls[0].item(),
                    "name": result.names[int(box.cls[0].item())]
                }
                results_json.append(result_dict)
        
        return jsonify({'results': results_json})
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        print(f'Error during prediction: {e}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
