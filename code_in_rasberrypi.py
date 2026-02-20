mv ~/Downloads/best.onnx ~/
cd ~
ls


sudo apt install python3-venv -y

python3 -m venv myenv

source myenv/bin/activate

pip install onnxruntime numpy opencv-python

nano live_detection.py


import numpy as np
import cv2
import onnxruntime as ort

# Load ONNX model
session = ort.InferenceSession("yolo.onnx")  # Ensure the correct model file
input_name = session.get_inputs()[0].name

# Label names (Ensure the order matches your training)
class_names = ['normal', 'pothole']

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break
    
    # Resize frame to 224x224 (or your model input size)
    img_resized = cv2.resize(frame, (224, 224))

    # Convert from BGR to RGB
    img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

    # Normalize the image
    img_rgb = img_rgb.astype(np.float32) / 255.0

    # HWC → CHW
    img_rgb = np.transpose(img_rgb, (2, 0, 1))

    # Add batch dimension
    img_rgb = np.expand_dims(img_rgb, axis=0)

    # Run inference
    outputs = session.run(None, {input_name: img_rgb})

    # Convert to numpy array and apply softmax
    logits = outputs[0]
    exp_logits = np.exp(logits)
    probabilities = exp_logits / np.sum(exp_logits)

    # Get predicted class
    predicted_class = np.argmax(probabilities)
    confidence = probabilities[0][predicted_class] * 100

    # Display the prediction on the frame
    cv2.putText(frame, f"Prediction: {class_names[predicted_class]} - {confidence:.2f}%", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Real-time Road Anomaly Detection", frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()

python live_detection.py