import matplotlib.pyplot as plt
import numpy as np

# X-axis
n = np.array([])

# Y-axis
x = np.array([])

# Load data from output of C program
with open("11_9_3_30cout.txt") as file:
    for line in file.readlines():
        split_line = line.split(" = ")
        n = np.append(n, int(split_line[0][2:-1]))
        x = np.append(x, int(split_line[1]))

# Plot graph
plt.stem(n, x)

# Plot (2, 120) and (4, 480) in a separate color and mark them.
plt.stem([2, 4], [120, 480], linefmt="C3")
plt.annotate("120", (2, 120), ha="center", va="bottom", xytext=(0, 10), textcoords="offset points")
plt.annotate("480", (4, 480), ha="center", va="bottom", xytext=(0, 10), textcoords="offset points")

# Label axes
plt.xlabel("n")
plt.ylabel("x(n)")

plt.savefig("../figs/11_9_3_30.png")
