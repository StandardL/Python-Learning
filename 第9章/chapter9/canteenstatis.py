#程序1：餐饮数据统计分析
import pandas as pd

detail = pd.read_excel('data/meal_order_detail.xlsx', engine='openpyxl')
order = pd.read_table('data/meal_order_info.csv',
      sep = ',',encoding = 'gbk')
user = pd.read_excel('data/users_info.xlsx', engine='openpyxl')

#查看餐饮数据基本信息
print('订单详情表的维度为：', detail.ndim)
print('订单信息表的维度为：', order.ndim)
print('客户信息表的维度为：', user.ndim)

print('订单详情表的形状为：', detail.shape)
print('订单信息表的形状为：', order.shape)
print('客户信息表的形状为：', user.shape)

print('订单详情表的元素个数为：', detail.size)
print('订单信息表的元素个数为：', order.size)
print('客户信息表的元素个数为：', user.size)

#餐饮菜品销量的描述性统计
print('订单详情表counts和amounts两列的描述性统计为：\n',
      detail.loc[:, ['counts','amounts']].describe())
print(detail['order_id'].dtype)
detail['order_id'] = detail['order_id'].astype('category')
detail['dishes_name'] = detail['dishes_name'].astype('category')
print('''订单信息表order_id(订单编号)与dishes_name(菜品名称)
的描述性统计结果为：''', '\n',
detail[['order_id','dishes_name']].describe())

#剔除全为空值或者所有元素取值相同的列
## 定义一个函数去除全为空值的列和标准差为0的列
def dropNullStd(data):
    beforelen = data.shape[1]
    colisNull = data.describe().loc['count'] == 0
    print(colisNull)


    for i in range(len(colisNull)):
        if colisNull[i]:
            data.drop(colisNull.index[i],axis = 1,inplace =True)

    stdisZero = data.describe().loc['std'] == 0
    for i in range(len(stdisZero)):
        if stdisZero[i]:
            data.drop(stdisZero.index[i],axis = 1,inplace =True)
    afterlen = data.shape[1]
    print('去除的列的数目为：',beforelen-afterlen)
    print('去除后数据的形状为：',data.shape)

##使用dropNullStd函数对订单详情表操作
dropNullStd(detail)

##使用dropNullStd函数对订单信息表操作
dropNullStd(order)

##使用dropNullStd函数对客户信息表操作
dropNullStd(user)