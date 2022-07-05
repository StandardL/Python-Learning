#程序1：求100个点，任意两点间的距离
import numpy as np  #导入NumPy库

n = 100
dist = np.zeros([n, n])
point = np.random.rand(n,2)
print(point)


for i in range(n):
    for j in range(n):
        dist[i, j] = np.sqrt(sum((point[i, :] - point[j, :])**2))

print(dist)













