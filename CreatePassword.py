def write_csv(list_pass):
    with open('password.csv','a',encoding="utf-8") as f:
        f.write(list_pass + '\n')

import string
import random

wCount = 8 #文字数
wRows = 10 #行数

words = string.ascii_letters #ascii_letters　→ a～z,A～Z

#password生成
passwd = [''.join(random.choice(words) for i in range(wCount)) for x in range(wRows)]

#出力処理
#print('------{}文字のパスワードを{}行を出力します。--------------'.format(wCount,wRows))
print('------{}文字のパスワードを{}行をCSV出力します。--------------'.format(wCount,wRows))
for password in passwd:
    write_csv(password)
#print('------------------------')
print('CSV出力が完了しました。')