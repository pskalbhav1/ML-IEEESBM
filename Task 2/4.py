import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random


x = np.linspace(-1,1,100)
p = 0.5
y = p*x
plt.plot(x,y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Straight Line Plot")
plt.show()