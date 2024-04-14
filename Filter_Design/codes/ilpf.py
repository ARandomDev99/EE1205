# Plot 2 subplots
# 1. Ideal Low Pass Filter Frequency Response
# 2. Ideal Low Pass Filter Impulse Response

import numpy as np
import matplotlib.pyplot as plt

# Frequency response of Ideal Low Pass Filter
w = np.linspace(-np.pi, np.pi, 1000)
H = np.zeros_like(w)
H[np.abs(w) <= .025 * np.pi] = 1
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(w, H)
plt.title('Ideal Low Pass Filter Frequency Response')
plt.xlabel('$\\omega$')
plt.ylabel('Magnitude')
plt.plot(.025 * np.pi, 0, 'ro', label='Cutoff Frequency')
plt.legend()
plt.grid()

# Impulse response of Ideal Low Pass Filter
n = np.linspace(-100, 100, 101)
h = np.sin(.025 * np.pi * n) / (np.pi * n)
h[n == 0] = .025
plt.subplot(2, 1, 2)
plt.stem(n, h, markerfmt='.')
plt.title('Ideal Low Pass Filter Impulse Response')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.grid()

plt.subplots_adjust(hspace=.5)

plt.savefig('LPF_FIR.png')
