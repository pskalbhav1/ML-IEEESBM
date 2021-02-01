import numpy as np
arr=np.array([1023,5202,6230,1671,1682,5241,4532])
carr=np.sort(arr)
x=()
for i in carr:
    x+=np.where(arr==i)
print(x)