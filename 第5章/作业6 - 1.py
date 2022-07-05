class Password:
    pw = 'None'  # 密码
    intensity = 0  # 密码强度等级
    digit = False
    alphas = False

    def __init__(self, p):
        self.pw = p

    def judge(self):
        if len(self.pw) >= 8:
            self.intensity = 1  # 符合最低要求的密码强度为1
        else:
            print('密码长度小于8个字符！')
            while len(self.pw) < 8:
                self.pw = input('请设置密码（至少8个字符）：')

        pw_list = list(self.pw)
        for i in range(len(pw_list)):
            pw_list[i] = ord(pw_list[i])

        for i in range(len(pw_list)):
            if pw_list[i] in range(48, 58):
                self.digit = True  # 字符串中含有数字
                print('密码中含有数字')
                break

        for i in range(len(pw_list)):
            if pw_list[i] in range(65, 91) or pw_list[i] in range(97, 123):
                self.alphas = True  # 字符串中含有字母
                print('密码中含有字母')
                break


p_in = input('请设置密码（至少8位，仅包含数字和字母）：')
p_w = Password(p_in)
p_w.judge()

