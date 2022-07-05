import numpy as np

arr1 = np.arange(0, 1.0, 0.01)
arr2 = np.random.randn(100)
print('arr1 = \n', arr1)
print('arr2 = \n', arr2)
print('arr1 + arr2 = \n', arr1 + arr2)
print('arr1 - arr2 = \n', arr1 - arr2)
print('arr1 * arr2 = \n', arr1 * arr2)
print('arr1 / arr2 = \n', arr1 / arr2)
print('arr1的累计和为：\n', np.cumsum(arr1))
print('arr2的累计和为：\n', np.cumsum(arr2))
print('arr1的标准差：\n', np.std(arr1))
print('arr2的标准差：\n', np.std(arr2))
