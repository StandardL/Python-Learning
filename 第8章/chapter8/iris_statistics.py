#程序2：花萼长度数据分析
import numpy as np  #导入NumPy库

iris_sepal_length = np.loadtxt("data/iris_sepal_length.csv",
    delimiter=",")  #读取文件
print('花萼长度表为：',iris_sepal_length)

iris_sepal_length.sort()  #对数据进行排序
print('排序后的花萼长度表为：',iris_sepal_length)

#去除重复值
print('去重后的花萼长度表为：',np.unique(iris_sepal_length))

print('花萼长度表的总和为：',np.sum(iris_sepal_length))  #计算数组总和

#计算所有元素的累计和
print('花萼长度表的累计和为：',np.cumsum(iris_sepal_length))

print('花萼长度表的均值为：',np.mean(iris_sepal_length))  #计算数组均值

#计算数组标准差
print('花萼长度表的标准差为：',np.std(iris_sepal_length))

print('花萼长度表的方差为：',np.var(iris_sepal_length))  #计算数组方差
print('花萼长度表的最小值为：',np.min(iris_sepal_length))  #计算最小值
print('花萼长度表的最大值为：',np.max(iris_sepal_length))  #计算最大值













