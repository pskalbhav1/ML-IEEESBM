from matplotlib import pyplot as plt 
import numpy as np
arr=np.array([np.random.randint(100,size=30)])
arr=arr.reshape((2,15))
colors=[np.random.randint(100,size=15)]
sizes=[np.random.randint(1000,size=15)]
plt.scatter(arr[0],arr[1], s=sizes, c=colors)
plt.colorbar().set_label('Random Colors')
plt.xlabel('X-axis -->')
plt.ylabel('Y-axis -->')
plt.show()