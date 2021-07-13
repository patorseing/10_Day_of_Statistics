# import math
import statistics

# n = 5
# xy = [map(int, input().split()) for _ in range(n)]

xy = [
    [95, 85],
    [85, 95],
    [80, 70],
    [70, 65],
    [60, 70],
]

n = len(xy)

sx, sy, sx2, sxy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))

b = (n * sxy - sx * sy) / (n * sx2 - sx**2)

a = (sy / n) - b * (sx / n)

X = 80

Y = a + b *X

print(round(Y, 3))

# for i in map(sum,zip(*[(x, y, x**2, x * y) for x, y in xy])):
#   print(i)
