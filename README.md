# 🧠 AI-Powered Drone for Automated Building Crack Detection

An **AI-powered drone system** designed for the **automatic detection of building facade cracks and structural anomalies**. This project integrates **computer vision**, **deep learning**, and **autonomous drone navigation** to enhance the accuracy and efficiency of **structural health monitoring (SHM)** in civil infrastructure.

---

## 🚀 Overview

Traditional crack detection methods are labor-intensive, time-consuming, and prone to human error. This project introduces a **fully automated drone-based inspection framework** that combines **high-resolution imaging**, **autonomous flight planning**, and **AI-driven crack detection models** to identify and classify surface defects in buildings.

---

## 🧩 Key Features

* **Autonomous Drone Navigation:** Uses pre-defined flight paths or SLAM-based autonomous movement for area coverage.
* **High-Resolution Imaging:** Captures detailed façade images using onboard camera modules.
* **AI-Based Crack Detection:** Implements a **CNN (Convolutional Neural Network)** model trained on crack datasets to detect and localize structural cracks.
* **Real-Time Monitoring:** Sends live video feed and analysis results to the control system or cloud dashboard.
* **Data Storage & Analysis:** Automatically stores inspection data for later review and maintenance planning.

---

## 🛠️ Technologies Used

| Component                 | Technology                            |
| ------------------------- | ------------------------------------- |
| **Drone Control**         | Pixhawk Flight Controller / Ardupilot |
| **Programming Languages** | Python, C++                           |
| **AI/ML Frameworks**      | TensorFlow, OpenCV, PyTorch           |
| **Flight Path & Control** | Mission Planner / ROS                 |
| **Database & Storage**    | Firebase / MongoDB                    |
| **Frontend (Dashboard)**  | React.js / Flask (optional)           |

---

## ⚙️ System Architecture

1. **Drone captures facade images** during autonomous flight.
2. **AI model processes images** to detect cracks and mark affected areas.
3. **Data transmitted** to the base station or cloud server.
4. **Dashboard visualizes** detected flaws and severity levels.

---

## 🧠 AI Model Details

* Model Type: Convolutional Neural Network (CNN)
* Input: RGB facade images (resized to 224×224)
* Output: Binary classification (Crack / No Crack) + Bounding Box (optional)
* Dataset: Public crack datasets (e.g., SDNET2018, Concrete Crack Dataset)
* Training Accuracy: ~99% (can be improved with custom data)

---


## 📸 Output Example

* Detected cracks highlighted in red boxes(Heat Map).
* Confidence scores displayed per image.
* Real-time feed available on control dashboard.

---

## 🧭 Future Enhancements

* Integrate **thermal imaging** for internal crack detection.
* Use **3D mapping (LiDAR)** for full structural modeling.
* Deploy **edge AI models** on drone hardware for real-time inference.

---

## 🤝 Contributing

Contributions are welcome! Please open a pull request or issue for suggestions and improvements.




---

## 👥 Team

Under the project: *AI-Powered Drone for Automated Building Crack Detection*
Guided by **Mentor Karobi Sarkar** Assistant Professor at Narula Institute of Technology(Kolkata),and Research Scholar at IIEST Shibpur.
