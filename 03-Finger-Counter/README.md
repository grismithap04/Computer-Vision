# ✋ Finger Counter - Real-Time Hand Gesture Detection

Finger Counter is a real-time computer vision application that detects hands through a webcam and counts the number of fingers raised.

The project uses **OpenCV** for live video processing and **MediaPipe Hands** for detecting hand landmarks. By analyzing the position of finger joints, the system determines whether each finger is open or closed.

---

## 🚀 Features

- ✋ Real-time hand detection
- 🔢 Counts raised fingers automatically
- 🖐️ Supports detection of both hands
- 📍 Tracks 21 hand landmark points
- 🟢 Shows individual finger status (UP/DOWN)
- 🦴 Displays hand skeleton connections
- 📹 Live webcam-based interaction

---

## 🛠️ Technologies Used

| Technology | Purpose |
|----------|----------|
| Python | Programming language |
| OpenCV | Webcam handling and visual display |
| MediaPipe | Hand landmark detection |
| NumPy | Coordinate and numerical operations |

---

## 🧠 How It Works

The application captures live webcam frames and analyzes hand movements using landmark detection.

### Workflow

```
Webcam Input
      ↓
OpenCV captures frames
      ↓
Frame converted from BGR to RGB
      ↓
MediaPipe detects hand landmarks
      ↓
Finger joint positions are compared
      ↓
Finger states are calculated
      ↓
Total finger count displayed
```

---

# ✋ Hand Landmark Detection

MediaPipe Hands detects **21 landmarks** on each hand.

Important landmarks used:

```
Thumb Tip  → 4
Index Tip  → 8
Middle Tip → 12
Ring Tip   → 16
Pinky Tip  → 20
```

Each fingertip position is compared with its lower joint to check if the finger is raised.

---

# 🔢 Finger Counting Logic

## Four Fingers

For index, middle, ring, and pinky:

```
Fingertip position
        |
        ↓
Compare Y-coordinate with lower joint
        |
        ↓
Finger UP or DOWN
```

Since the top of the image has a lower Y-value:

```
Tip above joint = Finger Raised
```

---

## Thumb Detection

The thumb moves sideways instead of vertically.

The application checks:

- Left hand thumb direction
- Right hand thumb direction

to accurately detect whether the thumb is raised.

---

# 📊 Display Output

The application displays:

- Hand landmarks
- Finger names
- Individual finger states
- Total raised finger count

Example:

```
Thumb : UP
Index : UP
Middle: DOWN
Ring  : DOWN
Pinky : DOWN

Fingers UP: 2
```

---

# ⌨️ Controls

| Key | Action |
|-|-|
| `q` | Quit application |

---

# 📦 Installation

Install required dependencies:

```bash
pip install opencv-python mediapipe numpy
```

---

# ▶️ Run the Project

Clone the repository:

```bash
git clone https://github.com/your-username/Real-Time-Computer-Vision-Projects.git
```

Move into the project:

```bash
cd Real-Time-Computer-Vision-Projects
```

Run:

```bash
python finger_counter.py
```

Allow webcam access when requested.

---

# 📚 What I Learned

Through this project, I explored:

- Real-time webcam processing
- Hand tracking using MediaPipe
- Understanding landmark coordinates
- Gesture recognition logic
- Mapping AI detection results to application actions
- Working with coordinate-based decision making

---

# 🔮 Possible Improvements

Future upgrades:

- Add custom hand gestures
- Control applications using gestures
- Add volume control using fingers
- Add virtual mouse functionality
- Train gesture recognition models

---

# 📌 Project Type

Computer Vision | Hand Tracking | Gesture Recognition | OpenCV | MediaPipe
