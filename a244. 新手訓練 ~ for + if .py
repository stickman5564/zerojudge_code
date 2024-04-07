# completed
while 1:
    try:
        n=0
        string = filter(str.isalpha,input().lower())
        count = list(string)
        for x in count:
            if n > 1:
                break
            if count.count(x) % 2 != 0:
                n += 1
            count = [y for y in count if y != x]
        if n > 1:
            print("no...")
        else:
            print("yes !")
    except EOFError:
        break
