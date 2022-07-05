# 基于字典的通讯录
address_book = {"小明": {'tel': '001', 'add': "广州"}, "小红": {'tel': '002', 'add': "上海"},
                "小王": {'tel': '003', 'add': "北京"}}
while True:
    print('\n1：好友添加', '2：好友删除', '3：好友信息修改', '4：好友信息查询', '0：退出', sep='\n')
    op = input('请输入操作代码：')

    if not op.isdigit():
        print('输入错误！程序退出！')
        break

    op = eval(op)
    if op == 1:
        name = input('输入新好友姓名：')
        tel = input('输入新好友电话：')
        add = input('输入新好友地址：')
        cache = {name: {'tel': tel, 'add': add}}
        address_book.update(cache)
        print('操作成功！')

    elif op == 2:
        delete = input('输入要删除的好友姓名：')
        del address_book[delete]

    elif op == 3:
        name = input('输入要修改的好友姓名：')
        tel = input('输入修改的电话：')
        add = input('输入修改的地址：')
        cache = {name: {'tel': tel, 'add': add}}
        address_book.update(cache)

    elif op == 4:
        search = input('输入要查找的好友姓名：')
        if search in address_book:
            print('姓名：', search)
            for key, value in address_book[search].items():
                print(key, value)
        else:
            print('查无此人！')

    elif op == 0:
        break

print("再见")
