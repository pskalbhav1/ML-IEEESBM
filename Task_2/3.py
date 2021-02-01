import numpy as np
arr=[]
import random
for i in range(0,27):
    arr.append(random.randint(0,100))
numarr=np.array(arr)
print(numarr.reshape((3,3,3)))