# completed
id = (list(map(int,list(input()))))
n = 1
total = 0
total += id[-1]
id.pop(-1)
id.reverse()
for id in id:
    r = int(id)*n
    total += r
    n += 1
c = (10 - total % 10) % 10
if c==0:
    print("BNZ")
if c==1:
    print("AMW")
if c==2:
    print("KLY")
if c==3:
    print("JVX")
if c==4:
    print("HU")
if c == 5:
    print("GT")
if c==6:
    print("FS")
if c==7:
    print("ER")
if c==8:
    print("DOQ")
if c==9:
    print("CIP")
