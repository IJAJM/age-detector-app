# Age Predictor Web App  
**Face Detection + Dummy Age Estimation**  

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)](https://opencv.org/)

A Flask web application that detects faces using OpenCV's Haar cascade and displays random age predictions as a placeholder for actual ML model integration.


## ✨ Features

- **Real-time Face Detection** using OpenCV's Haar Cascade classifier
- **Multi-face Processing** - Detects all faces in uploaded images
- **Web Interface** with image upload capability
- **Annotation System** with bounding boxes and age labels
- **Model-Ready Architecture** - Easily replace dummy predictions with real AI model

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/age-predictor-app.git
   cd age-predictor-app
   ```

2. **Setup Virtual Environment**
   ```bash
   python -m venv venv
   # Linux/MacOS
   source venv/bin/activate
   # Windows
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Application**
   ```bash
   python app.py
   ```

5. **Access in Browser**
   ```
   http://localhost:5000
   ```

## 🧠 Model Integration Guide

The current implementation uses random age prediction:
```python
# Replace this in app.py
def predict_age(face_img):
    return np.random.randint(18, 85)  # Placeholder
```

**To implement real age prediction:**
1. Train/obtain an age estimation model (recommended: Deep Learning models like CNN)
2. Save model in `models/` directory
3. Modify `predict_age()` function to use your model
4. Update requirements with necessary ML dependencies

## 📂 Project Structure

```
├── app.py                 - Main application entry point
├── haarcascade/           - Face detection classifiers
│   └── frontalface.xml
├── templates/             - Frontend components
│   └── home.html          
├── static/                - CSS/JS assets
│   └── styles.css
└── requirements.txt       - Dependency list
```

## 💡 Key Implementation Notes

- **Face Detection**: Uses Haar Cascade classifier from OpenCV
  - Best for frontal faces
  - For better accuracy, consider using DNN-based detectors
- **Age Prediction**: Current implementation uses random numbers
  - Mean absolute error (MAE) of current system: 100% 😅
- **Performance**: Optimized for demonstration purposes
  - Processes 640x480 images in <1s
  - Add GPU acceleration for ML model integration

## 🤝 How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ☕ Support Development

Like this project? Support future improvements:

[![Support via Saweria](https://img.shields.io/badge/Support-Saweria-FF5E5B)](https://saweria.co/ijajkeyboard)

## 📄 License

Distributed under MIT License. See `LICENSE` for more information.

---

**Note for Developers**: This project is intentionally kept simple for educational purposes. Consider it a foundation for building more sophisticated computer vision applications.
