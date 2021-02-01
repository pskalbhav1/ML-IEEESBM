import numpy as np
import pandas as pd
arr=np.array([50,19,40,23])
df=pd.DataFrame(data={'Numbers':arr},index=["num1","num2","num3","num4"])
print(df)