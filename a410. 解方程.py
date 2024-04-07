# completed
from sys import stdin
for line in stdin:
  try:
    a, b, c, d, e, f = map(int, line.split())
  except:
    continue
  if (a * e - d * b) != 0:
    x = str(round((c * e - f * b) / (a * e - d * b), 2))
    y = str(round((a * f - d * c) / (a * e - d * b), 2))
    if '.' in x:
      if len([i for i in x.split('.')][1]) == 1:
        x = x + '0'
    else:
      x = x + '.00'
    if '.' in y:
      if len([i for i in y.split('.')][1]) == 1:
        y = y + '0'
    else:
      y = y + '.00'

    print(f'x={x}')
    print(f'y={y}')
  else:
    if (c * e - f * b) == 0 and (a * f - d * c) == 0:
      print('Too many')
    else:
      print('No answer')