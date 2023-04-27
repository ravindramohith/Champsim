import matplotlib.pyplot as plt
import numpy as np

# Data for the first graph
x1 = np.arange(3)
x2 = np.arange(3)
x3 = np.arange(3)

lru_1 = [0.165301, 0.166627, 0.168316]
lfu_1 = [0.165139, 0.166106, 0.167362]
fifo_1 = [0.165301, 0.166627, 0.168316]
random_1 = [0.165295, 0.16658, 0.168727]
lru_2 = [0.165301, 0.166627, 0.168316]
lfu_2 = [0.165139, 0.166106, 0.167362]
fifo_2 = [0.165301, 0.166627, 0.168316]
random_2 = [0.165295, 0.16658, 0.168727]
lru_3 = [0.158098, 0.159381, 0.160617]
lfu_3 = [0.157393, 0.159203, 0.160758]
fifo_3 = [0.158098, 0.159339, 0.160559]
random_3 = [0.157926, 0.159012, 0.160923]

# Save the first subplot as a PNG image
fig1, ax1 = plt.subplots(figsize=(5, 5))
width = 0.2
ax1.bar(x1 - 0.3, lru_1, width, color="aquamarine")
ax1.bar(x1 - 0.1, lfu_1, width, color="cyan")
ax1.bar(x1 + 0.1, fifo_1, width, color="blue")
ax1.bar(x1 + 0.3, random_1, width, color="darkblue")
ax1.set_xticks(x1)
ax1.set_xticklabels([4, 16, 32])
ax1.set_xlabel("LLC Ways")
ax1.set_ylabel("IPC value")
ax1.set_title("Exclusive for cadical-1227B champsimtrace")
ax1.legend(["LRU", "LFU", "FIFO", "Random"])
fig1.savefig("exclusive_1227.png")

# Save the second subplot as a PNG image
fig2, ax2 = plt.subplots(figsize=(5, 5))
ax2.bar(x1 - 0.3, lru_2, width, color="yellow")
ax2.bar(x1 - 0.1, lfu_2, width, color="orange")
ax2.bar(x1 + 0.1, fifo_2, width, color="red")
ax2.bar(x1 + 0.3, random_2, width, color="brown")
ax2.set_xticks(x2)
ax2.set_xticklabels([4, 16, 32])
ax2.set_xlabel("LLC Ways")
ax2.set_ylabel("IPC value")
ax2.set_title("Non Inclusive for cadical-1227B champsimtrace")
ax2.legend(["LRU", "LFU", "FIFO", "Random"])
fig2.savefig("non_inclusive_1227.png")

# Save the third subplot as a PNG image
fig3, ax3 = plt.subplots(figsize=(5, 5))
ax3.bar(x3 - 0.3, lru_3, width, color="aquamarine")
ax3.bar(x3 - 0.1, lfu_3, width, color="chartreuse")
ax3.bar(x3 + 0.1, fifo_3, width, color="green")
ax3.bar(x3 + 0.3, random_3, width, color="darkgreen")
ax3.set_xticks(x3)
ax3.set_xticklabels([4, 16, 32])
ax3.set_xlabel("LLC Ways")
ax3.set_ylabel("IPC value")
ax3.set_title("Inclusive for cadical-1227B champsimtrace")
ax3.legend(["LRU", "LFU", "FIFO", "Random"])
fig3.savefig("inclusive_1227.png")

# Show the figure
# plt.show()
