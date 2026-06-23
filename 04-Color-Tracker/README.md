# 🎯 Color Tracker - Real-Time Object Tracking Using OpenCV

Color Tracker is a real-time computer vision application that detects and tracks objects based on their color using a webcam.

The project uses **OpenCV** to process live video frames, identify selected colors using HSV color filtering, and track the movement of colored objects on the screen.

---

## 🚀 Features

- 📹 Real-time webcam tracking
- 🎨 Select objects based on color
- 🔴 Track red objects
- 🟢 Track green objects
- 🔵 Track blue objects
- 🎯 Detect object position
- ⭕ Draw tracking circle around objects
- 📍 Show object center point
- ⌨️ Switch colors while running

---

# 🛠️ Technologies Used

| Technology | Purpose |
|----------|----------|
| Python | Programming language |
| OpenCV | Webcam handling and object tracking |
| NumPy | Mask creation and image operations |

---

# 🧠 How It Works

The application continuously captures frames from the webcam and searches for a selected color.

### Workflow

```
Webcam Input
      ↓
Capture frame using OpenCV
      ↓
Convert BGR image to HSV
      ↓
Apply selected color mask
      ↓
Remove noise from mask
      ↓
Find object contours
      ↓
Track largest detected object
      ↓
Display object location
```

---

# 🎨 Color Selection

The user can choose which color to track while the application is running.

Supported colors:

🔴 Red  
🟢 Green  
🔵 Blue  

The selected color is isolated from the camera feed using HSV ranges.

---

# 🌈 Why HSV Color Space?

Normal images use BGR/RGB values.

However, RGB values change easily due to lighting.

HSV separates:

```
Hue        → Color information
Saturation → Color intensity
Value      → Brightness
```

This makes object tracking more stable in different lighting conditions.

---

# 🎯 Object Tracking Process

## 1. Color Masking

The selected color is extracted:

```
Original Frame
        ↓
HSV Conversion
        ↓
Color Threshold
        ↓
Binary Mask
```

Only the selected color remains visible for detection.

---

## 2. Noise Removal

Small unwanted pixels are removed using:

- Erosion
- Dilation

Process:

```
Raw Mask
    ↓
Remove noise
    ↓
Cleaner object region
```

---

## 3. Contour Detection

The application finds the boundaries of detected objects.

The largest contour is selected as the main tracked object.

```
Detected Color Area
          ↓
Find Contour
          ↓
Calculate Position
          ↓
Draw Tracking Circle
```

---

# ⌨️ Controls

| Key | Action |
|-|-|
| `r` | Track red objects |
| `g` | Track green objects |
| `b` | Track blue objects |
| `q` | Quit application |

---

# 📦 Installation

Install required libraries:

```bash
pip install opencv-python numpy
```

---

# ▶️ Run the Project

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
python color_tracker.py
```

Make sure the webcam is connected.

---

# 📚 What I Learned

Through this project, I explored:

- Real-time video processing
- Color spaces in computer vision
- HSV-based object detection
- Creating binary masks
- Removing image noise
- Detecting contours
- Tracking moving objects

---

# 🔮 Possible Improvements

Future upgrades:

- Add tracking path/trail effect
- Track multiple objects
- Add custom color selection
- Estimate object speed
- Add gesture interaction
- Combine with object recognition models

---

# 📌 Project Type

Computer Vision | Object Tracking | Color Detection | OpenCV | HSV Processing
