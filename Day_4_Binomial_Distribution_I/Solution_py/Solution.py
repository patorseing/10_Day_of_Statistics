# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(x):
    return 1 if x == 0 else x*factorial(x-1)


def BinomialDistribution(b, g, n=6, x=3):
    res = 0
    p = b/(b+g)
    q = 1 - p
    for i in range(x, n+1):
      res += factorial(n)/(factorial(i)*factorial(n-i)) * (p**i) * (q ** (n-i))
    return round(res,3)


if __name__ == "__main__":
    b, g = list(map(float, input().strip().split()))
    print(BinomialDistribution(b, g))
