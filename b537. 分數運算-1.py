# completed
from sys import stdin
from fractions import Fraction
def getK(n):
    if n == 1:
        return 1
    if n < 1:
        return getK(1/n)+1
    if n > 1:
        return getK(n-1)*2
for line in stdin:
    a,b = map(int,line.split())
    n = Fraction(a,b)
    print(getK(n))