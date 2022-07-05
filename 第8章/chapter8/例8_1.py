#例8.1:创建数组查看属性
import numpy as np  #导入NumPy库

arr1 = np.array([1, 2, 3, 4])  #创建一维数组
print('创建的数组为：', arr1)

arr2 = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])    #创建二维数组
print('创建的数组为：\n', arr2)

#查看数组结构
print('数组维度为：', arr2.shape)

# 查看数组类型
print('数组类型为：', arr2.dtype)

#查看数组元素个数
print('数组元素个数为：', arr2.size)

#查看数组每个元素大小
print('数组每个元素大小为：', arr2.itemsize)


