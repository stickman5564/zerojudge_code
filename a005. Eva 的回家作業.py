# completed
count = int(input())
for x in range(count):
    a,b,c,d = map(int,input().split())
    if d/c==c/b:
        print(a,b,c,d,int(d*d/c))
        continue
    if d-c==c-b:
        print(a,b,c,d,int(d+d-c))
        continue
