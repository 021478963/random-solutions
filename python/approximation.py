import gmpy2
from gmpy2 import mpfr, sqrt
import math

gmpy2.get_context().precision = 999

def Liu_Hui(n):
    return float(3 * 2 ** n * sqrt(2 - Liu_Helper(n)))

def Liu_Helper(n):
    if n == 0:
        return mpfr(1)
    else:
        return mpfr(sqrt(2 + Liu_Helper(n - 1)))

def Madhava(n):
    result = 0
    for i in range(n + 1):
        result += (-(1 / 3)) ** i / (2 * i + 1)
    return float(sqrt(12) * result)


def Newton(n):
    return mpfr(2 * Newton_Helper(1, n + 1))

def Newton_Helper(n, final):
    if final == 0:
        return mpfr(1)
    elif n == final:
        return mpfr(1)
    else:
        return mpfr(1 + (n / (2 * n + 1) * Newton_Helper(n + 1, final)))

def approximation(n):
    for i in range(30):
        print(Liu_Hui(i))

    bestName = "Liu Hui"
    best = Liu_Hui(n)
    madhava = Madhava(n)
    newton = Newton(n)
    print(best, madhava, newton)
    if abs(math.pi - best) > abs(math.pi - madhava):
        best = madhava
        bestName = "Madhava"
    if abs(math.pi - best) > abs(math.pi - newton):
        best = newton
        bestName = "Newton-Euler"
    return [best, bestName]

if __name__ == "__main__":
    print(approximation(2))
    #print(approximation(2))
    #print(approximation(900))