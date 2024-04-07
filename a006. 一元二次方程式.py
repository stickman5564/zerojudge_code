# completed
import math
a,b,c = map(int,input().split())
i = b**2//1 - 4*a*c//1
if i == 0:
    root1 = str(round((b/2/a*(-1))))
    print('Two same roots x=' + root1)
elif i < 0:
    print('No real root')
elif i > 0:
    root1 = math.floor((b*(-1) + math.sqrt(b**2-4*a*c))/2/a)
    root2 = math.floor((b*(-1) - math.sqrt(b**2-4*a*c))/2/a)
    if root1 > root2:
        root1 = str(root1)
        root2 = str(root2)
        print('Two different roots x1=' + root1 + " , x2=" + root2)
    else:
        root1 = str(root1)
        root2 = str(root2)
        print('Two different roots x1=' + root2 + " , x2=" + root1)
