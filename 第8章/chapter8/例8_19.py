#例8.19：数组内去重
import numpy as np  #导入NumPy库

names = np.array(['小明', '小黄', '小花', '小明',  '小花', '小兰', '小白'])
print('创建的数组为：', names)

print('去重后的数组为：', np.unique(names))


ints = np.array([11,1,2,3,4,4,5,6,6,7,8,8,9,10])  #创建数值型数据
print('创建的数组为：', ints)
print('去重后的数组为：', np.unique(ints))

print(sorted(set(names)))












