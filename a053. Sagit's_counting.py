# completed
num = int(input())
if num > 40:
    print(100)
else:
    score = 0
    for x in range(1, 11):
        if num > 0:
            score += 6
            num -= 1
        else:
            break
    for x in range(11, 21):
        if num > 0:
            score += 2
            num -= 1
        else:
            break
    for x in range(21, 41):
        if num > 0:
            score += 1
            num -= 1
        else:
            break
    print(score)