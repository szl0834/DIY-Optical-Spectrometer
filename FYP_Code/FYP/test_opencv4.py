import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./FYP/cat.png")
XYZ = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
col, row, a = img.shape
col2 = col // 2
print(col2)
""" B = img[col2, :, 0] / 255
G = img[col2, :, 1] / 255
R = img[col2, :, 2] / 255
Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
print("R:", R.shape) """
x = np.arange(0, row)
Y = XYZ[col2, :, 2]
""" plt.plot(x, B, color='blue', label='blue')
plt.plot(x, G, color='green', label='green')
plt.plot(x, R, color='red', label='red') """
plt.plot(x, Y, color='black', label='luma')
plt.show()

cv2.imshow("Image", XYZ)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("dimention:",img.shape)