x=np.linspace(10,30,100)
y1=[((-3)*i + 70) for i in x if i<=20]
y2=[((2*i)-30) for i in x if i>20]
y3=[(2*i) for i in x if i<=20]
y4=[((-3*i)+100) for i in x if i>20]

y5=y1+y2
y6=y3+y4
plt.plot(x,y5,'.',color='b',label='line1-dotted')
plt.plot(x,y6,'--', color='r',label='line2-dashed')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.title("Plot with two or more lines with different styles")
plt.show()