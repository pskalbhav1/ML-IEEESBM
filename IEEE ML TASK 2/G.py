import math
import random
import matplotlib.pyplot as plt
no_of_balls = 30
x = [random.triangular() for i in range(no_of_balls)]
y = [random.gauss(1, 1.9) for i in range(no_of_balls)]
colors = [np.random.randint(1,7) for i in range(no_of_balls)]
areas = [math.pi * random.randint(7, 18)**2 for i in range(no_of_balls)]
plt.figure()
plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
plt.axis([0.0, 2.0, 0.0, 2.0])
plt.show()
