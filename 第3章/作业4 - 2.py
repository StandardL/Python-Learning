str_in = input('输入小写的英文字母（不多于20个字母）：')

# 统计字母出现次数
lstr = list(str_in)
dic = {}
for e in lstr:
    if e not in dic:
        dic[e] = 1
    else:
        dic[e] += 1
dic_copy = dic.copy()
k0 = lstr[0]
mini = dic_copy.pop(k0)

# 找出现次数最少的字符
for value in dic.values():
    if value < mini:
        mini = value

lstr_select = lstr.copy()
for key, value in dic.items():
    if value == mini:
        lstr_select.remove(key)

# 输出
for i in range(len(lstr_select)):
    print(lstr_select[i], end='')
