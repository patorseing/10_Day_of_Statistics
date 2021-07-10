import statistics
import math


def mean(X):
    return statistics.mean(X)


def sd(X, meanx):
    # return statistics.stdev(X)
    return round(math.sqrt((sum(list(map(lambda x: math.pow(x-meanx, 2), X)))) / (len(X))), 5)


def Cor(n, X, Y):
    meanx = mean(X)
    meany = mean(Y)

    stdx = sd(X, meanx)
    stdy = sd(Y, meany)

    res = 0
    for i in range(n):
        res += ((X[i] - meanx) * (Y[i] - meany))

    return round(res / (n * stdx * stdy), 3)


if __name__ == "__main__":
    n = int(input())
    X = list(map(float, input().strip().split()))
    Y = list(map(float, input().strip().split()))
    print(Cor(n, X, Y))
