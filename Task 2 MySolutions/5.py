import matplotlib.pyplot as plt
import numpy as np

x1=np.array([10,14,20,26,30])
y1=np.array([20,30,40,20,10])
y2=np.array([40,30,10,20,30])

plt.plot(x1,y1,"-b",linestyle=":",label="line 1 = dotted")
plt.plot(x1,y2,"-r",linestyle="-",label="line 2 = dashed")
plt.legend(loc="upper right")
plt.xlabel("X axis")
plt.ylabel("Y aixs")
plt.title("Plot two or more lines with different styles")
plt.show()