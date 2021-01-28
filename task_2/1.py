import numpy as np
arr=input("enter space seperated numbers\n")
arr=arr.split()
arr=np.array(arr,np.int32)
print(arr.argsort(axis=0))

