num = list(input())
num.reverse()
ans = ""
while len(num) > 1 and num[0] == "0":
    num.remove("0")
for x in num:
    ans += x
print(ans)
