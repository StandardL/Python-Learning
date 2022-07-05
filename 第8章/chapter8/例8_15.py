#例8.15：txt文件读写
import numpy as np  #导入NumPy库

arr = np.arange(0,12,0.5).reshape(4,-1)
print('创建的数组为：\n',arr)

#fmt ="%d"为指定保存为整数
np.savetxt("tmp/arr.txt", arr, fmt="%d", delimiter=",")
#读入的时候也需要指定逗号分隔
loaded_data = np.loadtxt("tmp/arr.txt", delimiter=",")
print('读取的数组为：\n',loaded_data)











