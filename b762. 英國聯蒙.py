# completed
kill_streak = 0
kill_count = 0
assist_count = 0
death_count = 0
n = int(input())
for x in range(n):
    m = input().replace(" ","")
    if m == "Get_Kill":
        kill_streak += 1
        kill_count +=1
        if kill_streak < 3:
            print("You have slain an enemie.")
        if kill_streak == 3:
            print("KILLING SPREE!")
        if kill_streak == 4:
            print("RAMPAGE~")
        if kill_streak == 5:
            print("UNSTOPPABLE!")
        if kill_streak == 6:
            print("DOMINATING!")
        if kill_streak == 7:
            print("GUALIKE!")
        if kill_streak > 7:
            print("LEGENDARY!")
    if m == "Get_Assist":
        assist_count += 1
    if m == "Die":
        death_count += 1
        if kill_streak < 3:
            print("You have been slained.")
        elif kill_streak >= 3:
            print("SHUTDOWN.")
        kill_streak = 0
print(str(kill_count)+"/"+str(death_count)+"/"+str(assist_count))