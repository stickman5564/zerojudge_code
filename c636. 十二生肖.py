# completed
from sys import stdin
list_0 = ["鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬"]
for line in stdin:
    n = int(line) - 1
    print(list_0[n%12])