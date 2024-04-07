# completed
while 1:
    try:
        n = int(input())
        list_1 = sorted(list(map(int,input().split())))
        list_1 = list(map(str, list_1))
        ans = " ".join(list_1)
        print(ans)
    except EOFError:
        break
