import numpy
import matplotlib.pyplot as plt

# X-axis
n = numpy.linspace(0, 7, 8)

# Y-axis
x = 30 * (2 ** n)

# Plot graph
plt.stem(n, x)

# Plot (2, 120) and (4, 480) in a separate color and mark them.
plt.stem([2, 4], [120, 480], linefmt="C3")
plt.annotate("120", (2, 120), ha="center", va="bottom", xytext=(0, 10), textcoords="offset points")
plt.annotate("480", (4, 480), ha="center", va="bottom", xytext=(0, 10), textcoords="offset points")

# Label axes
plt.xlabel("n")
plt.ylabel("x(n)")

# Title
plt.title("$x(n) = 30(2^n)$")

plt.savefig("../figs/11_9_3_30.png")
