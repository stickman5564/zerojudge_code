# completed
list = []
while 1:
    try:
        action = input()
        if action == "2":
            list.sort()
            print(list.pop(-1))
        elif action == "3":
            list.sort()
            print(list.pop(0))
        elif "1 " in action:
            a, b = action.split()
            b = int(b)
            list.insert(0,b)
    except EOFError:
        break
