# completed
while 1:
    try:
        n = int(input())
        print(n*(n+1)//2,(n*(n+1)*(2*n+1)//6+n*(n+1)//2)//2)
    except EOFError:
        break