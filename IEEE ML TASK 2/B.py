import numpy as np
dt=np.dtype([('name',(np.str_, 10)),('class','i1'),('height','f4')])
x=np.array([('James', 5, 48.5 ), ('Nail', 6, 52.5 ), ('Paul', 5, 42.1 ), ('Pit', 5, 40.11)],dtype=dt)
x=np.sort(x,order='class')
x=np.sort(x,order='height')
print(x)
