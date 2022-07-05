#例8.12：一维数组的广播机制
import numpy as np  #导入NumPy库

arr1 = np.array([[0,0,0],[1,1,1],[2,2,2],[3,3,3]])
print('创建的数组1为：',arr1)
print('数组1的shape为：',arr1.shape)
arr2 = np.array([1,2,3])

print('创建的数组2为：',arr2)
print('数组2的shape为：',arr2.shape)
print('数组相加结果为：',arr1 + arr2)













