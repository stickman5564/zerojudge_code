# completed
roman2int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
int2roman = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
             20: "XX", 30: "XXX", 40:"XL", 50:"L", 60: "LX" , 70: "LXX", 80: "LXXX", 90: "XC", 100: "C",
            200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM", 1000: "M",
             2000: "MM", 3000: "MMM", 4000: "MMMM"}
line = input()
num1 = 0
num2 = 0
while line != "#":
    num1_list, num2_list = line.split()
    num1_list = list(num1_list)
    num2_list = list(num2_list)
    for x in range(len(num1_list)):
        num1_list[x] = roman2int[num1_list[x]]
    for x in range(len(num2_list)):
        num2_list[x] = roman2int[num2_list[x]]
    while len(num1_list) > 1:
        if num1_list[0] >= num1_list[1]:
            num1 += num1_list[0]
        else:
            num1 -= num1_list[0]
        del num1_list[0]
    num1 += num1_list[0]
    while len(num2_list) > 1:
        if num2_list[0] >= num2_list[1]:
            num2 += num2_list[0]
        else:
            num2 -= num2_list[0]
        del num2_list[0]
    num2 += num2_list[0]
    ans = abs(num1 - num2)
    # convert integer to roman numbers
    if ans == 0:
        print("ZERO")
    else:
        a = ans - ans % 1000
        b = (ans - a) - ans % 100
        c = (ans - a - b) - ans % 10
        d = ans % 10
        a = int2roman[a]
        b = int2roman[b]
        c = int2roman[c]
        d = int2roman[d]
        print(a + b + c + d)
    num1 = 0
    num2 = 0
    line = input()
