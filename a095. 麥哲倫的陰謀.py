# completed
while True:
    try:
        a,b=map(int,input().split())
        if a==b:
            print(b)
        else:
            print(b+1)
    except EOFError:
        break
