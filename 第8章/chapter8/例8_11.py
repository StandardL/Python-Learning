#例8.11：ufunc函数运算
import numpy as np  #导入NumPy库

#四则运算
x = np.array([1,2,3])
y = np.array([4,5,6])
print('数组相加结果为：', x + y)  #数组相加
print('数组相减结果为：', x - y)  #数组相减
print('数组相乘结果为：', x * y)  #数组相乘
print('数组相除结果为：', x / y)  #数组相除
print('数组幂运算结果为：', x ** y)  #数组幂运算

#比较运算
x = np.array([1,3,5])
y = np.array([2,3,4])
print('数组比较结果为：', x < y)
print('数组比较结果为：', x > y)
print('数组比较结果为：', x == y)
print('数组比较结果为：', x >= y)
print('数组比较结果为：', x <= y)
print('数组比较结果为：', x != y)

#逻辑运算
print('数组逻辑运算结果为：', np.all(x == y))  #np.all()表示逻辑and
print('数组逻辑运算结果为：', np.any(x == y))  #np.any()表示逻辑or














