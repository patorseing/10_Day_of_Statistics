import math
# Enter your code here. Read input from STDIN. Print output to STDOUT


def N(mean, sd, x):
    return round((1/(sd * math.sqrt(2*math.pi)) * math.exp(-(math.pow(x-mean, 2)/(2*math.pow(sd, 2))))), 3)


def cdf(mean, sd, X):
    return 0.5 * (1 + math.erf((X-mean)/(sd*math.sqrt(2))))


if __name__ == "__main__":
    mean, sd = list(map(float, input().strip().split()))
    X = float(input().strip())
    lower, upper = list(map(float, input().strip().split()))
    print("{:.3f}".format(cdf(mean, sd, X)))
    print("{:.3f}".format(cdf(mean, sd, upper) - cdf(mean, sd, lower)))
