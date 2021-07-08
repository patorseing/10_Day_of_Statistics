# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


'''
E[X**2] = mean + mean **2
'''
def C(X, mean):
    return round(X + 40 *(mean + math.pow(mean, 2)), 3)


if __name__ == "__main__":
    A, B = list(map(float, input().strip().split()))
    print(C(160, A))
    print(C(128, B))
