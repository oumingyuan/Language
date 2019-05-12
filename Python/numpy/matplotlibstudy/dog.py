import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-10, 11)
y1 = 2 * x + 5
y2 = x * x
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
# plt.plot(x, y1, "ob")
plt.plot(x, y2, "ob")
plt.show()