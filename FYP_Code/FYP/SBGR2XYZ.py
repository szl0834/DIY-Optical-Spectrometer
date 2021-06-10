import cv2
import numpy as np
from matplotlib import pyplot as plt


def linear(u):
    if u < 0.04045:
        gamma = 25 * u / 323
    else:
        gamma = pow(((200 * u + 11) / 211), (12 / 5))
    return gamma


img = cv2.imread("./FYP/cat.png")
img2 = img.astype(float)
col, row, a = img.shape
for x in range(col):
    for y in range(row):
        for z in range(a):
            img2[x, y, z] = linear(img[x, y, z] / 255) * 255

img3 = img2.astype(int)
print(img3*255)
XYZ = cv2.cvtColor(img2, cv2.COLOR_BGR2XYZ)
cv2.imshow("Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
col2 = col // 2
x = np.arange(0, row) * 4.72 - 246.8
Y = XYZ[col2, :, 1]
plt.plot(x, Y, color='black', label='luma')
plt.show()