import cv2
import numpy as np

# Color data: (BGR, HSV ranges)
COLORS = {
    'Red': ((0,0,255), [((0,120,70),(10,255,255)), ((170,120,70),(180,255,255))]),
    'Green': ((0,255,0), [((36,100,70),(86,255,255))]),
    'Blue': ((255,0,0), [((100,150,70),(130,255,255))]),
    'White': ((255,255,255), [((0,0,200),(180,30,255))]),
    'Black': ((0,0,0), [((0,0,0),(180,255,50))])
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    hsv = cv2.cvtColor(cv2.GaussianBlur(frame, (11,11), 0), cv2.COLOR_BGR2HSV)
    result = frame.copy()
    
    for name, (bgr, ranges) in COLORS.items():
        mask = np.zeros(hsv.shape[:2], np.uint8)
        for lower, upper in ranges:
            mask |= cv2.inRange(hsv, np.array(lower), np.array(upper))
        
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
        
        for cnt in cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]:
            if cv2.contourArea(cnt) > 2000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(result, (x, y), (x+w, y+h), bgr, 2)
                rgb = frame[y:y+h, x:x+w].mean(axis=(0,1)).astype(int)[::-1]
                cv2.putText(result, f"RGB{tuple(rgb)} {name}", (x, max(y-10,20)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.55, bgr, 2)
    
    cv2.imshow("Color Detection", result)
    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()
