import numpy
import matplotlib.pyplot as plt

# X-axis
n = numpy.arange(0, 31, 1)

# Y-axis
x = 5000 + 200 * n

# Plot graph
plt.stem(n, x)

# Label axes
plt.xlabel("n")
plt.ylabel("x(n)")

# Save x(n) vs n graph
plt.savefig("../figs/10_5_2_19.png")
