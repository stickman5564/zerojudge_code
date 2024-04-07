# completed
code = list(map(ord,list(input())))
ans = []
for x in range(len(code)-1):
    ans.append(str(abs(code[x] - code[x+1])))
ans_string = "".join(ans)
print(ans_string)