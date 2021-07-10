import math


def means(n, mean):
    return n * mean


def sds(n, sd):
    return math.sqrt(n) * sd


def cdf(x, n, mean, sd):
    u = means(n, mean)
    d = sds(n, sd)
    Z = (x-u)/d
    return round(0.5 * (1 + math.erf(Z/math.sqrt(2))), 4)


x = 9800
n = 49
mean = 205
sd = 15
print(cdf(x, n, mean, sd))
