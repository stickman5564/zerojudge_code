# completed
num=int(input())
total=(list(map(int,input().split())))
sum=0
for i in range(num):
    sum+=total[i]*(i+1)
print(sum)