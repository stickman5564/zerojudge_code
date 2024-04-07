# completed
from itertools import accumulate
while 1:
  try:
    n, m = map(int, input().split())
    food = (list(map(int,input().split())))
    food_sum = [0] + list(accumulate(food))
    for i in range(m):
      a, b = map(int, input().split())
      print(food_sum[b] - food_sum[a-1])
  except EOFError:
    break