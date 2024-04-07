while 1:
    try:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        code = ""
        ans = ""
        for x in range(n):
            code += input()
        list_1 = list(map(int, input().split()))
        for y in list_1:
            ans += code[y-1]
        print(ans)
    except EOFError:
        break