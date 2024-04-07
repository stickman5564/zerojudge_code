# completed
from sys import stdin
for line in stdin:
    num = int(line.strip())
    ans = 0
    n = 6
    while num % 2 == 0:
        ans += 2
        num /= 2
    while num % 3 == 0:
        ans += 3
        num /= 3
    while n*n <= num:
        while num % (n-1) == 0:
            ans += n-1
            num = num // (n - 1)
        while num % (n + 1) == 0:
            ans += n+1
            num = num // (n + 1)
        n += 6
    if num > 1:
        ans += num
    print(int(ans))
