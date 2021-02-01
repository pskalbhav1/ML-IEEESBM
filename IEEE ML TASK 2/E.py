import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[40,10,30]
x2=[10,20,30]
y2=[20,40,10]
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(x1,y1, color='red', linewidth = 3,  label = 'line1',linestyle='dashed')
plt.plot(x2,y2, color='blue', linewidth = 5,  label = 'line2',linestyle='dotted')
plt.title('graph with two lines')
plt.show()
