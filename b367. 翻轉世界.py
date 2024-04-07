# completed
while 1:
    try:
        N = input()
        if N == "\r":
            continue
        N = int(N)
        for x in range(N):
            a = []
            b = []
            n, m = map(int, input().split())
            for y in range(n):
                list_0 = list(map(int, input().split()))
                a.append(list_0)
                b.insert(0, list_0[::-1])
            if b == a:
                print('go forward')
            else:
                print('keep defending')
    except EOFError:
        break
