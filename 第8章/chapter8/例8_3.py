#例8.3:自定义数据类型
import numpy as np  #导入NumPy库

#1:创建数据类型
df = np.dtype([("name", np.str_, 40), ("numitems", np.int64), ("price", np.float64)])
print('数据类型为：', df)

print('数据类型为：', df["name"])

print('数据类型为：', np.dtype(df["name"]))

#2:创建数组
itemz = np.array([("tomatoes", 42, 4.14), ("cabbages", 13, 1.72)], dtype=df)
print('自定义数据为：', itemz)








