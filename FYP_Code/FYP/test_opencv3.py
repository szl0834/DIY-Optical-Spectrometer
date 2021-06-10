import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)
ret, frame = cap.read()
print("cap:", type(cap))
""" print("ret:",type(ret))
print("frame:",type(frame))
print("dimention:",frame.shape)
R = frame[240,:,0]
print("R:",R.shape)
x = np.arange(0,640)
plt.plot(x,R) 
plt.show() """