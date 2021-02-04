import numpy as np
import random

ar=np.ones((3,3,3),int)

for x in range(3):
    for y in range(3):
        for z in range(3):
            ar[x][y][z]=random.randint(0,10000)
        
print(ar)