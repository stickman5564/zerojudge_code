# completed
n = int(input())
list_0 = list(map(int, input().split()))
a = b = 0
for i in range(n):
    if list_0[i] > a:
        a = list_0[i]
    else:
        b = max(b, a - list_0[i])
print(b)
