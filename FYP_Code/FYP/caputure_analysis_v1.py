import cv2
import numpy as np
from matplotlib import pyplot as plt


def linear(u):
    if u < 0.04045:
        gamma = 25 * u / 323
    else:
        gamma = pow(((200 * u + 11) / 211), (12 / 5))
    return gamma

def wavelength_to_rgb(wavelength, gamma=0.8):
    ''' taken from http://www.noah.org/wiki/Wavelength_to_RGB_in_Python
    This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    Additionally alpha value set to 0.5 outside range
    '''
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 750:
        A = 1.
    else:
        A = 0.3
    if wavelength < 380:
        wavelength = 380.
    if wavelength > 750:
        wavelength = 750.
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation)**gamma
        G = 0.0
        B = (1.0 * attenuation)**gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440))**gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490))**gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510))**gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580))**gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation)**gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R, G, B, A)

cap = cv2.VideoCapture(2)
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

img = frame
cv2.imwrite('spectrum.png', img)
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
x_1 = (np.sin((x - (row / 2)) * pixel_w / F_L2 + phi) + np.sin(alpha)) * d / k
Y_1 = np.flipud(XYZ[1, :])

x = x_1
y = Y_1
colors = np.array(np.vectorize(wavelength_to_rgb)(x))
fig, ax = plt.subplots()
ax.plot(x, y, color="gray")
for i in range(len(x) - 1):
    plt.fill_between([x[i], x[i+1]], [y[i], y[i+1]], color=colors[:, i], alpha = colors[3, i])
plt.savefig('WavelengthColors.png', dpi=200)
plt.show()
