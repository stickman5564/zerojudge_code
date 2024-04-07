# completed
while 1:
    try:
        a, b, N = map(int, input().split())
        ans = (a * (10 ** N) // b)
        ans = str(ans)
        ans = ans.rjust(N,"0")
        x = N*-1
        if ans[:x] == "":
            print("0." + ans[x:])
        else:
            print(ans[:x] + "." + ans[x:])
    except EOFError:
        break