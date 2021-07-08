# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def factorial(x):
    return 1 if x == 0 else x*factorial(x-1)


def P(mean, k):
    return round(math.pow(mean, k) * math.exp(-mean)/factorial(k), 3)


if __name__ == "__main__":
    mean = float(input().strip())
    X = int(input().strip())
    print(P(mean, X))
