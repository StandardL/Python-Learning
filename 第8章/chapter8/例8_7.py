#例8.7:变换数组形态
import numpy as np  #导入NumPy库

arr = np.arange(12) #创建一维数组
print('创建的一维数组为：', arr)

print('新的一维数组为：', arr.reshape(3,4)) #设置数组的形状

print('数组维度为：', arr.reshape(3,4).ndim) #查看数组维度
print(arr)

#ravel函数数组展平工作
arr = np.arange(12).reshape(3, 4)
print('创建的二维数组为：\n', arr)

print('数组展平后为：', arr.ravel())

#flatten函数数组展平工作
print('数组展平为：', arr.flatten()) #横向展平

print('数组展平为：', arr.flatten('F')) #纵向展平
















