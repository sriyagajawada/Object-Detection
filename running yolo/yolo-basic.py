from ultralytics import YOLO
import cv2
model = YOLO("../yolo-weig/yolov8l.pt")
results=model("images/img.png", show=True)
cv2.waitKey(0)