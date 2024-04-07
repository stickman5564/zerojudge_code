# completed
a,op,b=input().split()
if op=='+':
    print(int(a)+int(b))
elif op=='-':
    print(int(a)-int(b))
elif op=='*':
    print(int(a)*int(b))
else:
    print(int(int(a)/int(b)))