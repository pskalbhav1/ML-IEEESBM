import pandas as pd
import numpy as np
x=np.random.random(size =(5,5))
sheet=pd.DataFrame(data=x,columns=['a','b','c','d','e'],index=['1','2','3','4','5'])
print(sheet)
