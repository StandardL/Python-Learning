import pandas as pd
import numpy as np
detail = pd.read_excel('data/meal_order_detail.xlsx')

##自定义函数求两倍的和
def DoubleSum1(data):
    s = np.sum(data)*2
    return s
print('订单详情表的菜品销量两倍总和为：\n',
      detail.agg({'counts':DoubleSum1},axis = 0).head())

print('订单详情表的菜品销量与售价的和的两倍为：\n',
      detail[['counts','amounts']].agg(DoubleSum1))



