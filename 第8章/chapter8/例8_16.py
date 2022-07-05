#例8.16：txt文件读写
import numpy as np  #导入NumPy库

x, errx, y, erry = np.genfromtxt('data/arr.txt', dtype=float, unpack=True, skip_header=1, usecols=(1, 2, 3))

print(x)
print(errx)
print(y)
print(erry)












