from ultralytics import YOLO


model = YOLO('best.pt')

img='./다육이/Test/라울.jpg'
results = model.predict(img, save=True, conf=0.1)