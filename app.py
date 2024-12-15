from flask import Flask, request, jsonify, send_file, render_template
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Load Pre-trained Haar Cascade for Face Detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Dummy function for predicting age (ganti dengan model prediksi umur)
def predict_age(face_image):
    # Dummy prediction
    return np.random.randint(15, 50)  # Random age between 15-50

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files.get('image')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Read the image
    np_img = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Crop face region
        face_img = img[y:y+h, x:x+w]

        # Predict age
        age = predict_age(face_img)

        # Draw rectangle and put text
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, f'{age} yrs', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Convert image to bytes for response
    _, buffer = cv2.imencode('.jpg', img)
    io_buf = BytesIO(buffer)

    return send_file(io_buf, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
