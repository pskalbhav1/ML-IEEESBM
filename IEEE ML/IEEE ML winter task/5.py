import matplotlib.pyplot as plt
x1 = [0, 20, 30]
y1 = [40, 0, 30]

x2 = [0, 20, 30]
y2 = [20, 40, 0]
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x1, y1, linewidth=5, label='dashed line', linestyle='dashed', color='red')
plt.plot(x2, y2, linewidth=7, label='dotted line', linestyle='dotted', color='blue')
plt.title("Plot with two or more lines with different style")
plt.show()
