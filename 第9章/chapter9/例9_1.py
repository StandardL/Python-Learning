#例9.1:读取csv文件
import pandas as pd
## 使用read_table读取订单信息表
order = pd.read_table('data/meal_order_info.csv',
      sep = ',', encoding = 'gbk')
print('使用read_table读取的订单信息表的长度为：',len(order))


## 使用read_csv读取订单信息表
order1 = pd.read_csv('data/meal_order_info.csv',
      encoding = 'gbk')
print('使用read_csv读取的订单信息表的长度为：',len(order1))

order2 = pd.read_table('data/meal_order_info.csv',
      sep = ';', encoding = 'gbk')
print(order2)

order3 = pd.read_csv('data/meal_order_info.csv',
      sep = ',', header= None, encoding = 'gbk')
print(order3)

order4 = pd.read_csv('data/meal_order_info.csv',
      sep = ',', encoding = 'utf-8')
print(order4)

