"""
最后更新：2022/3/29
作者：林子皓
版本：2.0
内容：嵌套函数
"""


def var(*nums):  # 求方差
    n = len(nums)

    def mean():  # 求均值的平方

        def sum() -> float:  # 求传入的数字和
            s = 0.0
            for i in range(n):
                s += nums[i]
            return s
        s1 = sum()
        m = (s1/n) * (s1/n)
        return m
    M = mean()

    def sums():
        s = 0.0
        for i in range(n):
            s += nums[i] * nums[i]
        return s

    S2 = sums()
    S = S2/n - M
    return S


a = var(1, 2, 3, 4, 5, 6)
a= round(a, 4)
print(a)
