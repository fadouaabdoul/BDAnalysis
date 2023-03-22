import pandas as pd
import numpy as np

data = np.array([0, 7, 3, 6, 2, 8, 5, 9, 4]).reshape(3, -1)
df = pd.DataFrame(data, index=['One', 'Two', 'Three'], columns=['a', 'b', 'c'])

print("question 1",df)
