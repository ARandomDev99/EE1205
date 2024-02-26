import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 100)

v_laplace = 7 * (1 - np.exp(-t / .121))

v_dc = 7 * (1 - np.exp(-t / .121))

plt.plot(t, v_laplace, label="s-Domain", linestyle="-.", color="C0")
plt.plot(t, v_dc, label="DC", linestyle=":", color="C3")

plt.xlabel("Time ($s$)")
plt.ylabel("Voltage ($V_c$)")

plt.legend()

plt.savefig("plot.png")
