# completed
import itertools
while 1:
    try:
        n = int(input())
        a = [str(i) for i in range(1, n+1)]
        a = a[::-1]
        p = itertools.permutations(a)
        for i in p:
            print("".join(i))
    except:
        break
