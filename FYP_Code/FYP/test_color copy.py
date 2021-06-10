import matplotlib.pyplot as plt
import numpy as np


def wavelength_to_rgb(wavelength, gamma=0.8):
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


if __name__ == '__main__':
    x = np.linspace(300, 1000, 700)
    y = np.sin(x / 100)  # replace with your function / measured values.
    colors = np.array(np.vectorize(wavelength_to_rgb)(x))
    fig, ax = plt.subplots()
    ax.plot(x, y, color="gray")
    for i in range(len(x) - 1):
        plt.fill_between([x[i], x[i + 1]], [y[i], y[i + 1]],
                         color=colors[:, i],
                         alpha=colors[3, i])
    plt.show()