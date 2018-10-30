
# Iterative Python 3 program to find 
# modular inverse using extended 
# Euclid algorithm 
  
# Returns modulo inverse of a with 
# respect to m using extended Euclid 
# Algorithm Assumption: a and m are 
# coprimes, i.e., gcd(a, m) = 1 
def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        # q is quotient 
        q = a // m 
        t = m 
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
        # Update x and y 
        y = x - q * y 
        x = t 
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
    return x 

def findM(P1, P2, E, n):
    if(P1 == P2):
        num = (3*P1[0]**2 + E[0]) % n
        den = (2*P1[1]) % n
    else:
        num = (P1[1] - P2[1]) % n
        den = (P1[0] - P2[0]) % n
    if den == 0:
        raise EnvironmentError
    den_i = modInverse(den, n)
    return num*den_i%n

def findXn(m, x1, x2, n):
    return (m**2 - x1 - x2) % n

def findYn(m, x1, y1, xn, n):
    return (m*(x1 - xn) - y1) % n

E = (1,6)
n = 11

G = [(8,3)]
for x in range(1, 12):
    m = findM(G[0],G[-1], E, 11)
    xn = findXn(m, G[0][0], G[-1][0], n)
    yn = findYn(m, G[0][0], G[0][1], xn, n)
    # print(m, xn, yn)
    G.append((xn,yn))
    print('%iG: (%i,%i)' % (x+1, xn, yn))

# P1 = (8,3)
# P2 = (5,2)
# m = findM(P1, P2, E, 11)
# xn = findXn(m, P1[0], P2[0], n)
# yn = findYn(m, P1[0], P1[1], xn, n)
# print('(%i,%i)' % (xn, yn))