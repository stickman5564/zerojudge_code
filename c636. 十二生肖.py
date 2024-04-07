# completed
from sys import stdin
list_0 = ["鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬"]
list_1 = list_0[::-1]
for line in stdin:
    n = int(line)
    if n >=0:
        n = (n - 1) % 12
        print(list_0[n])
    else:
        n = (abs(n) - 1) % 12
        print(list_1[n])
