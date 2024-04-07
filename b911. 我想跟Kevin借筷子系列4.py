import math
while 1:
    try:
        n = int(input())
        ans=math.floor(math.log2(n)+1)
        print(ans)
    except EOFError:
        break
