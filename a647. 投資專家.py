# completed
from sys import stdin
for line in stdin:
    try:
        m, p = map(int, line.split())
    except:
        continue
    r = (p - m) / m * 100
    if r < 0:
        r = r - 0.000001
    elif r > 0:
        r = r + 0.000001
    if r >= 10 or r <= -7:
        t = 'dispose'
    else:
        t = 'keep'
    print('{0:.2f}% {1}'.format(r,t))
