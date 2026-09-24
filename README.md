# 🎚️ AI Hand Gesture Volume Control

A computer vision-based **Hand Gesture Volume Control System** that allows users to control their computer's system volume using natural hand movements.

The project uses computer vision and hand-tracking technologies to detect the distance between the **thumb and index finger** and convert that distance into a corresponding system volume level.

## ✋ How It Works

The application uses the camera to detect and track the user's hand.

* When the **thumb and index finger move gradually farther apart**, the system volume **increases gradually**.
* When the **thumb and index finger move gradually closer together**, the system volume **decreases gradually**.

The distance between the two fingers is continuously measured and mapped to the system volume level.

## 🧠 Technologies & Libraries

The project uses computer vision and hand-tracking libraries such as:

* **OpenCV** — Camera access and computer vision processing
* **MediaPipe** — Real-time hand and finger landmark detection
* **PyAutoGUI / System Audio Control** — Controlling the system volume
* **Python** — Core programming language

## ⚙️ Key Features

* ✋ Real-time hand detection
* ☝️ Thumb and index finger tracking
* 📏 Finger-distance measurement
* 🔊 Gradual volume increase
* 🔉 Gradual volume decrease
* 🎥 Real-time camera processing
* 🖥️ Touch-free computer interaction

## 🎯 Project Objective

The main objective of this project is to create a **touch-free human-computer interaction system** where users can control system volume naturally through hand gestures instead of using traditional keyboard or mouse controls.

> **Move your fingers apart to increase the volume and bring them closer together to decrease it — all in real time using computer vision.**

