import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import pyttsx3
import os
import sys

print("Starting Sign Language Prediction...", flush=True)

# === Check if model files exist ===
model_path = "Model/keras_model.h5"
label_path = "Model/labels.txt"

if not os.path.exists(model_path) or not os.path.exists(label_path):
    print(f"Error: Model files not found in 'Model' folder.\nChecked:\n- {model_path}\n- {label_path}", flush=True)
    sys.exit()

# === Initialize video capture ===
print("Accessing webcam...", flush=True)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the camera.", flush=True)
    sys.exit()
else:
    print("Webcam initialized", flush=True)

# === Initialize hand detector and classifier ===
print("Loading hand detector and model...", flush=True)
detector = HandDetector(maxHands=1)
try:
    classifier = Classifier(model_path, label_path)
    print("Model loaded successfully.", flush=True)
except Exception as e:
    print(f"Model load error: {e}", flush=True)
    cap.release()
    cv2.destroyAllWindows()
    sys.exit()

# === Initialize text-to-speech ===
engine = pyttsx3.init()
print("Text-to-speech initialized.", flush=True)

# === Parameters ===
offset = 20
imgSize = 300
labels = ["Bad", "Call", "Eat", "Good", "Hello", "ILoveYou", "ThankYou"]
last_prediction = None

print("Running... Press 'q' to quit.", flush=True)

while True:
    try:
        success, img = cap.read()
        if not success:
            print("Failed to read from webcam.", flush=True)
            break

        imgOutput = img.copy()
        hands, img = detector.findHands(img)

        if hands:
            print("Hand detected.", flush=True)
            hand = hands[0]
            x, y, w, h = hand['bbox']
            x = max(x - offset, 0)
            y = max(y - offset, 0)
            x2 = min(x + w + offset, img.shape[1])
            y2 = min(y + h + offset, img.shape[0])

            imgCrop = img[y:y2, x:x2]
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

            if imgCrop.size == 0:
                print("Empty cropped image. Skipping frame.", flush=True)
                continue

            aspectRatio = h / w
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap: wCal + wGap] = imgResize
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap: hCal + hGap, :] = imgResize

            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            print(f"Prediction: {labels[index]} ({prediction[index] * 100:.2f}%)", flush=True)

            cv2.rectangle(imgOutput, (x, y - 70), (x + 400, y - 10), (0, 255, 0), cv2.FILLED)
            cv2.putText(imgOutput, labels[index], (x + 10, y - 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 2)
            cv2.rectangle(imgOutput, (x, y), (x2, y2), (0, 255, 0), 4)

            if last_prediction != labels[index]:
                last_prediction = labels[index]
                engine.say(labels[index])
                engine.runAndWait()

            cv2.imshow("Cropped", imgCrop)
            cv2.imshow("White Background", imgWhite)

        cv2.imshow("Output", imgOutput)

    except Exception as e:
        print(f"Runtime error: {e}", flush=True)
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting loop...", flush=True)
        break

cap.release()
cv2.destroyAllWindows()
print("Program finished.", flush=True)
