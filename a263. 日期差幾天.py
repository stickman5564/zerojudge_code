# completed
import datetime
while 1:
    try:
        td=list(map(int,input().split()))
        te=list(map(int,input().split()))
        t1=datetime.datetime(td[0], td[1], td[2])
        t2=datetime.datetime(te[0], te[1], te[2])
        print(abs((t2-t1).days))
    except EOFError:
        break
