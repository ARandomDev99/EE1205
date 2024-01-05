import numpy
import matplotlib.pyplot as plt

# X-axis
n = numpy.arange(1, 11, 1)

# Y-axis
x = 15 * numpy.power(2, n)

# Plot graph
plt.stem(n, x)

# Label axes
plt.xlabel("n")
plt.ylabel("x(n)")

# Title
plt.title("$x(n) = 15(2^n)$")

plt.savefig("../plots/11_9_3_30.png")
