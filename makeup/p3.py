import random
import math

def Miller_Rabin(n):
    k = 100
    if (n%2 == 0): 
        return False
    extracttwo = lambda x: 1+extracttwo(x/2) if x%2==0 else 0
    r = extracttwo(n-1)
    d = int((n-1)/2**r)
    for i in range(k):
        a = random.randint(2, n-1)
        x = a**d % n
        if x==1 or x == n-1:
            continue
        for j in range(r-1):
            x = x**2 % n
            if x==n-1:
                continue
        return False
    return True

def Pollard_Rho(n, g):
    x=2
    y=2
    d=1
    while(d==1):
        x = g(x,n)
        y = g(g(y,n),n)
        d = math.gcd(abs(x-y), n)
    if(d==n):
        return 1
    else:
        return d

g = lambda x,n: (x*2-1)%n
num = 520482
res = Miller_Rabin(num)
if(res):
    print(res, 'is prime')
else:
    print(res, 'is not prime')
    f = Pollard_Rho(num, g)
    print('Can be factored', f, '*', num//f, '=', num)
