#例8.21：常用统计函数
import numpy as np  #导入NumPy库

arr = np.arange(20).reshape(4,5)
print('创建的数组为：\n',arr)
print('数组的和为：',np.sum(arr))  #计算数组的和
print('数组横轴的和为：',arr.sum(axis = 0))  #沿着横轴计算求和
print('数组纵轴的和为：',arr.sum(axis = 1))  #沿着纵轴计算求和
print('数组的均值为：',np.mean(arr))  #计算数组均值
print('数组横轴的均值为：',arr.mean(axis = 0))  #沿着横轴计算数组均值
print('数组纵轴的均值为：',arr.mean(axis = 1))  #沿着纵轴计算数组均值
print('数组的标准差为：',np.std(arr))  #计算数组标准差
print('数组的方差为：',np.var(arr))  #计算数组方差
print('数组的最小值为：',np.min(arr))  #计算数组最小值
print('数组的最大值为：',np.max(arr))  #计算数组最大值
print('数组的最小元素为：',np.argmin(arr))  #返回数组最小元素的索引
print('数组的最大元素为：',np.argmax(arr))  #返回数组最大元素的索引

arr = np.arange(2,10)
print('创建的数组为：', arr)
print('数组元素的累计和为：',np.cumsum(arr))  #计算所有元素的累计和
print('数组元素的累计积为：',np.cumprod(arr))  #计算所有元素的累计积










