import cv2
from PIL import Image
import numpy as np
import time
import datetime
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

# Get a frame from the capture device
while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
# print(frame)
print(cap)
print(ret)
print(frame)
cap.release()
