import numpy as np
import pandas as pd

m=np.random.rand(5,5)
df=pd.DataFrame(m, columns=('A','B','C','D','E'),index=['1','2','3','4','5'])
print(df)
