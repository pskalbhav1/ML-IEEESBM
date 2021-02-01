import matplotlib.pyplot as plt
a=[10,20,30]
b=[40,10,30]
c=[10,20,30]
d=[20,40,10]
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(a,b, color='red', linewidth = 3,  label = 'line1-dotted',linestyle='dashed')
plt.plot(c,d, color='blue', linewidth = 3,  label = 'line2-dashed',linestyle='dotted')
plt.title('graph with two lines')
plt.legend(loc='best')
plt.show()
