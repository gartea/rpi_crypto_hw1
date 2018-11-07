import math
p = 499
q = 547
a = -57
b = 52
c = '00100000110011100100'
y = 40632

n = p*q
k = math.floor(math.log2(n))
h = math.floor(math.log2(k))
t = len(c)//h

rp = pow(y, ((p+1)//4)**t, p)
rq = pow(y, ((q+1)//4)**t, q)
x_0 = (q*b*rp + p*a*rq)%n
print(x_0)

c_i = [c[i*h:i*h+h] for i in range(t)]
m_i = []
x_i = x_0
for i in range(t):
    x_i = (x_i**2)%n
    p_i = x_i%(2**h)
    m_i.append(p_i ^ int(c_i[i], 2))
m = ''.join(format(i, '04b') for i in m_i)
print(m)