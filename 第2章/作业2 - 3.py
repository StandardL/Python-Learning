text = list(input())
re_text = list(reversed(text))
if list(text) == list(re_text):
    print('是回文字符串')
else:
    print('不是回文字符串')