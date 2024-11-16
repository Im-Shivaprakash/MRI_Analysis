# MRI_Analysis - A YOLO Disease Detection

A Flask-based web application for detecting brain-related diseases from medical images using a YOLO model. Users can upload an image, and the application processes it to identify and localize potential disease regions with bounding boxes. The application also provides the associated disease names and confidence scores.

---

## Features

- Object detection with YOLO for diseases.
- Displays bounding boxes with disease names and confidence scores.
- Clean and modular code with Flask for the front-end.
- Easy to set up and run locally.

## Project Structure

project/
├── static/
│   ├── css/
│   │   └── styles.css       # CSS for UI
│   └── uploads/             # Folder for uploaded images
├── templates/
│   └── index.html           # HTML for the front-end
├── app.py                   # Flask application
├── yolo_detector.py         # YOLO detection logic
├── requirements.txt         # Dependencies for the project
└── README.md                # Project documentation

## Prerequisites

- Python 3.8 or higher
- A YOLO-trained model

## Getting Started

# Steps to Run Locally

- Clone the Repository Clone the repository from GitHub:

```bash

git clone https://github.com/your-username/yolo-disease-detection.git

cd yolo-disease-detection

```

 - Install Dependencies Ensure you have Python installed, then install required packages:

```bash

pip install -r requirements.txt

```

 - Run the Application Start the Flask application:

```bash

python app.py

```

### Open in Browser Open http://127.0.0.1:5000 in your browser to access the interface.

## Example Usage
- Upload an Image: Select an image file containing a suspected diseased region.
- View Results: The app processes the image and displays:
- Bounding boxes around detected regions.
- Disease names and confidence scores.

Example Outputs
Input Image:

Output Image:
The output shows bounding boxes with disease names and confidence scores.

Contributing
Contributions are welcome! If you find any bugs or have feature requests, feel free to:

Submit an issue.
Create a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.