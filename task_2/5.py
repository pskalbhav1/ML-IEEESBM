from matplotlib import pyplot as plt    
from matplotlib import style as stl
l1x=[10,20,30]
l1y=[20,40,10]
l2x=[10,20,30]
l2y=[40,10,30]
plt.plot(l1x,l1y,  ':', label="line1-dotted",linewidth=3)
plt.plot(l2x,l2y,  '--', label="line2-dashed",linewidth=7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("stonks")
plt.legend()
plt.show()

