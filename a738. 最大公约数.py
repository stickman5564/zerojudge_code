# completed
import math
from sys import stdin
for line in stdin:
    try:
        a, b = map(int,line.split())
    except:
        continue
    print(math.gcd(a,b))