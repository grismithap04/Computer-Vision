# 📸 FilterCapture - Real-Time Camera Filter Application

FilterCapture is an interactive computer vision camera application that applies live visual effects to webcam input.

The project uses **OpenCV** to process real-time video frames, apply image filters, detect faces, create portrait-style background effects, and capture images with timestamps.

It transforms a normal webcam into a smart camera application with customizable filters.

---

## 🚀 Features

- 📹 Real-time webcam processing
- 🖼️ Portrait-style background blur
- ⚫ Grayscale camera mode
- 😀 Face detection
- 📷 Photo capture feature
- 🕒 Automatic date and time watermark
- 💾 Save or discard captured images
- ⌨️ Keyboard-controlled filter switching

---

## 🛠️ Technologies Used

| Technology | Purpose |
|----------|----------|
| Python | Programming language |
| OpenCV | Camera handling and image processing |
| NumPy | Image arrays, masks, and blending |
| Haar Cascade | Face detection |

---

## 🧠 How It Works

FilterCapture continuously captures frames from the webcam and applies selected filters based on user input.

### Workflow

```
Webcam Input
      ↓
OpenCV captures frames
      ↓
Face detection is performed
      ↓
Person area is separated using masking
      ↓
Filters are applied
      ↓
Processed frame displayed live
```

---

# 🎭 Available Modes

## 🖼️ Portrait Blur Mode

Creates a portrait-camera effect by keeping the person focused and blurring the background.

Process:

```
Original Frame
      ↓
Detect Face
      ↓
Create Person Mask
      ↓
Blur Background
      ↓
Merge Foreground + Background
      ↓
Portrait Output
```

---

## ⚫ Grayscale Mode

Converts the live camera feed into black-and-white format.

Process:

```
BGR Image
    ↓
Grayscale Conversion
    ↓
Filtered Output
```

---

## 📷 Capture Mode

Allows users to capture photos with active filters.

Features:

- Applies current selected filters
- Adds timestamp
- Shows preview
- Allows save/discard decision

---

## ⌨️ Controls

| Key | Action |
|-|-|
| `b` | Toggle portrait blur |
| `g` | Toggle grayscale filter |
| `SPACE` | Capture photo |
| `y` | Save captured photo |
| `n` | Discard captured photo |
| `q` | Quit application |

---

# 📌 Computer Vision Concepts Used

## Face Detection

The application uses OpenCV Haar Cascade detection to locate faces from webcam frames.

Detected regions help estimate the person area.

---

## Image Masking

A mask is created to separate:

```
Person
  +
Background
```

This allows different effects to be applied to different parts of the image.

---

## Image Blending

The final image combines:

```
Original Person Region
          +
Blurred Background
          ↓
Final Portrait Effect
```

---

## Real-Time Frame Processing

Each webcam frame follows:

```
Capture
   ↓
Process
   ↓
Apply Filter
   ↓
Display
```

creating a live interactive camera experience.

---

# 📦 Installation

Install required dependencies:

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
python filter_capture.py
```

Make sure your webcam is connected and camera permissions are enabled.

---

# 📚 What I Learned

Through this project, I explored:

- Accessing webcam streams using OpenCV
- Processing video frames continuously
- Applying real-time image filters
- Detecting faces using Haar Cascades
- Creating and using masks
- Combining multiple processed images
- Building interactive keyboard-controlled applications

---

# 🔮 Possible Improvements

Future enhancements:

- Add more filters
- Improve background segmentation using AI models
- Add beauty/skin smoothing filters
- Add video recording support
- Add adjustable blur intensity
- Add face effects and stickers

---

# 📌 Project Type

Computer Vision | Image Processing | Camera Application | OpenCV | Real-Time Filters
