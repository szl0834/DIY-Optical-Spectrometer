import numpy as np
from matplotlib import pyplot as plt
sensor_w = 6.4
F_L2 = 3.6
phi = 0.9376
alpha = 0
d = 1000
k = 1
row = 3840
pixel_w = sensor_w / row
x = np.arange(0, row)
x_1 = (np.sin((x - (row / 2)) * pixel_w / F_L2 + phi) + np.sin(alpha)) * d / k
plt.plot(x, x_1, color='black', label='luma')
plt.show()