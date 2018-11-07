import math
p = 499
q = 547
a = -57
b = 52
x_0 = 159201
m = '10011100000100001100'

n = p*q
k = math.floor(math.log2(n))
h = math.floor(math.log2(k))
t = len(m)//h
x_i = x_0

m_i = [m[i*h:i*h+h] for i in range(t)]
c_i = []

for i in range(t):
    x_i = (x_i**2)%n
    p_i = x_i%(2**h)
    c_i.append(p_i ^ int(m_i[i], 2))

c = ''.join(format(i, '04b') for i in c_i)
print(c, x_i)
