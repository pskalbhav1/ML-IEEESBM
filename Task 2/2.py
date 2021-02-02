import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random


a=np.array([('James', 5, 48.5 ), ('Nail', 6, 52.5 ), ('Paul', 5, 42.1 ), ('Pit', 5, 40.11)],
           dtype=[('name', (np.str_, 10)), ('class', np.int32), ('height', np.float64)])
b = np.sort(a, order='class') 
c = np.sort(b, order='height') 
print(c)