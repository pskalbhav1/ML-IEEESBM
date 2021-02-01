import pandas
import numpy
a=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
df=pandas.DataFrame(data=a,columns=['a','b','c'],index=['1','2','3'])
print(df)
