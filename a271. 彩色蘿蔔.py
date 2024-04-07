# completed
from sys import stdin
for line in stdin:
    a = int(line)
    for _ in range(a):
        x, y, z, w, n, m = map(int, stdin.readline().split())
        role = {'0': 0, '1': x, '2': y, '3': -z, '4': -w}
        if line == '':
            print('{}g'.format(m))
        else:
            days = stdin.readline().split()
            poison = 0
            for i in days:
                m -= poison * n
                if m <= 0:
                    break
                if i == '4':
                    poison += 1
                m += role[i]
                if m <= 0:
                    break
            if m <= 0:
                print('bye~Rabbit')
            else:
                print('{}g'.format(m))
