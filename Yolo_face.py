import torch
import cv2
import time

_MARGIN = 10  # pixels
_ROW_SIZE = 10 
_FONT_SIZE = 2
_FONT_THICKNESS = 2
_TEXT_COLOR = (0, 0, 255) 
row_size = 20  # pixels
left_margin = 24


model = torch.hub.load('ultralytics/yolov5', 'custom', 'face_detection_yolov5s.engine')
device = torch.device('cpu')
model.to(device)
cap = cv2.VideoCapture(0)
counter, fps = 0, 0
start_time = time.time()
fps_avg_frame_count = 10

while (True):
    ret, img = cap.read()
    img = cv2.resize(img, (640, 640))
    result = model(img[..., ::-1])
    results = result.pandas().xyxy[0].to_dict(orient="records")
    for result in results:
          con = round(result['confidence'], 2)
          cs = result['class']
          nm = result['name']
          x1 = int(result['xmin'])
          y1 = int(result['ymin'])
          x2 = int(result['xmax'])
          y2 = int(result['ymax'])
          box = (x1+x2, y1+y2)
          x = int( (x1+x2) /2)
          y = int( (y1+y2) /2)
          center = (x, y)
          text_location = (_MARGIN + x1,_MARGIN + _ROW_SIZE + y1)
          cv2.rectangle(img, (x1, y1), (x2, y2), _TEXT_COLOR, 2)
          if nm == 'person':
               print('person detected')
               cv2.circle(img, center, 5,  _TEXT_COLOR, -1)

          fps_location = (left_margin, row_size)
          print('confidence:\n', con, 'class:\n', nm)
          cv2.putText(img, nm, text_location, cv2.FONT_HERSHEY_PLAIN,
               _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS)
    res = cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
