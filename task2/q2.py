import numpy as np
import pandas as pd

inputs=np.array([('James', 5, 48.5 ), ('Nail', 6, 52.5 ), ('Paul', 5, 42.1 ), ('Pit', 5, 40.11)],
              dtype=[('name', (np.str_, 10)), ('class', np.int32), ('height', np.float64)])
classarrangment= np.sort(inputs, order='class')
heightarrangment = np.sort(classarrangment, order='height')
print(heightarrangment)
