import cv2
import numpy as np
from datetime import datetime

# Initialize camera
cap = cv2.VideoCapture(0)

# toogle functions for user input
blur_on = False
gray_on = False

# Load face detection from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def get_person_mask(frame):
    """Create mask that covers face and estimated body area"""
    h, w = frame.shape[:2]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    # Create empty mask
    mask = np.zeros((h, w), dtype=np.uint8)
    
    for (x, y, w_face, h_face) in faces:
        # Face area (keep sharp)
        cv2.rectangle(mask, (x, y), (x + w_face, y + h_face), 255, -1)
        
        # Estimate body area (below face, wider)
        body_width = int(w_face * 1.5)
        body_height = int(h_face * 2)
        body_x = x + w_face//2 - body_width//2
        body_y = y + h_face
        
        # Make sure body area stays within frame
        body_x = max(0, body_x)
        body_y = min(body_y, h)
        body_w = min(body_width, w - body_x)
        body_h = min(body_height, h - body_y)
        
        # Body area (keep sharp too)
        if body_h > 0 and body_w > 0:
            cv2.rectangle(mask, (body_x, body_y), (body_x + body_w, body_y + body_h), 255, -1)
        
        # Also add a bit above the face (for hair)
        head_y = max(0, y - int(h_face * 0.3))
        head_h = int(h_face * 0.3)
        cv2.rectangle(mask, (x, head_y), (x + w_face, y), 255, -1)
    
    # If face detected, smooth the mask edges
    if len(faces) > 0:
        mask = cv2.GaussianBlur(mask.astype(np.float32), (31, 31), 0)
        mask = mask / 255.0
    else:
        # No face detected, keep everything sharp
        mask = np.ones((h, w), dtype=np.float32)
    
    return mask

def blur_background(frame, mask):
    """Blur background, keep entire person sharp"""
    # Apply median blur to entire frame
    blurred = cv2.medianBlur(frame, 25)
    
    # Use mask to keep person sharp, blur background
    mask_3channel = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    result = (frame * mask_3channel + blurred * (1 - mask_3channel)).astype(np.uint8)
    return result

def add_datestamp(img):
    """Add date and time to bottom-right corner"""
    h, w = img.shape[:2]
    now = datetime.now()
    text = f"{now.strftime('%d-%m-%Y')} {now.strftime('%H:%M:%S')}"
    
    cv2.rectangle(img, (w - 200, h - 35), (w, h), (0, 0, 0), -1)
    cv2.putText(img, text, (w - 195, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

def show_save_prompt(photo):
    """Display photo with smaller Y/N prompt"""
    h, w = photo.shape[:2]
    
    # Create a copy for the prompt
    prompt_display = photo.copy()
    
    # Draw smaller semi-transparent overlay at the bottom
    overlay = prompt_display.copy()
    cv2.rectangle(overlay, (0, h - 60), (w, h), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.7, prompt_display, 0.3, 0, prompt_display)
    
    # Add prompt text with SMALLER font
    cv2.putText(prompt_display, "Save this photo?", (w//2 - 80, h - 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(prompt_display, "Y = Save     N = Discard", (w//2 - 85, h - 18), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 220, 110), 1)
    
    # Show the prompt window
    cv2.imshow("Save Photo?", prompt_display)
    
    # Wait for user input
    while True:
        key = cv2.waitKey(0) & 0xFF
        if key == ord('y') or key == ord('Y'):
            cv2.destroyWindow("Save Photo?")
            return True
        elif key == ord('n') or key == ord('N'):
            cv2.destroyWindow("Save Photo?")
            return False

print("Starting camera...")
print("Press 'b' for portrait blur, 'g' for grayscale, SPACE for photo, 'q' to quit\n")

while True:
    success, frame = cap.read()
    if not success:
        break
    
    # Get mask for the person (face + body)
    mask = get_person_mask(frame)
    
    # Start with original frame
    result = frame.copy()
    
    # Apply portrait blur if enabled
    if blur_on:
        result = blur_background(result, mask)
    
    # Apply grayscale if enabled
    if gray_on:
        result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
    
    # Show HUD
    h, w = result.shape[:2]
    cv2.rectangle(result, (0, 0), (w, 50), (0, 0, 0), -1)
    cv2.putText(result, "SPACE=capture  b=portrait blur  g=gray  q=quit", (10, 20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
    
    status = f"● LIVE    Portrait Blur: {'ON' if blur_on else 'OFF'}    Gray: {'ON' if gray_on else 'OFF'}"
    cv2.putText(result, status, (10, 42), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 
                (0, 220, 110) if blur_on else (140, 140, 140), 1)
    
    cv2.imshow("Portrait Mode", result)
    
    # Handle keys
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('b'):
        blur_on = not blur_on
        print(f"Portrait Blur: {'ON' if blur_on else 'OFF'}")
    elif key == ord('g'):
        gray_on = not gray_on
        print(f"Grayscale: {'ON' if gray_on else 'OFF'}")
    elif key == ord(' '):
        print("Photo captured!")
        
        # Capture photo with current settings
        photo = frame.copy()
        if blur_on:
            photo_mask = get_person_mask(photo)
            photo = blur_background(photo, photo_mask)
        if gray_on:
            photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
            photo = cv2.cvtColor(photo, cv2.COLOR_GRAY2BGR)
        
        add_datestamp(photo)
        
        # Show prompt and ask user
        if show_save_prompt(photo):
            filename = f"photo_opencv_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            cv2.imwrite(filename, photo)
            print(f"Saved: {filename}")
        else:
            print("Discarded")

cap.release()
cv2.destroyAllWindows()
