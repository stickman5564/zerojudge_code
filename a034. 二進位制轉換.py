# completed
while 1:
    try:
        num = int(input())
        num = bin(num)[2:]
        print(num)
    except EOFError:
        break
