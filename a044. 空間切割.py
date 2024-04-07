# completed
while 1:
    try:
        num = int(input())
        num = (num * num * num + 5 * num + 6) / 6
        print(int(num))
    except EOFError:
        break
