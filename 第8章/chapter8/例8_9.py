#例8.9：创建NumPy矩阵
import numpy as np  #导入NumPy库

matr1 = np.mat("1 2 3;4 5 6;7 8 9") #使用分号隔开数据
print('创建的矩阵为：\n', matr1)

matr2 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('创建的矩阵为：', matr2)

arr1 = np.eye(3)
print('创建的数组1为：\n', arr1)

arr2 = 3*arr1
print('创建的数组2为：\n', arr2)

print('创建的矩阵为：\n', np.bmat("arr1 arr2; arr1 arr2"))

print('创建的矩阵为：\n', np.bmat("arr1 arr2"))

print('创建的矩阵为：\n', np.bmat("arr1; arr2"))














