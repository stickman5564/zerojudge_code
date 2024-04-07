# completed
while 1:
    try:
        input()
        list_0 = list(map(int,input().split()))
        list_0.sort(key=lambda x: (x % 10, -x // 10))
        list_0 = [str(i) for i in list_0]
        ans = " ".join(list_0)
        print(ans)
    except EOFError:
        break