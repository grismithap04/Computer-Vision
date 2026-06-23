# 🌈 Color Detector - Real-Time Color Recognition Using OpenCV

Color Detector is a real-time computer vision application that identifies and highlights different colors from a live webcam feed.

The project uses **OpenCV** to process video frames, detect predefined colors using HSV color segmentation, and display detected color information including RGB values.

---

## 🚀 Features

- 📹 Real-time webcam color detection
- 🔴 Detects Red objects
- 🟢 Detects Green objects
- 🔵 Detects Blue objects
- ⚪ Detects White regions
- ⚫ Detects Black regions
- 📦 Draws bounding boxes around detected colors
- 🎨 Displays detected color names
- 🔢 Shows RGB values of detected regions

---

# 🛠️ Technologies Used

| Technology | Purpose |
|----------|----------|
| Python | Programming language |
| OpenCV | Image processing and object detection |
| NumPy | Array operations and color calculations |

---

# 🧠 How It Works

The application captures live frames from the webcam and analyzes each frame to identify colors.

### Workflow

```
Webcam Input
      ↓
Capture frame using OpenCV
      ↓
Apply Gaussian Blur
      ↓
Convert BGR image to HSV
      ↓
Create masks for each color
      ↓
Clean masks using morphology
      ↓
Detect color regions
      ↓
Display color information
```

---

# 🎨 Color Detection Process

The system detects colors using predefined HSV ranges.

Supported colors:

🔴 Red  
🟢 Green  
🔵 Blue  
⚪ White  
⚫ Black  

Each color has its own HSV threshold values.

---

# 🌈 HSV Color Space

Instead of detecting colors directly from RGB/BGR values, the project uses HSV.

HSV separates:

```
Hue
 |
 └── Actual color information

Saturation
 |
 └── Color intensity

Value
 |
 └── Brightness
```

This improves detection accuracy under different lighting conditions.

---

# 🔍 Image Processing Steps

## 1. Noise Reduction

Before detecting colors, Gaussian blur is applied:

```
Camera Frame
       ↓
Gaussian Blur
       ↓
Smoother Image
```

This reduces unwanted noise from the webcam feed.

---

## 2. Color Mask Creation

For every color:

```
HSV Image
    ↓
Apply Color Range
    ↓
Create Binary Mask
```

The mask separates the selected color from the background.

---

## 3. Morphological Processing

The mask is cleaned using morphological operations.

This helps remove:

- Small unwanted pixels
- Camera noise
- False detections

Process:

```
Raw Mask
    ↓
Morphological Opening
    ↓
Clean Mask
```

---

## 4. Contour Detection

The application finds the boundaries of detected colored regions.

```
Color Mask
     ↓
Find Contours
     ↓
Filter Large Regions
     ↓
Draw Bounding Box
```

---

# 📊 Output Information

For each detected object:

The application displays:

```
Color Name

+

RGB Value
```

Example:

```
RGB(240, 20, 30) Red
```

This allows both visual detection and numerical color analysis.

---

# ⌨️ Controls

| Key | Action |
|-|-|
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

Move into the project:

```bash
cd Real-Time-Computer-Vision-Projects
```

Run:

```bash
python color_detector.py
```

Allow webcam permission if required.

---

# 📚 What I Learned

Through this project, I explored:

- Working with live video streams
- Understanding color spaces
- HSV-based color segmentation
- Creating and combining masks
- Applying image preprocessing
- Morphological transformations
- Detecting object boundaries using contours
- Extracting RGB values from image regions

---

# 🔮 Possible Improvements

Future enhancements:

- Add custom color picker
- Detect more colors
- Improve detection under low lighting
- Add object size measurement
- Save detected color information
- Build a color analysis tool

---

# 📌 Project Type

Computer Vision | Color Recognition | Image Processing | OpenCV | HSV Segmentation
