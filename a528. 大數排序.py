# completed
while 1:
    try:
        list_1 = []
        n = int(input())
        for x in range(n):
            list_1.append(int(input()))
        list_1.sort()
        for y in range(len(list_1)):
            print(list_1[y])
    except EOFError:
        break
