# completed
while 1:
    try:
        a,b = map(int,input().split())
        n = 1
        while n*a + (n**2-n) / 2 <= b:
            n += 1
        print(n)
    except EOFError:
        break
