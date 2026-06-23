# 🎨 Air Canvas - Virtual Drawing Using Hand Gestures

Air Canvas is a real-time computer vision project that allows users to draw on a virtual canvas by simply moving their finger in the air.

The project uses **OpenCV** for webcam processing and **MediaPipe Hands** for detecting and tracking hand landmarks. The index finger acts as a virtual brush, making the webcam an interactive drawing tool.

---

## 🚀 Features

- ✋ Real-time hand tracking
- 🖌️ Draw using index finger movement
- 🎨 Multiple color selection
- 🧽 Eraser mode
- 👍 Gesture-based canvas clearing
- 🖥️ Interactive on-screen toolbar
- 📹 Live webcam processing

---

## 🛠️ Technologies Used

| Technology | Purpose |
|----------|----------|
| Python | Programming language |
| OpenCV | Webcam handling and image processing |
| MediaPipe | Hand detection and landmark tracking |
| NumPy | Canvas creation and pixel manipulation |

---

## 🧠 How It Works

The application captures video frames from the webcam and processes each frame in real time.

### Workflow

```
Webcam Input
      ↓
OpenCV captures frames
      ↓
MediaPipe detects hand landmarks
      ↓
Index fingertip coordinates are extracted
      ↓
Finger movement is mapped onto canvas
      ↓
Drawing appears on screen
```

---

## ✋ Gesture Controls

| Action | Gesture |
|------|---------|
| Draw | Move index finger |
| Change Color | Touch color toolbar |
| Erase | Select eraser option |
| Clear Canvas | Thumb up gesture |
| Quit Application | Press `q` |

---

## 🎨 Available Tools

The virtual toolbar provides:

- 🔵 Blue Brush
- 🟢 Green Brush
- 🔴 Red Brush
- 🟡 Yellow Brush
- ⚫ Eraser

The selected tool is highlighted while drawing.

---

## 📌 Computer Vision Concepts Used

### Hand Landmark Detection

MediaPipe detects 21 points on the hand.

The project mainly uses:

- Index fingertip landmark → drawing position
- Thumb landmark → clear gesture detection

---

### Coordinate Mapping

MediaPipe provides normalized coordinates.

They are converted into screen pixel positions:

```
Hand Position
      ↓
Landmark Coordinates
      ↓
Screen Coordinates
      ↓
Canvas Drawing
```

---

### Canvas Overlay

A separate NumPy canvas layer is maintained.

The webcam frame and drawing canvas are combined to create the final output.

```
Camera Frame
      +
Drawing Canvas
      ↓
Final Display
```

---

## 📦 Installation

Install required libraries:

```bash
pip install opencv-python mediapipe numpy
```

---

## ▶️ Run the Project

Clone the repository:

```bash
git clone https://github.com/your-username/Real-Time-Computer-Vision-Projects.git
```

Move into the project folder:

```bash
cd Real-Time-Computer-Vision-Projects
```

Run:

```bash
python air_canvas.py
```

---

## 📚 What I Learned

Through this project, I explored:

- Processing live camera input
- Working with OpenCV video streams
- Using MediaPipe hand tracking
- Understanding landmark-based detection
- Creating gesture-controlled interfaces
- Combining computer vision with user interaction

---

## 🔮 Possible Improvements

Future upgrades:

- Save drawings as images
- Add more brush styles
- Brush size adjustment using gestures
- Shape drawing tools
- Gesture-based undo option

---

## 📌 Project Type

Computer Vision | Hand Tracking | Gesture Recognition | OpenCV | MediaPipe
