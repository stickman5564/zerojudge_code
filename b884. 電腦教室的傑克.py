# completed
n=int(input())
for i in range(n):
    a = input().split()
    x,y=int(a[0]),int(a[1])
    r=(abs(x)+abs(y))**0.5
    yee=100-r*r
    if 0<yee<=30:
        print("sad!")
    elif 0<yee<=60:
        print("hmm~~")
    elif 60<yee<100:
        print("Happyyummy")
    else:
        print("evil!!")
