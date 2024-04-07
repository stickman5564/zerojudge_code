# completed
while 1:
    try:
        n = int(input())
        n = n ** 2 - n + 2
        print(n)
    except EOFError as e:
        break