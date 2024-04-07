# completed
while True:
    try:
        matrix = []
        ans = []
        row, column =map(int,input().split())
        for x in range(row):
            matrix_temp = input().split()
            matrix.append(matrix_temp)
        ans = list(zip(*matrix))
        for y in range(column):
            string = ""
            for x in range(row):
                if x != row-1:
                    string += ans[y][x] + " "
                else:
                    string += ans[y][x]
            print(string)
    except EOFError as e:
        break
