# completed
num = int(input())
list = []
ans = ""
for x in range(2,num+1):
    count = 0
    if num < x:
        break
    if num % x != 0:
        continue
    while num % x == 0:
        count += 1
        num = num / x
    if count == 1:
        list.append(str(x))
    else:
        list.append(str(x)+"^"+str(count))
for x in range(len(list)-1):
    ans += list[x] + " * "
ans += list[-1]
print(ans)