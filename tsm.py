import matplotlib.pyplot as plt
from random import randint
import math


plt.axis('off')
plt.xlim(0, 20)
plt.ylim(0, 20)

total = 4


x, y = [], []

for i in range(total):
    x.append(randint(1, 15))
    y.append(randint(1, 15))

plt.plot(x, y, 's', marker="o", markersize=10,
         markerfacecolor="black", markeredgecolor="black")
plt.pause(2)

for i in range(total):
    plt.plot(x[i], y[i], markersize=10,
             markerfacecolor="black", markeredgecolor="black")
    plt.pause(1)

print(math.hypot(x[0], y[0])+math.hypot(x[1], y[1])+math.hypot(x[2], y[2]))

plt.show()


# points = []

# for i in range(0, 10):
#     points.append((random.randint(1, 1000), random.randint(1, 1000)))

# x = []
# y = []

# for i in cities:
#     x.append(points[i][0])
#     y.append(points[i][1])
#
