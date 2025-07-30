from ultralytics import YOLO
import cv2

# Load your trained YOLOv8 model
model = YOLO(r"...\Object_detection_project\models\best.pt")

# Path to your input video
video_path = r"C:\Users\kaung\Downloads\demo2.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Output video writer
output_path = r"...\Object_detection_project\output_demo.mp4"
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# Inference loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame, conf=0.25)[0]

    # Override class names if needed
    results.names = {0: 'car', 1: 'truck', 2: 'bus'}

    # Annotate frame with bounding boxes
    annotated_frame = results.plot()

    # Display the frame
    cv2.imshow("Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Write annotated frame to output video
    out.write(annotated_frame)

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Saved detected video to: {output_path}")
