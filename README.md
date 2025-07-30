# Vehicle Detection with YOLOv8

This project demonstrates object detection for vehicles (cars, trucks, buses) using a custom-trained [YOLOv8](https://github.com/ultralytics/ultralytics) model. It includes training scripts, model weights, and documentation for replication or extension.

## 🚗 Project Overview

The model was trained on drone footage datasets to detect:
- Cars
- Trucks
- Buses

## 📁 Project Structure

```
vehicle-detection-yolov8/
│
├── models/
│   └── best.pt                # Trained YOLOv8 weights
│
├── training/
│   ├── train.py               # YOLO training script
│   ├── data.yaml              # Dataset config used for training
│   └── utils/                 # (Optional) Helper functions
│
├── README.md
├── LICENSE
```



## 🧠 Training Setup

This project uses the [Ultralytics YOLOv8 framework](https://docs.ultralytics.com/) for training.

### 1. Install Requirements

pip install ultralytics opencv-python

### 2. Prepare Dataset

Dataset used for training is based on annotated drone footage. For large file size reasons, the dataset is not included here. You can recreate it using Roboflow export or your own annotated set.

The data.yaml file format:

train: /path/to/train/images
val: /path/to/val/images
test: /path/to/test/images

nc: 3
names: ['car', 'truck', 'bus']

### 3. Run Training

yolo detect train data=training/data.yaml model=yolov8n.pt epochs=50 imgsz=640

This will output best.pt inside a runs directory.
🖥 Demo App (Streamlit)

A demo app was built using Streamlit and deployed to Hugging Face Spaces. You can try it live or clone it locally.

The app allows:

    Uploading a video file for detection

    Viewing demo detection on a sample video

    Note: App code (app.py, detect.py, and demo video) are not included in this GitHub repository.
