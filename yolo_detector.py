import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("D:\Medical_Application\Final_Project\yolov11s_trained.pt")

# Mapping of class IDs to disease names
CLASS_NAMES = {
    0: 'Glioma',
    1: 'Meningioma',
    2: 'No Tumor',
    3: 'Pituitary',
    # Add more mappings as per your model's class definitions
}


def detect_objects(image_path, output_path):
    """
    Run YOLO inference and draw bounding boxes on the image.
    :param image_path: Path to the input image.
    :param output_path: Path to save the processed image.
    """
    # Run YOLO inference
    results = model(image_path)

    # Load the image
    img = cv2.imread(image_path)

    # Draw bounding boxes
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            conf = box.conf[0].item()
            class_id = int(box.cls[0].item())
            disease_name = CLASS_NAMES.get(class_id, "Unknown Disease")

            label = f"{disease_name} ({conf:.2f})"
            color = (0, 255, 0)
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Save the processed image
    cv2.imwrite(output_path, img)
