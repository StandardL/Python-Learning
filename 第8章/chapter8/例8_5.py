#例8.5:二维数组索引
import numpy as np  #导入NumPy库

arr = np.array([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10, 11]])
print('创建的二维数组为：', arr)

print('索引结果为：', arr[0, 3:5]) #索引第0行中第3和4列的元素

#索引第2和3行中第3～5列的元素
print('索引结果为：', arr[1:, 2:])

print('索引结果为：', arr[:, 2]) #索引第2列的元素











