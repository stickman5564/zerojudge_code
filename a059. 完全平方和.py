# completed
count = int(input())
for x in range(count):
    ans = 0
    string_ans = ""
    a = int(input())
    b = int(input())
    for y in range(1,32):
        if a <= y*y <= b:
           ans += y*y
    string_ans = "Case {0}: {1}".format((x+1),ans)
    print(string_ans)
