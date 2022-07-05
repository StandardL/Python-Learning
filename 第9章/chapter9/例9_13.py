import pandas as pd
import numpy as np
detail = pd.read_excel('data/meal_order_detail.xlsx')

def DoubleSum(data):
      s = data.sum() * 2
      return s

print('菜品订单详情表的菜品销量两倍总和为：', '\n',
      detail.agg({'counts': DoubleSum}, axis=0))



