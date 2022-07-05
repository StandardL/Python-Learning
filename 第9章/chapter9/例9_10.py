import pandas as pd
order = pd.read_table('data/meal_order_info.csv',
      sep = ',',encoding = 'gbk')

order['lock_time'] = pd.to_datetime(order['lock_time'])

time1 = order['lock_time']+pd.Timedelta(days = 1)
print('lock_time在加上一天前前5行数据为：\n',order['lock_time'][:5])
print('lock_time在加上一天前前5行数据为：\n',time1[:5])

timeDelta = order['lock_time'] - pd.to_datetime('2016-8-1')
print('lock_time减去2016年8月1日0点0时0分后的数据：\n',
      timeDelta[:5])
print('lock_time减去time1后的数据类型为：',timeDelta.dtypes)
