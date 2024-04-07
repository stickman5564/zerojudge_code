from sys import stdin


def isPrime(n):
    '''
    參考 http://www.csie.ntnu.edu.tw/~u91029/Prime.html
    質數判定
    '''
    if (n == 1): return 0
    # 傳進來的 n 都已經過濾過，底下這 3 行先 mark 起來
    # if(n in (2, 3)): return 1
    # if(n % 2 == 0): return 0
    # if(n%6 not in [1,5]): return 0
    u = n - 1
    t = 0
    while (u % 2 == 0):
        u >>= 1
        t += 1
    sprp = [2, 7, 61]
    for sk in sprp:
        a = sk % n
        if (a == 0 or a == 1 or a == n - 1): continue
        x = pow(a, u, n)
        if (x == 1 or x == n - 1): continue
        for i in range(t - 1):
            x = pow(x, 2, n)
            if (x == 1): return 0
            if (x == n - 1): break
        if (x != n - 1): return 0
    return 1


for s in stdin:
    a, b = map(int, s.split())
    r = 0
    k = a // 6
    v = 1
    while (v):
        for n in (k * 6 + 1, k * 6 + 5):
            # 為了節省時間，只檢測 6p+1, 6p-1
            # 其實除了 5 以外， 5 的倍數也不必測
            if (n < a): continue
            if (n > b):  # 超過上界
                v = 0
                break
            r += isPrime(n)
        k += 1
    if (a <= 2 and b >= 2): r += 1
    if (a <= 3 and b >= 3): r += 1
    # 上面的檢測會遺漏 2, 3 在這裡補
    print(r)