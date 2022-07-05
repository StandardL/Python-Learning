#例8.8:实现数组组合
import numpy as np
# hstack函数横向组合
arr1 = np.arange(12).reshape(3,4)
print('创建的数组1为：\n',arr1)

arr2 = arr1*3
print('创建的数组2为：\n',arr2)
print('横向组合为：\n',np.hstack((arr1,arr2)))  #hstack函数横向组合

#使用vstack函数实现数组纵向组合
print('纵向组合为：\n',np.vstack((arr1,arr2)))  #vstack函数纵向组合

# 使用concatenate函数实现数组组合
print('横向组合为：\n',np.concatenate((arr1,arr2),axis = 1))  #concatenate函数横向组合
print('纵向组合为：\n',np.concatenate((arr1,arr2),axis = 0))  #concatenate函数纵向组合

# 使用hsplit函数实现数组横向分割
arr = np.arange(16).reshape(4,4)
print('创建的二维数组为：\n',arr)
print('横向分割为：\n',np.hsplit(arr, 2))  #hsplit函数横向分割

# vsplit函数实现数组纵向分割
print('纵向分割为：\n',np.vsplit(arr, 2))  #vsplit函数纵向分割

# split函数分割数组
print('横向分割为：\n',np.split(arr, 2, axis=1))  #split函数横向分割
print('纵向分割为：\n',np.split(arr, 2, axis=0))  #split函数纵向分割
















