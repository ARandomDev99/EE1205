import matplotlib.pyplot as plt
import numpy as np

# X-axis
t = np.linspace(-.2, 1, 200)

# Y-axis
# V_c = 7u(t)(1 - e^(-t / 0.121))
V_c = 7 * np.heaviside(t, 1) * (1 - np.exp(-t / .121))

plt.plot(t, V_c)

plt.xlabel("Time ($s$)")
plt.ylabel("Voltage ($V_c$)")

plt.savefig("plot.png")
