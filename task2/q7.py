import numpy as np
import random
import matplotlib.pyplot as plt
import math
# create random data
no_of_balls = 25
x = [random.triangular() for i in range(no_of_balls)]
y = [random.gauss(0.5, 0.25) for i in range(no_of_balls)]
colors = [random.randint(1, 6) for i in range(no_of_balls)]
areas = [math.pi * random.randint(5, 20)**2 for i in range(no_of_balls)]
# draw the plot
plt.figure()
plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.show()
