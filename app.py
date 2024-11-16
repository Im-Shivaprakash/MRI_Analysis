from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from yolo_detector import detect_objects

app = Flask(__name__)

# Configurations
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Upload and Process Route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Define the output path for the processed image
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"processed_{file.filename}")

        # Call YOLO detection logic
        detect_objects(filepath, output_path)

        return redirect(url_for('uploaded_file', filename=f"processed_{file.filename}"))

# Route to Display Processed Image
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
