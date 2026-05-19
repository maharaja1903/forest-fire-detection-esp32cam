# Real-Time Forest Fire Detection using ESP32-CAM and YOLOv11

## Overview

This project detects forest fires in real-time using an ESP32-CAM module and a YOLOv11 deep learning model. The system captures live video from ESP32-CAM, performs fire detection using TensorRT optimized inference, and sends emergency SMS and voice call alerts using Twilio.

---

## Features

* Real-time fire detection
* ESP32-CAM live video streaming
* YOLOv11 TensorRT inference
* SMS alert system
* Automated voice call alerts
* Multi-threaded alert handling
* GPU accelerated detection

---

## Hardware Components

* ESP32-CAM
* FTDI Programmer
* Buzzer
* LED Indicator
* Laptop/Desktop with GPU

---

## Software Used

* Python
* OpenCV
* PyTorch
* Ultralytics YOLOv11
* Twilio API
* TensorRT

---

## Python Version

Python 3.10 recommended

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Project Structure

```text
forest-fire-detection-esp32cam/
│
├── detect.py
├── requirements.txt
├── README.md
├── .gitignore
├── best.engine
├── screenshots/
└── docs/
```

---

## Run the Project

```bash
python detect.py
```

---

## ESP32-CAM Stream URL

```python
STREAM_URL = "http://YOUR_ESP32_CAM_IP:81/stream"
```

Example:

```python
STREAM_URL = "http://10.251.170.250:81/stream"
```

---

## Twilio Alert System

This project sends:

* SMS alerts
* Automated voice call alerts

when fire is detected.

---

## Model Information

This project uses TensorRT optimized YOLOv11 engine:

```text
best.engine
```

for high-speed real-time inference.

---

## Detection Results

Add screenshots inside:

```text
screenshots/
```

Example:

* detection1.png
* telegram_alert.png
* fire_detected.png

---

## Future Improvements

* Drone integration
* GSM module support
* Cloud dashboard
* Edge AI deployment
* GPS-based fire location tracking

---

## Author

Maharaja
Santhiga
---
