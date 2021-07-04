# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import statistics


def convertInt(x):
    x = x.split()
    return list(map((lambda i: int(i)), x))


def mean(N, x):
    return sum(x)/N


def findPosMed(N):
    return math.ceil(N/2)


def median(N, x):
    x = sorted(x)
    pos = findPosMed(N)
    med = x[pos-1]
    if N % 2 == 0:
        med = (med + x[pos])/2
    return med
    # return statistics.median(x)


def mode(x):
    x = sorted(x)
    M = 0
    modelist = []
    for i in x:
        count = 0
        for j in x:
            if i == j:
                count += 1
        if M < count:
          M = count
          modelist = []
        modelist.append(i)
    return modelist[0]
    # return statistics.mode(x)


if __name__ == '__main__':
    N = int(input().strip())
    x = input().strip()
    x = convertInt(x)
    print(mean(N, x))
    print(median(N, x))
    print(mode(x))
