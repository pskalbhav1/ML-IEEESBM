import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,20,30])
y1=np.array([20,40,0])
y2=np.array([40,0,30])

plt.xlim(0,30)
plt.ylim(0,40)
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.title('Plot with two or more lines with different styles')

plt.plot(x,y1,'-',color='b', label='Line1- dotted')
plt.plot(x,y2,'--',color='r', label='Line2- dotted')
plt.show()
