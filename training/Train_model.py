from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.yaml')  # Or yolov8s.yaml for better accuracy
    model.train(
        data='C:/Users/kaung/OneDrive/Documents/Object_detection_project/training/data.yaml',
        epochs=50,
        imgsz=416,
        batch=4,
        workers=2,
        amp=False,
        name='vehicle_detector7',
    )

if __name__ == '__main__':
    main()
