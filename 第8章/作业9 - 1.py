import numpy as np
mat1 = np.matrix([[0, 1], [0, 0]])
mat2 = np.matrix([[0, 0], [0, 0]])
mat = np.bmat('mat1 mat1 mat1 mat2; mat1 mat1 mat1 mat2; mat1 mat1 mat1 mat2; mat1 mat1 mat1 mat2')
print(mat)