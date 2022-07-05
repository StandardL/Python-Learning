type = input()
a = type.count('1')
if a == 0:
    print('字符串中没有1')
elif a % 2 == 0:
    print('字符串中有偶数个1')
elif a % 2 == 1:
    print('字符串中有奇数个1')