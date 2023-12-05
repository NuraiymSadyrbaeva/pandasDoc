import pandas as pd
import numpy as np

#hier wird series erstellt
data = [55, 14, 2, 63]
index = ['A', 'B', 'C', 'D']
s = pd.Series(data, name="age", index=index)
#print(s["B"])
data_dict = {
    "A": 55,
    "B": 14,
    "C": 2,
    "D": 63
    }

s2 = pd.Series(data_dict)
print(s2)

s3 = pd.Series(np.random.randn(10), dtype=np.int32)
print(s3)

