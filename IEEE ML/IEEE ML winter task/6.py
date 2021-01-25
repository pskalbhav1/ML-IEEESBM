import numpy as np
import pandas as pd
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index1 = ['first', 'second', 'third']
column1 = ['1st', '2nd', '3rd']
dataframe = pd.DataFrame(data=array1, index=index1, columns=column1)
print(dataframe)
