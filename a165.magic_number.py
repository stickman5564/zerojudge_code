# completed
from itertools import permutations
import math
for x in permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
    num = ""
    for y in x:
        num += y
    num = int(num)
    if math.floor(num / 10000000) % 2 == 0:
        if math.floor(num / 1000000) % 3 == 0:
            if math.floor(num / 100000) % 4 == 0:
                if math.floor(num / 10000) % 5 == 0:
                    if math.floor(num / 1000) % 6 == 0:
                        if math.floor(num / 100) % 7 == 0:
                            if math.floor(num / 10) % 8 == 0:
                                if num % 9 == 0:
                                    print(num)
                                    break