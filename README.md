# 📸 SnapClass — AI-Powered Attendance System

SnapClass is a next-generation, automated attendance and session management platform that leverages cutting-edge computer vision, voice biometrics, and machine learning to eliminate manual roll calls. 

---

## 🚀 Key Features

* **📸 FaceID Room Scan:** Recognizes and marks an entire classroom of students from a single group photo in under 3 seconds.
* **🎙️ Sequential Voice ID Roll-Call:** Audio-AI model matches student voice biometrics ("Present") against stored voice embeddings.
* **📱 QR-Driven Rosters:** Instant enrollment and course tracking using dynamic QR codes.
* **📊 Smart Analytics Dashboard:** Auto-generated reports, attendance trends, streaks, and exportable CSV files.
* **🔒 Secure Cloud Infrastructure:** Robust user authentication and real-time syncing across devices.

---

## 🛠️ Comprehensive Tech Stack

SnapClass is built using a modern, multi-tiered technology stack combining high-performance web frameworks, audio-visual AI pipelines, and scalable cloud databases:

### 1. Core Language & Backend Frameworks
* **Python:** The core programming language powering all backend scripts, machine learning models, and automation workflows.
* **FastAPI:** High-performance asynchronous API layer used to handle client requests, biometric payload processing, and fast endpoint communication.
* **Flask:** Lightweight routing and landing layer handling initial server requests and web views.

### 2. Frontend & User Interface
* **Streamlit:** Reactive frontend architecture providing clean, interactive dashboards for both students and teachers.
* **HTML5 & CSS3:** Custom-designed layouts, modern component styling, and typography for the landing and auth portals.

### 3. Machine Learning, Computer Vision & Audio AI
* **Machine Learning (ML):** Core classification and pattern-matching models utilized for biometric verification.
* **OpenCV:** Real-time computer vision library used for image capture, preprocessing, and bounding-box rendering during face scans.
* **Face Recognition (Dlib-based):** High-fidelity facial landmark detection and metric encoding extraction for accurate student identification.
* **Resemblyzer:** Deep learning framework used to generate unique numerical voice embeddings from audio samples.
* **Librosa:** Audio and music processing library used for feature extraction (MFCCs, spectrograms) during voice verification.

### 4. Database & Cloud Storage
* **Supabase:** Real-time PostgreSQL database infrastructure providing lightning-fast data querying, secure role-based access control, and user management.

---

## 📁 Project Architecture

```text
snapclass/
├── .streamlit/             # Streamlit configuration settings & themes
├── src/                    # Core modules (Face recognition, audio processing, DB handlers)
├── static/                 # Static assets (CSS styles, brand logos, UI images)
├── templates/              # HTML/Jinja2 templates for landing & views
├── app.py                  # Main application entry point
├── requirements.txt        # Project Python dependencies
└── README.md               # Project documentation
