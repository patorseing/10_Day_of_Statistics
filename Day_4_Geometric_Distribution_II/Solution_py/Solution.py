'''
Task
The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the first 5 inspections?
'''


def g(n, p):
    result = 0
    for i in range(1, n+1):
        result += ((1-p) ** (i-1)) * p
    return round(result, 3)


if __name__ == "__main__":
    numerator, denominator = list(map(int, input().strip().split()))
    n = int(input().strip())
    print(g(n, numerator/denominator))
