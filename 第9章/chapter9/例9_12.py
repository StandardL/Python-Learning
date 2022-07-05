import pandas as pd
import numpy as np
detail = pd.read_excel('data/meal_order_detail.xlsx', engine='openpyxl')

detailGroup = detail[['order_id','counts',
      'amounts']].groupby(by = 'order_id')
print('分组后的订单详情表为：',detailGroup)

print(detailGroup.mean().head())

print(detailGroup.std().head())

print(detailGroup.size().head())

print(detail[['counts', 'amounts']].agg([np.sum, np.mean]))

print(detail.agg({'counts': np.sum, "amounts": np.mean}))

print(detail.agg({"counts": np.sum, "amounts":[np.mean, np.sum]}))