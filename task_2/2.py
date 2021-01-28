import numpy as np
import pandas as pd
student_info=np.array([('Harry',7,100.1),('Potter',7, 99.5),('Snape',9,120.2),('Lily',10,120.2)], dtype=[('name', (np.str_, 10)), ('class', np.int16), ('height', np.float64)])
student_info = np.sort(student_info, order='class') 
student_info = np.sort(student_info, order='height') 
print(student_info)