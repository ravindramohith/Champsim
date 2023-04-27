import matplotlib.pyplot as plt
import numpy as np

# Data for the first graph
x1 = np.arange(3)
x2 = np.arange(3)
x3 = np.arange(3)

lru_1 = [0.306616, 0.310411, 0.315366]
lfu_1 = [0.305921, 0.307186, 0.308989]
fifo_1 = [0.306616, 0.310411, 0.315366]
random_1 = [0.3066, 0.310163, 0.314371]
lru_2 = [0.306616, 0.310411, 0.315366]
lfu_2 = [0.305921, 0.307186, 0.308989]
fifo_2 = [0.306616, 0.310411, 0.315366]
random_2 = [0.3066, 0.310163, 0.314371]
lru_3 = [0.301933, 0.307455, 0.312418]
lfu_3 = [0.289828, 0.305282, 0.309736]
fifo_3 = [0.301933, 0.306826, 0.311461]
random_3 = [0.301393, 0.306668, 0.31109]

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
ax1.set_title("Exclusive for kissat-1802B champsimtrace")
ax1.legend(["LRU", "LFU", "FIFO", "Random"])
fig1.savefig("exclusive_kiss.png")

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
ax2.set_title("Non Inclusive for kissat-1802B champsimtrace")
ax2.legend(["LRU", "LFU", "FIFO", "Random"])
fig2.savefig("non_inclusive_kiss.png")

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
ax3.set_title("Inclusive for kissat-1802B champsimtrace")
ax3.legend(["LRU", "LFU", "FIFO", "Random"])
fig3.savefig("inclusive_kiss.png")
