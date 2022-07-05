from random import randrange
from random import randint
# 模拟已有历史数据，{用户名:{喜欢的电影名单: 打分}}
data = {'user'+str(i): {'film'+str(randrange(1, 10)): randint(0, 11) for j in range(randrange(15))} for
        i in range(10)}
# 某用户（随机产生）曾经看过并感觉不错的电影
user = {'film'+str(randrange(1, 10)): randint(0, 11) for i in range(randrange(1, 6))}
# 查找与待测用户最相似的用户和 Ta 喜欢看的电影
# 和Ta喜欢看的电影：两个用户共同打分的电影最多，并且这些所有的共同电影打分差值的平方和最小
similarUser, films = \
    min(data.items(), key=lambda item: (-len(item[1].keys() & user),
                                        sum(((item[1].get(film) - user.get(film)) ** 2
                                             for film in user.keys() & item[1].keys()))))
print('know data'.center(80, '='))
for u, f in data.items():
    print(u, f, sep=':')
print('current user'.center(80, '='))
print(user)
print('most similar user and his films：'.center(80, '='))
print(similarUser, films.keys(), sep=':')
print('recommend film'.center(80, '='))
print(films.keys()-user.keys())
