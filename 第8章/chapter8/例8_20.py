#例8.20：数组内去重
import numpy as np  #导入NumPy库

#title函数实现重复
arr = np.arange(5)
print('创建的数组为：', arr)
print('重复后数组为：', np.tile(arr,3))  #对数组进行重复

#repeat函数实现重复
np.random.seed(42)  #设置随机种子
arr = np.random.randint(0,10,size = (3,3))
print('创建的数组为：\n', arr)
print('重复后数组为：\n', arr.repeat(2, axis = 0))  #按行进行元素重复
print('重复后数组为：\n', arr.repeat(2, axis = 1))  #按列进行元素重复













