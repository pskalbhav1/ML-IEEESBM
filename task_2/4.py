from matplotlib import pyplot as plt 
from matplotlib import style as stl
m=int(input("input slope for line\n>"))
x1=range(10)
x1=list(x1)
y1=range(0,10*m,m)
y1=list(y1)
plt.plot(x1,y1, label="a very interesting line")
plt.xlabel('X-Axis -->')
plt.ylabel('Y-Axis -->')
plt.title("a very interesting graph")
plt.legend()
plt.show()

