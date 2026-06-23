# 👁️ Real-Time Computer Vision Projects

A collection of interactive real-time computer vision applications built using **Python, OpenCV, and MediaPipe**.

This repository explores how computers can understand live camera input through image processing, object tracking, hand detection, and gesture-based interaction.

The focus of these projects is not just processing images, but building applications where the camera responds to real-world actions.

---

## 🚀 Overview

Computer Vision is a field that enables machines to analyze and interpret visual information.

This repository contains a series of beginner-to-intermediate projects created to understand important computer vision concepts through practical implementation.

The projects include:

- 🎨 Gesture-controlled drawing
- ✋ Hand and finger tracking
- 📸 Real-time camera filters
- 🎯 Object tracking
- 🌈 Color detection

---

# 🛠️ Tech Stack

| Technology | Usage |
|-----------|-------|
| Python | Core programming language |
| OpenCV | Image processing, webcam handling, filtering |
| MediaPipe | Hand detection and landmark tracking |
| NumPy | Image arrays and mathematical operations |

---

# 📂 Projects

## 🎨 1. Air Canvas

A virtual drawing application where hand movements are converted into digital drawings.

The index finger acts as a brush, allowing users to draw in the air using real-time hand tracking.

**Key Concepts**
- Hand landmark detection
- Gesture recognition
- Coordinate tracking
- Virtual canvas implementation

📁 Folder: `01-Air-Canvas`

---

## 📸 2. FilterCapture

A real-time camera filter application with portrait-style effects.

The application applies image processing techniques to modify live webcam frames.

**Key Concepts**
- Image filtering
- Background blur
- Face detection
- Image masking

📁 Folder: `02-FilterCapture`

---

## ✋ 3. Finger Counter

A hand tracking system that detects fingers and counts how many are raised.

It analyzes hand landmark positions to identify finger states.

**Key Concepts**
- MediaPipe Hands
- Landmark analysis
- Hand tracking
- Gesture interpretation

📁 Folder: `03-Finger-Counter`

---

## 🎯 4. Color Tracker

Tracks selected colored objects through the webcam.

Objects are detected based on color ranges and tracked in real time.

**Key Concepts**
- HSV color space
- Color masking
- Contour detection
- Object tracking

📁 Folder: `04-Color-Tracker`

---

## 🌈 5. Color Detector

Detects multiple colors from live video input and displays information about detected regions.

**Key Concepts**
- Color segmentation
- HSV thresholding
- Morphological operations
- Contour analysis

📁 Folder: `05-Color-Detector`

---

# 📁 Repository Structure

```
Real-Time-Computer-Vision-Projects

│
├── 01-Air-Canvas
│   ├── air_canvas.py
│   └── README.md
│
├── 02-FilterCapture
│   ├── filter_capture.py
│   └── README.md
│
├── 03-Finger-Counter
│   ├── finger_counter.py
│   └── README.md
│
├── 04-Color-Tracker
│   ├── color_tracker.py
│   └── README.md
│
├── 05-Color-Detector
│   ├── color_detector.py
│   └── README.md
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/your-username/Real-Time-Computer-Vision-Projects.git
```

Navigate into the folder:

```bash
cd Real-Time-Computer-Vision-Projects
```

---

## 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Dependencies:

```
opencv-python
mediapipe
numpy
```

---

# ▶️ Running Projects

Go into any project folder:

Example:

```bash
cd 01-Air-Canvas
```

Run:

```bash
python air_canvas.py
```

Allow webcam access when requested.

---

# 🧠 Computer Vision Concepts Covered

Through these projects, the following concepts are explored:

- Real-time video processing
- Image transformations
- Color space conversion
- HSV-based segmentation
- Image masking
- Contour detection
- Hand landmark tracking
- Gesture recognition
- Coordinate mapping
- Interactive vision applications

---

# 🔮 Future Scope

Future additions may include:

- Face recognition systems
- Pose estimation applications
- Gesture-controlled interfaces
- Deep learning based object detection
- YOLO-based projects

---

# 📌 Purpose

This repository documents my learning journey in Computer Vision by creating practical applications using OpenCV and MediaPipe.

Each project focuses on understanding a core concept and applying it through real-time webcam interaction.
