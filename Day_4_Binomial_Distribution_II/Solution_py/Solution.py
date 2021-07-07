'''
Task
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:
case 1: No more than 2 rejects?
case 2: At least 2 rejects?
'''
def factorial(x):
    return 1 if x == 0 else x*factorial(x-1)


def BinomialDistribution(p, n, start, end):
    res = 0
    p /= 100
    q = 1 - p
    for i in range(start, end):
      res += factorial(n)/(factorial(i)*factorial(n-i)) * (p**i) * (q ** (n-i))
    return round(res,3)

if __name__ == "__main__":
    p, n = list(map(int, input().strip().split()))
    print(BinomialDistribution(p, n, 0, 3))
    print(BinomialDistribution(p, n, 2, n+1))

