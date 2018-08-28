import string
import random

wCount = 8 #文字数
wRows = 10 #行数

words = string.ascii_letters

#password生成
passwd = [''.join(random.choice(words) for i in range(wCount)) for x in range(wRows)]

#出力処理
print('------{}文字のパスワードを{}行を出力します。--------------'.format(wCount,wRows))
for password in passwd:
    print(password)
print('------------------------')