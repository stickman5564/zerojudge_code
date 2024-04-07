# completed
while 1:
    ans = 0
    n = int(input())+1
    if n == 1:
        break
    while n % 2 ==0:
        n /= 2
        ans += 1
    print(ans)