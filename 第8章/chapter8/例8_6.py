#例8.6:二维数组索引2
import numpy as np  #导入NumPy库

arr = np.array([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10, 11]])
#从两个序列的对应位置取出两个整数来组成下标：arr[0,1], arr[1,2], arr[2,3]
print('索引结果为：', arr[[(0,1,2), (1,2,3)]])

print('索引结果为：', arr[1:, (0,2,3)]) #索引第2、3行中第0、2、3列的元素

mask = np.array([1,0,1], dtype=np.bool)
print(mask)
#mask是一个布尔数组，它索引第1、3行中第2列的元素
print('索引结果为：', arr[mask, 2])













