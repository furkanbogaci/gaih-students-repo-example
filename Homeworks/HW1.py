import numpy as np
matrix = [[],[],[]]

for i in range(0,3):
  for j in range(0,3):
      for k in np.random.randint(0,10,1):
        matrix[i].append(k)

for i in range(3):
      print(matrix[i])
