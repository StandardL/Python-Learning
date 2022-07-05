from random import randrange
from random import randint
import json
file_name = r"D:\华师\Python\实验2\history_list.json"
# 预处理程序
json_text = {
 "user0": {
 "film10": 5,
 "film7": 2,
 "film3": 5,
 "film14": 4,
 "film2": 1
 },
 "user1": {
 "film2": 1,
 "film4": 4,
 "film9": 4,
 "film3": 2,
 "film7": 2,
 "film1": 5
 },
 "user2": {
 "film3": 5,
 "film1": 5,
 "film12": 3,
 "film5": 2,
 "film14": 5
 },
 "user3": {
 "film4": 2,
 "film11": 3,
 "film10": 5,
 "film7": 5,
 "film2": 5,
 "film12": 4
 },
 "user4": {
 "film7": 5,
 "film9": 2,
 "film13": 4,
 "film12": 4,
 "film5": 5,
 "film3": 1,
 "film8": 2
 }
}
with open(file_name, 'w') as f:
    json.dump(json_text, f)

# 添加一些新数据
user = {'user'+str(i): {'film'+str(randrange(1, 10)): randint(0, 11) for j in range(randrange(1, 6))}
        for i in range(5, 11)}


with open(file_name, 'r') as f:
    data = json.load(f)
    data.update(user)

with open(file_name, 'w') as f:
    json.dump(data, f)

x = randint(0, 10)
user_chosen = data['user'+str(x)]
# 查找与待测用户最相似的用户和 Ta 喜欢看的电影
# 和Ta喜欢看的电影：两个用户共同打分的电影最多，并且这些所有的共同电影打分差值的平方和最小
similarUser, films = \
    min(data.items(), key=lambda item: (-len(item[1].keys() & user.keys()),
                                        sum(((item[1].get(film) - user.get(film)) ** 2
                                             for film in user.keys() & item[1].keys()))))

print('know data'.center(80, '='))
for u, f in data.items():
    print(u, f, sep=':')
print('new user data'.center(80, '='))
for u, f in user.items():
    print(u, f, sep=':')
print('most similar user and his films：'.center(80, '='))
print(similarUser, films.keys(), sep=':')
print('recommend film'.center(80, '='))
print(max(films.keys()-user.keys(), key=lambda film: films[film]))

with open(r"D:\华师\Python\实验2\recommendmoive.txt", 'a+') as f:
    f.write(max(films.keys()-user.keys(), key=lambda film: films[film]))
    f.write('\n')
