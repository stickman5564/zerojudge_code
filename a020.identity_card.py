# completed
dict = {
    'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14',
    'F': '15', 'G': '16', 'H': '17', 'I': '34', 'J': '18',
    'K': '19', 'L': '20', 'M': '21', 'N': '22', 'O': '35',
    'P': '23', 'Q': '24', 'R': '25', 'S': '26', 'T': '27',
    'U': '28', 'V': '29', 'W': '32', 'X': '30', 'Y': '31',
    'Z': '33'}
multiply = [8, 7, 6, 5, 4, 3, 2, 1, 1]
num = 0
id = list(input())
abc = int(dict[id.pop(0)])
id = list(map(int,id))
abc= ( abc - ( abc % 10 ) ) / 10 + ( abc % 10 * 9 )
for x in range(9):
    num +=id[x]*multiply[x]
num+=abc
if num%10==0:
    print("real")
else:
    print("fake")