"""
项目名称：实验一——基金定投计算
作者：林子皓
时间：2022/4/4
版本：v3.1
"""

import math


def whether_earn(f_e):
    if i == 0:
        if f_e[-1] > num_sum:  # 如果当期收益赚钱了
            earn_month.append(i+1)
    else:
        if f_e[-1] > f_e[-2]:  # 如果当期收益赚钱了
            earn_month.append(i+1)
    return


def invest_sum(summary):
    global num_new
    if fund_earn[-1] < -0.05 * summary:  # 投入的资金跌幅超过5%
        num_new = num * (1 + 0.25 * (fund_earn[-1] / summary)/0.05)  # 根据收益率计算本期投资额
    elif fund_earn[-1] > 0.05 * summary:  # 投入的资金涨幅超过5%
        num_new = num * (1 - 0.25 * (fund_earn[-1] / summary)/0.05)  # 根据收益率计算本期投资额
    else:
        num_new = num
    return num_new


net_value = []  # 每期基金净值列表
fund_share = []  # 每期基金份额列表
fund_earn = []  # 每期基金收益列表
earn_month = []  # 有正收益的月份
LIST = []  # 用于记录净值,总份额,本期份额,投资总额,本期投入,收益

num = int(input('请输入您每月基础定投的金额（单位：元）：'))
num_new = num  # 在基础定投金额上下浮动的每月投资额
num_sum = num_new  # 总共投入的资金
invest_month = int(input("请输入定投投资的月数："))
fund_share_sum = 0


for i in range(invest_month):
    net_value_f = 0.001 * pow(i - 17, 2) + 0.8599  # 当期净值
    net_value.append(net_value_f)
    fund_share.append(round(num_new / net_value_f, 2))  # 当期份额

    fund_share_sum = math.fsum(fund_share)  # 当期基金总份额
    ending_assets = fund_share_sum * net_value[-1]  # 当期资产

    fund_earn.append(round(ending_assets - num_sum, 2))  # 截至当期的收益

    whether_earn(fund_earn)

    LIST += [("第{}个月".format(i+1), round(net_value_f, 4), round(fund_share_sum, 2), round(fund_share[-1], 2), round(num_sum, 2), round(num_new, 2), fund_earn[-1])]
    # 将净值、份额、投入等放在同一个列表：[(净值,总份额,本期份额,投资总额,本期投入,收益)]

    num_sum += invest_sum(num_sum)  # 统计总投入资金

fund_share_sum = math.fsum(fund_share)  # 期末总基金份额
ending_assets = fund_share_sum * net_value[-1]  # 期末资产
earnings = ending_assets - num_sum  # 期末收益

print(LIST)

print('您定投月份为{}月，总投资{}元，投资的份额为{}'.format(invest_month, round(num_sum, 2), fund_share_sum))
print('您投资基金的当前净值为每份{:.2f}元，期末资产为{:.2f}元'.format(net_value[-1], ending_assets))
print('期末收益为{:.2f}元，收益率为{:.2f}%:'.format(earnings, earnings/(num * invest_month)*100))
if len(earn_month) == 0:
    print('您的基金目前是没有正收益')
elif earnings/(num * invest_month)*100 > 0:
    print('当您定投投资到第{}个月开始有正收益，此时基金的净值为每份{}元'.format(earn_month[0], net_value[earn_month[0]-1]))
else:
    print('当您定投投资到第{}个月开始有正收益，此时基金的净值为每份{}元，但随后存在亏损风险'.format(earn_month[0], net_value[earn_month[0]-1]))

