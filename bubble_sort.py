import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

arr = list(range(1, 51))
np.random.shuffle(arr)
arr = arr.copy()

bars = ax.bar(range(len(arr)), arr, color='cyan')
ax.set_xlim(-1, len(arr))
ax.set_ylim(0, 55)
ax.axis('off')
title = ax.set_title('Bubble Sort', color='white', fontsize=14)

def bubble_sort_steps(arr):
    steps = []
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            steps.append((a.copy(), j))
    return steps

steps = bubble_sort_steps(arr)

def update(frame):
    data, idx = steps[frame]
    for bar, h in zip(bars, data):
        bar.set_height(h)
        bar.set_color('cyan')
    bars[idx].set_color('red')
    bars[idx+1].set_color('yellow')
    return bars

ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=50)
plt.show()
