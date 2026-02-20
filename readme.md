🛣️ Pothole Detection using YOLOv8 with Edge Deployment
📌 Project Overview

This project focuses on automatic pothole detection and classification using deep learning techniques. The system classifies road images into two categories:

🛣️ Normal Road

🕳️ Pothole

The model is trained using the Kaggle Pothole Detection Dataset and optimized for real-time edge deployment on Raspberry Pi using ONNX Runtime.

This system is designed for:

Smart transportation systems

Road condition monitoring

Intelligent mobility solutions

Accident prevention systems

🎯 Problem Statement

Potholes are one of the major causes of:

Road accidents

Vehicle suspension damage

Increased maintenance cost

Traffic congestion

Manual inspection of roads is inefficient and not scalable.

An automated vision-based pothole detection system can:

Detect damaged roads in real-time

Assist municipal authorities

Enable smart vehicle warning systems

Improve autonomous driving safety

📂 Dataset

Dataset Name: Pothole Detection Dataset
Source: Kaggle
🔗 https://www.kaggle.com/datasets/atulyakumar98/pothole-detection-dataset

Dataset Details:

Two Classes:

Normal

Pothole

Real-world road images

Used for binary image classification

Organized into structured folders

Train–Validation split: 80:20

🛠️ Technologies Used

Python

PyTorch

Ultralytics YOLOv8

OpenCV

NumPy

Matplotlib

Scikit-learn

ONNX

ONNX Runtime

Raspberry Pi 4

🧠 Model Architecture

The project uses YOLOv8 Nano (Classification Model).

Architecture Details:

Pretrained Backbone: YOLOv8n-cls

Input Size: 224 × 224

Output Classes: 2

Loss Function: Cross-Entropy Loss

Optimizer: Adam

Transfer Learning with ImageNet weights

YOLOv8 Nano was selected because:

Lightweight architecture

Low memory usage

Fast inference speed

Suitable for Raspberry Pi deployment

🔬 Methodology
1️⃣ Dataset Preparation

Dataset organized into:

normal/

potholes/

Images resized to 224×224

Pixel normalization (0–1 scaling)

Train–Validation split (80:20)

Data shuffling for better generalization

2️⃣ Model Training

Training Configuration:

Platform: Google Colab

Framework: Ultralytics YOLOv8

Epochs: 10–20

Batch Size: 16

Optimizer: Adam

Device: GPU (when available)

Transfer learning was used to accelerate convergence and improve accuracy.

3️⃣ Model Evaluation

Evaluation Metrics:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

Training & Validation Loss Curves

The YOLOv8 Nano model demonstrated strong classification capability with minimal misclassification between pothole and normal road images.

📊 Results

Best Performing Model: YOLOv8 Nano

Performance Metrics:

Accuracy: ~95%

High Precision and Recall

Stable validation performance

Low overfitting observed

Confusion matrix analysis shows accurate separation between pothole and normal road images.

⚙️ Hardware Utilization
🖥️ Training Environment

Platform: Google Colab

Framework: PyTorch / Ultralytics

GPU Acceleration

12GB RAM (Colab Environment)

📦 Deployment Environment

Device: Raspberry Pi 4

RAM: 4GB

OS: Raspberry Pi OS

Inference Engine: ONNX Runtime

Model Format: ONNX

The trained YOLOv8 Nano model was exported to ONNX format for:

Faster inference

Lower latency

Platform independence

Real-time edge deployment

🚀 Deployment

The model is deployed on Raspberry Pi using:

ONNX Runtime

OpenCV for webcam capture

Real-time inference pipeline

The system captures live video frames, preprocesses them, runs inference using the ONNX model, and displays:

Prediction: Normal / Pothole
Confidence Score (%)

🔧 Optimization Techniques

Transfer Learning

Lightweight Nano Architecture

Hyperparameter tuning

Batch size optimization

ONNX model export for reduced inference latency

🌍 Applications

Smart Road Monitoring

Intelligent Transportation Systems

Municipal Road Maintenance

Autonomous Vehicles

Fleet Management Systems

Accident Prevention Systems

🏁 Conclusion

This project successfully implements a lightweight, high-accuracy deep learning framework for pothole detection and demonstrates real-time deployment on Raspberry Pi using ONNX Runtime.

YOLOv8 Nano provides an optimal balance between:

Accuracy

Computational efficiency

Memory usage

Real-time inference capability

The system shows strong potential for integration into smart city and intelligent mobility ecosystems.