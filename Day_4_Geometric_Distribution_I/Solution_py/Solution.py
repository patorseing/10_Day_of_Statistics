
def g(n, p):
    return round(((1-p) ** (n-1)) * p, 3)


if __name__ == "__main__":
    numerator, denominator = list(map(int, input().strip().split()))
    n = int(input().strip())
    print(g(n, numerator/denominator))
