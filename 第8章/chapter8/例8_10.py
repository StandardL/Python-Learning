#例8.10：矩阵运算
import numpy as np  #导入NumPy库

matr1 = np.mat("1 2 3;4 5 6;7 8 9")  #创建矩阵
print('创建的矩阵为：', matr1)

matr2 = matr1*3  #矩阵与数相乘
print('创建的矩阵为：', matr2)
print('矩阵相加结果为：', matr1+matr2)  #矩阵相加

print('矩阵相减结果为：', matr1-matr2)  #矩阵相减
print('矩阵相乘结果为：', matr1*matr2)  #矩阵相乘
print('矩阵对应元素相乘结果为：', np.multiply(matr1, matr2))












