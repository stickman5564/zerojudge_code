# completed
while 1:
    try:
        num=list(map(int,input().split()))
        a=num.pop(0)
        if sum(num) / a > 59:
            print("no")
        else:
            print("yes")
    except EOFError:
        break
