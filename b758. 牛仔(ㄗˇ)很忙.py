# completed
from sys import stdin
x = y = 0
for line in stdin:
    try:
        x, y = map(int, line.split())
    except:
        continue
    h = x + 2
    m = y + 30
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
        h = str(h).rjust(2, "0")
        m = str(m).rjust(2, "0")
    print('{0}:{1}'.format(h, m))