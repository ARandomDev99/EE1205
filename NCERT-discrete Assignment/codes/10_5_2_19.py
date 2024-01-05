import numpy
import matplotlib.pyplot as plt

# X-axis
n = numpy.arange(1, 31, 1)

# Y-axis
x = 4800 + 200 * n

# Plot graph
plt.stem(n, x)

# Label axes
plt.xlabel("n")
plt.ylabel("x(n)")

# Title
plt.title("$x(n) = 4800 + 200n$")

# Save x(n) vs n graph
plt.savefig("../plots/10_5_2_19.png")
