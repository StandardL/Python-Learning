L = [1, 2, 3, 4, 5]

# 法一：
i = 4
while i >= 0:
    print(L[i], end=' ')
    i = i - 1
print()

# 法二：
L_re = list(reversed(L))
for i in range(5):
    print(L_re[i], end=' ')
print()
