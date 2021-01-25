import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
p=2
y= p*x
plt.plot(x,y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Graph of straight line')
plt.show()
