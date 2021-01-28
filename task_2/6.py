import numpy as np
import pandas as pd 
arr=np.array(np.random.randint(10,size=25))
arr=arr.reshape((5,5))
data=pd.DataFrame(arr)
data.columns=['A','B','C','D','E']
data.index=[1,2,3,4,5]
print(data)
data.to_csv('sheet.csv')