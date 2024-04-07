import math
while 1:
    try:
        x1, y1, x2, y2 = map(int,input().split())
        a, b, c, d = ((x1 - x2) ** 2), (y2 - y1), (-2 * x1 * (y2 - y1)), (y1 * (x2 - x1) * (x2 - x1) + x1 * x1 * (y2 - y1))
        gcd = math.gcd(math.gcd(abs(a), abs(b)), math.gcd(abs(c), abs(d)))
        a = a // gcd
        b = b // gcd
        c = c // gcd
        d = d // gcd
        ans = "{0}y = {1}x^2 + {2}x + {3}".format(a, b, c, d)
        print(ans)
    except EOFError:
        break
