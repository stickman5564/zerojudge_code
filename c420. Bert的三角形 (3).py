# completed
n = int(input())
width = n
for x in range(0,n*2,2):
    print('{:^{width}}'.format("*"*(x+1),width=n*2-1).replace(" ","_"))