# completed
while 1:
    try:
        num = int(input())
        ans = 0
        for x in range(1,num):
            if num % x == 0:
                ans += x
        if ans > num:
            print("盈數")
        if ans == num:
            print("完全數")
        if ans < num:
            print("虧數")
    except EOFError:
        break