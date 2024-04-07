# completed
N = int(input())
for x in range(N):
    num = input()
    ans = 1
    for y in num:
        y = int(y)
        ans *= y
    print(ans)