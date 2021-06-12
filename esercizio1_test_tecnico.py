import numpy as np
import pandas as pd

data = pd.read_csv('exercise_1.txt', header = None)
out = np.cumsum(np.sum(np.array_split(data, 100), axis = 1))
### Visto che il task richiedeva una lista e out è un ndarray
out = out.tolist()
