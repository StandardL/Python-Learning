'''
最后更新：2022/3/29
作者：林子皓
版本：1.2
内容：猜数字
'''
from random import randint


def guessNumber(maxValue=10, maxTime=3):
    # 随机生成一个整数
    value = randint(1, maxValue)

    for i in range(maxTime):
        # 记录次数
        print('这是第', i + 1, '次')

        # 输入数字
        a = eval(input('请输入一个1-10的整数：'))
        # 判断数字是否是maxValue范围内的正整数，否则重新输入
        while True:
            if not (0 < a < 10) or not isinstance(a, int):
                a = eval(input('请重新输入:'))
            else:
                break
        # 判断猜测是否正确，不正确提示太大或太小
        if a == value:
            print('恭喜你，猜对了！')
            break
        elif a < value:
            print('太小了！')
        else:
            print('太大了！')
    else:
        # 次数用完了还没有猜对就提示输了，正确值应该是
        print('拉了啊，次数都用完了啊。正确值是：', value)


guessNumber()
