"""
最后更新：2022/4/2
作者：林子皓
版本：1.0
内容：骰子游戏
"""

from random import randint
import sys

d1 = 0
d2 = 0


def roll_dice():
    # 随机生成两个骰子
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)
    # 赋予全局变量
    global d1
    global d2
    # 记录两个骰子的值
    d1 = dice_1
    d2 = dice_2
    return


def display_dice(dice_1, dice_2):
    # 计算两次投骰子的和
    total = dice_1 + dice_2
    return total


roll_dice()
value = display_dice(d1, d2)
print('Player rolled ', d1, '+', d2, ' = ', value, sep='')

# win
if value == 7 or value == 11:
    print('Player wins')
    sys.exit(0)

# craps
elif value == 2 or value == 3 or value == 12:
    print('Player loses')
    sys.exit(0)

# point
else:
    point = value
    print('Point is', point)
    while True:
        roll_dice()
        value = display_dice(d1, d2)
        print('Player rolled ', d1, '+', d2, ' = ', value, sep='')
        if value == 7:
            print('Player loses')
            sys.exit(0)
        elif value == point:
            print('Player wins')
            sys.exit(0)


