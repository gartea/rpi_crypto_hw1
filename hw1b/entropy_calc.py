import math

K = [1/2, 1/4, 1/4]
P = [1/3, 1/6, 1/2]
C = [7/24, 5/12, 1/8, 1/6]

KPC = [K, P, C]
Hs = []

for x in KPC:
    Hs.append(0)
    for y in x:
        Hs[-1] += y*math.log(y,2)

print(Hs)