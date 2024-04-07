# completed
while 1:
    lis = []
    num = int(input())
    if num == 0:
        break
    for x in range(num):
        if x % 7 != 0:
            lis.append(x)
    lis = list(map(str,lis))
    ans =" ".join(lis)
    print(ans)