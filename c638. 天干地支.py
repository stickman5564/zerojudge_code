# completed
from sys import stdin
sky = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
earth = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']

for line in stdin:
    line = int(line)
    line -= 1800
    print(sky[line%10-4]+earth[line%12-4])