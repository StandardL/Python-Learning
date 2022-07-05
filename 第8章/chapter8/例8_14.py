#例8.14：二进制数据文件读写
import numpy as np  #导入NumPy库

#一个数组存储
arr = np.arange(100).reshape(10,10)  #创建一个数组
np.save("tmp/save_arr", arr)  #保存数组
print('保存的数组为：\n', arr)

# 多个数组存储
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.arange(0,1.0,0.1)
np.savez('tmp/savez_arr',first = arr1, second = arr2)
print('保存的数组1为：',arr1)
print('保存的数组2为：',arr2)

# 读取二进制文件
loaded_data = np.load("tmp/save_arr.npy")  #读取含有单个数组的文件
print('读取的数组为：\n',loaded_data)

loaded_data1 = np.load("tmp/savez_arr.npz")  #读取含有多个数组的文件
print('读取的数组1为：',loaded_data1['first'])
print('读取的数组2为：',loaded_data1['second'])












