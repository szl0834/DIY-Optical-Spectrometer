import cv2
import numpy as np
from matplotlib import pyplot as plt


def linear(u):
    if u < 0.04045:
        gamma = 25 * u / 323
    else:
        gamma = pow(((200 * u + 11) / 211), (12 / 5))
    return gamma


cap = cv2.VideoCapture(2)
while (1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

img = frame
col, row, a = img.shape
col2 = col // 2
img2 = img.astype(float)[col2, :, :]

for x in range(row):
    for y in range(a):
        img2[x, y] = linear(img2[x, y] / 255)

convert_XYZ = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722],
                        [0.0193, 0.1192, 0.9505]])

XYZ = np.dot(convert_XYZ, np.fliplr(img2).T)

sensor_w = 6.4
F_L2 = 4.784575119803315
phi = 0.942087992419107
alpha = 0
d = 1000
k = 1
pixel_w = sensor_w / row
x = np.arange(0, row)
x_1 = np.flipud(
    (np.sin((x - (row / 2)) * pixel_w / F_L2 + phi) + np.sin(alpha)) * d / k)
print(XYZ)
Y = XYZ[1, :]
B = img[col2, :, 0] / 255
G = img[col2, :, 1] / 255
R = img[col2, :, 2] / 255
""" plt.plot(x_1, B, color='blue', label='blue')
plt.plot(x_1, G, color='green', label='green')
plt.plot(x_1, R, color='red', label='red') """
plt.plot(x_1, Y, color='black', label='luma')
plt.show()