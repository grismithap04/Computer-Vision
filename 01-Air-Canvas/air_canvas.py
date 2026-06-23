"""
AIR CANVAS - Draw in the air using your index finger!
Thumb up = clear | q = quit
"""

import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.85,
    min_tracking_confidence=0.85
)

PALETTE = [
    ((180, 60, 20), "Blue"),
    ((30, 130, 30), "Green"),
    ((30, 30, 180), "Red"),
    ((20, 160, 160), "Yellow"),
    ((0, 0, 0), "Eraser"),
]

BRUSH_SIZE = 6
ERASER_SIZE = 30

PANEL_X, PANEL_Y = 10, 10
ROW_H = 28
DOT_R = 8
PANEL_W = 90
PANEL_PAD = 8

ROW_CENTERS = [PANEL_Y + PANEL_PAD + i * ROW_H + ROW_H // 2 for i in range(len(PALETTE))]
PANEL_H = PANEL_PAD * 2 + ROW_H * len(PALETTE)

current_color = PALETTE[0][0]
prev_x, prev_y = 0, 0

def get_finger_tip(landmarks, frame_w, frame_h):
    tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    return int(tip.x * frame_w), int(tip.y * frame_h)

def is_thumb_up(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP].y
    thumb_mcp = landmarks[mp_hands.HandLandmark.THUMB_MCP].y
    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    return thumb_tip < thumb_mcp and thumb_tip < index_tip - 0.05

def pick_color_from_toolbar(x, y):
    global current_color
    if PANEL_X <= x <= PANEL_X + PANEL_W:
        for i, (draw_color, _) in enumerate(PALETTE):
            cy = ROW_CENTERS[i]
            if abs(y - cy) < ROW_H // 2:
                current_color = draw_color
                return True
    return False

def draw_toolbar(frame):
    cv2.rectangle(frame, (PANEL_X, PANEL_Y), (PANEL_X + PANEL_W, PANEL_Y + PANEL_H), (0, 0, 0), -1)
    
    for i, (draw_color, name) in enumerate(PALETTE):
        cy = ROW_CENTERS[i]
        dot_cx = PANEL_X + PANEL_PAD + DOT_R
        
        dot_display = (90, 90, 90) if draw_color == (0, 0, 0) else draw_color
        cv2.circle(frame, (dot_cx, cy), DOT_R, dot_display, -1)
        
        if draw_color == current_color:
            cv2.circle(frame, (dot_cx, cy), DOT_R + 2, (220, 220, 220), 1)
        
        cv2.putText(frame, name, (dot_cx + DOT_R + 6, cy + 4),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.38, (200, 200, 200), 1)

def draw_hint_bar(frame, h, w):
    bar_h = 22
    cv2.rectangle(frame, (0, h - bar_h), (w, h), (0, 0, 0), -1)
    cv2.putText(frame, "thumb up: clear   |   q: quit",
                (10, h - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (170, 170, 170), 1)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

canvas = None

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]
    
    if canvas is None:
        canvas = np.zeros_like(frame)
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    
    mask = np.any(canvas > 0, axis=2)
    frame[mask] = canvas[mask]
    
    draw_toolbar(frame)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            lm = hand_landmarks.landmark
            fx, fy = get_finger_tip(lm, w, h)
            
            if is_thumb_up(lm):
                canvas.fill(0)
                cv2.putText(frame, "CLEARED", (w//2 - 40, h//2), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                prev_x, prev_y = 0, 0
            
            elif pick_color_from_toolbar(fx, fy):
                prev_x, prev_y = 0, 0
            
            else:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = fx, fy
                
                thickness = ERASER_SIZE if current_color == (0, 0, 0) else BRUSH_SIZE
                cv2.line(canvas, (prev_x, prev_y), (fx, fy), current_color, thickness)
                prev_x, prev_y = fx, fy
            
            dot_color = (90, 90, 90) if current_color == (0, 0, 0) else current_color
            cv2.circle(frame, (fx, fy), 7, dot_color, -1)
    
    else:
        prev_x, prev_y = 0, 0
    
    draw_hint_bar(frame, h, w)
    
    cv2.imshow("Air Canvas", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
