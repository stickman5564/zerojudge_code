n = int(input())
list = [0,0,0]
while n > 0:
    num = int(input())
    num %= 3
    list[num] += 1
    n -= 1
print(list[0],list[1],list[2])