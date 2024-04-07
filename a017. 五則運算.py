import sys
def count(a, b, op):
    if (op == '+'):
        return a + b
    if (op == '-'):
        return a - b
    if (op == '*'):
        return a * b
    if (op == '/'):
        return a // b
    if (op == '%'):
        return a % b
    return -999
def calculate(expr):
    exprs = expr.split()
    opers = []
    nums = []
    prior = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '(': -1}
    for ele in exprs:
        if ele == '(':
            opers.append('(')
        elif ele == ')':
            while opers[-1] != '(':
                val2 = nums.pop();
                val1 = nums.pop();
                op = opers.pop()
                result = count(val1, val2, op)
                nums.append(result)
            opers.pop()
        elif (ele in ['+', '-', '*', '/', '%']):
            while (opers and prior[ele] <= prior[opers[-1]]):
                val2 = nums.pop();
                val1 = nums.pop();
                op = opers.pop()
                result = count(val1, val2, op)
                nums.append(result)
            opers.append(ele)
        else:
            nums.append(int(ele))
    while (opers):
        val2 = nums.pop();
        val1 = nums.pop();
        op = opers.pop()
        result = count(val1, val2, op)
        nums.append(result)
    return nums[-1]
for inp in sys.stdin:
    ans = calculate(inp)
    print(ans)
