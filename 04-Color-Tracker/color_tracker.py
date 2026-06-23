import cv2
import numpy as np

# Color configurations
COLORS = {
    'r': {'name': 'Red', 'bgr': (0, 0, 255), 'ranges': [([0, 120, 70], [10, 255, 255]), ([170, 120, 70], [180, 255, 255])]},
    'g': {'name': 'Green', 'bgr': (0, 255, 0), 'ranges': [([36, 100, 50], [86, 255, 255])]},
    'b': {'name': 'Blue', 'bgr': (255, 0, 0), 'ranges': [([94, 100, 50], [126, 255, 255])]}
}

def get_mask(hsv, color_key):
    """Create mask for a specific color"""
    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
    for lower, upper in COLORS[color_key]['ranges']:
        mask |= cv2.inRange(hsv, np.array(lower), np.array(upper))
    
    # Clean up mask
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    return mask

def add_text_overlay(frame, text, position, color, scale=0.65):
    """Add text with black background overlay"""
    cv2.rectangle(frame, (position[0], position[1] - 25), 
                  (position[0] + 370, position[1] + 5), (0, 0, 0), -1)
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, scale, color, 2)

cap = cv2.VideoCapture(0)
current_color = None
WIN = "Color Tracker"

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    if current_color is None:
        # Show color selection dialog
        overlay = frame.copy()
        h, w = frame.shape[:2]
        cx, cy = w // 2, h // 2
        
        cv2.rectangle(overlay, (cx - 180, cy - 50), (cx + 180, cy + 30), (30, 30, 30), -1)
        cv2.addWeighted(overlay, 0.75, frame, 0.25, 0, frame)
        cv2.putText(frame, "Select color to track", (cx - 140, cy - 20),    
                   cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
        cv2.putText(frame, "Press R / G / B to track", (cx - 130, cy + 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)
    else:
        # Track selected color
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = get_mask(hsv, current_color)
        
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest) > 500:
                (x, y), radius = cv2.minEnclosingCircle(largest)
                center = (int(x), int(y))
                color_bgr = COLORS[current_color]['bgr']
                
                cv2.circle(frame, center, int(radius), color_bgr, 2)
                cv2.circle(frame, center, 5, color_bgr, -1)
                cv2.putText(frame, f"{COLORS[current_color]['name']} detected",
                           (center[0] - 50, center[1] - int(radius) - 12),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_bgr, 2)
        
        # Show tracking info
        add_text_overlay(frame, f"Tracking: {COLORS[current_color]['name']}", (10, 28), 
                        COLORS[current_color]['bgr'])
        add_text_overlay(frame, "Press R/G/B to switch | Q to quit", (10, 54), 
                        (255, 255, 255), 0.45)
    
    cv2.imshow(WIN, frame)
    
    # Handle key presses
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif chr(key).lower() in COLORS:
        current_color = chr(key).lower()

cap.release()
cv2.destroyAllWindows()
