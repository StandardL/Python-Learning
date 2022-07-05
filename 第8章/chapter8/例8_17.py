#例8.17：sort函数排序
import numpy as np  #导入NumPy库

np.random.seed(42)  #设置随机种子
arr = np.random.randint(1, 10, size = 10)  #生成随机数
print('创建的数组为：\n', arr)

arr.sort()  #直接排序
print('排序后数组为：\n', arr)

arr = np.random.randint(1,10,size = (3,3))  #生成3行3列的随机数
print('创建的数组为：\n', arr)

arr.sort(axis = 1)  #沿着横轴排序
print('排序后数组为：\n', arr)

arr.sort(axis = 0)  #沿着纵轴排序
print('排序后数组为：\n', arr)












