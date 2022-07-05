#例8.18：argsort函数和lexsort函数排序
import numpy as np  #导入NumPy库

arr = np.array([2,3,6,8,0,7])
print('创建的数组为：',arr)
print('排序后数组为：',arr.argsort())  #返回值为重新排序值的下标

a = np.array([3,2,6,4,5])
b = np.array([50,30,40,20,10])
c = np.array([400,300,600,100,200])
d = np.lexsort((a,b,c))  #lexsort函数只接受一个参数，即（a,b,c）
print(d)#返回的是按最后一个传入数据的从小到大的排序值的下标
#多个键值排序是按照最后一个传入数据计算的
print('排序后数组为：',list(zip(a[d],b[d],c[d])))













