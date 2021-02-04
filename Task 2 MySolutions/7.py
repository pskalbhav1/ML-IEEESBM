import matplotlib.pyplot as plt
import numpy as np
from numpy import random

l1=int(input("Enter no. of entries for scatter 1 = "))
x1=random.rand(l1)
y1=random.rand(l1)
l2=int(input("Enter no. of entries for scatter 2 = "))
x2=random.rand(l2)
y2=random.rand(l2)
l3=int(input("Enter no. of entries for scatter 3 = "))
x3=random.rand(l3)
y3=random.rand(l3)

plt.scatter(x1,y1, color="red", alpha=0.25, s=800)

plt.scatter(x2,y2, color="blue", alpha=0.95, s=200)

plt.scatter(x3,y3, color="Purple", alpha=0.45, s=400)

plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.show()