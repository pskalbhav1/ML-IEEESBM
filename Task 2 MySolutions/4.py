import matplotlib.pyplot as plt 
import numpy as np

p=int(input("Enter p = "))
xpoints=np.array([1,5])
ypoints=np.array([p*1,p*5])

plt.plot(xpoints,ypoints)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("y=px")
plt.show()

