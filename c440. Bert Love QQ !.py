ans = 0
sumQ = leftQ = 0
string = input()
for i in string:
    if i == 'Q':
        sumQ += 1
        ans += leftQ
    elif i == 'A':
        leftQ += sumQ
print(ans)