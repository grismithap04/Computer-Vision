import cv2
import mediapipe as mp

# Initialize MediaPipe Hand tracking and drawing modules
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Landmark IDs for finger tips and their corresponding lower knuckles (PIP joints)
# IDs represent: Thumb=4, Index=8, Middle=12, Ring=16, Pinky=20
FINGER_TIPS = [4, 8, 12, 16, 20]
FINGER_PIPS = [3, 6, 10, 14, 18]

def count_fingers(hand_landmarks, handedness):
    """
    Analyzes hand landmarks to determine which fingers are raised.
    Returns a list of boolean states for each finger and the total count.
    """
    lm = hand_landmarks.landmark
    is_right = handedness == "Right"
    
    # --- Thumb Logic ---
    # Thumb state relies on horizontal movement relative to its inner joint.
    # Right hand: raised if tip is to the left of the PIP joint.
    # Left hand: raised if tip is to the right of the PIP joint.
    thumb_up = (lm[4].x < lm[3].x) if is_right else (lm[4].x > lm[3].x)
    
    # --- Other Fingers Logic ---
    # In OpenCV, y=0 is at the top of the frame. 
    # If a fingertip's y-coordinate is lower than its PIP joint, the finger is raised.
    fingers = [thumb_up]
    for tip, pip in zip(FINGER_TIPS[1:], FINGER_PIPS[1:]):
        fingers.append(lm[tip].y < lm[pip].y)
    
    return fingers, sum(fingers)

def main():
    # Initialize the default webcam feed
    cap = cv2.VideoCapture(0)
    
    # Configure MediaPipe Hands to track up to 2 hands simultaneously
    with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7) as hands:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Flip the frame horizontally to create a natural mirror effect
            frame = cv2.flip(frame, 1)
            
            # Convert BGR image to RGB as required by MediaPipe processing
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)
            
            total = 0
            # Process data if hands are detected in the frame
            if results.multi_hand_landmarks:
                for hand_lm, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
                    # Get the individual finger states and count for the current hand
                    states, count = count_fingers(hand_lm, hand_info.classification[0].label)
                    total += count
                    
                    # Draw the 21 skeletal landmarks and connecting lines on the frame
                    mp_drawing.draw_landmarks(frame, hand_lm, mp_hands.HAND_CONNECTIONS)
                    
                    # --- Render Labels Near Fingertips ---
                    for tip_id, name, is_up in zip(FINGER_TIPS, ["Thumb","Index","Middle","Ring","Pinky"], states):
                        # Convert normalized MediaPipe coordinates (0.0 to 1.0) to pixel integers
                        x = int(hand_lm.landmark[tip_id].x * frame.shape[1])
                        y = int(hand_lm.landmark[tip_id].y * frame.shape[0]) - 18
                        
                        # Green for UP, Blue/Orange tint for DOWN
                        color = (0,255,0) if is_up else (0,80,200)
                        cv2.putText(frame, f"{name}: {'UP' if is_up else 'DOWN'}", (x-30,y), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1)
            
            # --- Render Total Count Dashboard (Top-Left) ---
            # Draw dark background bounding box
            cv2.rectangle(frame, (10,10), (200,110), (30,30,30), -1)
            # Add text headers and total counter integer
            cv2.putText(frame, "Fingers UP", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255), 1)
            cv2.putText(frame, str(total), (75,95), cv2.FONT_HERSHEY_SIMPLEX, 2.2, (0,255,0), 3)
            
            # Render exit instructions at the bottom right
            cv2.putText(frame, "Press 'q' to quit", (frame.shape[1]-150, frame.shape[0]-12), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, (150,150,150), 1)
            
            # Display the live window frame
            cv2.imshow("Finger Counter", frame)
            
            # Break loop when 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    # Release hardware resources and close all application windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

