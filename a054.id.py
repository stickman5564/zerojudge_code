# completed
identity=int(input())
i=1
g=identity%10
identity=identity//10
while(i<9):
    k=identity%10*i
    identity=identity//10
    g=g+k
    i=i+1
c=(10-g%10)%10
if c==0:
    print("BNZ")
elif c==1:
    print("AMW")
elif c==2:
    print("KLY")
elif c==3:
    print("JVX")
elif c==4:
    print("HU")
elif c == 5:
    print("GT")
elif c==6:
    print("FS")
elif c==7:
    print("ER")
elif c==8:
    print("DOQ")
elif c==9:
    print("CIP")