# 🛡️ AI Missing Person Detection System

> A web-based application to digitally register, manage, and search missing person records — built with Python, Flask, and SQLite.

---

## 🌟 Live Demo
> 🔗 _Coming soon — deployment in progress on Render_

---

## 📌 About the Project

Every year, thousands of missing person cases go untracked due to lack of a centralized digital system. This project addresses that gap by providing a fast, accessible, and AI-ready web platform where authorities or families can:

- Register missing persons with photos
- Search existing records instantly
- Manage and delete resolved cases
- View dashboard statistics at a glance

Built as a real-world social impact project using Python and Flask, with future AI face recognition integration planned via OpenCV.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 📝 Register Missing Person | Submit name, age, location, and photo |
| 📷 Photo Upload | Upload and store images of missing persons |
| 🔍 Smart Search | Search records by name or details |
| 🗑️ Delete Record | Remove resolved/found cases |
| 📊 Dashboard | View total cases, recent registrations |
| 💾 Database Storage | Persistent SQLite storage |
| 🎨 Responsive UI | Mobile-friendly Bootstrap interface |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| Frontend | HTML5, CSS3, Bootstrap |
| AI (Upcoming) | OpenCV, Face Recognition |

---

## 📂 Project Structure

```
AI-Missing-Person-Detection-System/
│
├── app.py                  # Main Flask application
├── database.py             # Database setup and queries
├── face_detection.py       # Face detection module (OpenCV)
├── deploy.prototxt.txt     # OpenCV DNN model config
│
├── templates/              # HTML templates
│   ├── index.html
│   ├── register.html
│   ├── search.html
│   └── dashboard.html
│
├── static/
│   └── css/               # Stylesheets
│
├── uploads/               # Uploaded person photos
├── .gitignore
└── README.md
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/keerthanakumar02/AI-Missing-Person-Detection-System.git
cd AI-Missing-Person-Detection-System
```

### 2. Install dependencies
```bash
pip install flask opencv-python
```

### 3. Run the application
```bash
python app.py
```

### 4. Open in browser
```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### 🏠 Home Page
> _(Add screenshot here)_

### 📝 Register Page
> _(Add screenshot here)_

### 🔍 Search Page
> _(Add screenshot here)_

### 📊 Dashboard
> _(Add screenshot here)_

---

## 🔮 Upcoming Features

- [ ] 🤖 Face Recognition using OpenCV & deep learning
- [ ] 📷 Live Webcam Detection
- [ ] 📧 Email Notification when match is found
- [ ] 🧠 AI-based Person Matching algorithm
- [ ] ☁️ Cloud deployment on Render

---

## 🎯 Use Cases

- Police stations managing missing person cases
- NGOs tracking vulnerable individuals
- Community portals for public awareness

---

## 👩‍💻 Developer

**Keerthana K**

[![GitHub](https://img.shields.io/badge/GitHub-keerthanakumar02-black?logo=github)](https://github.com/keerthanakumar02)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> ⭐ If you found this project useful, please give it a star on GitHub!
