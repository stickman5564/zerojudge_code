# completed
mini, maxi = map(int,input().split())
list = []
for x in range(mini, maxi):
    a_num = 0
    N = len(str(x))
    for y in str(x):
        a_num += int(y) ** N
    if a_num == x:
        list.append(str(a_num))
if list == []:
    print("none")
else:
    print(" ".join(list))
