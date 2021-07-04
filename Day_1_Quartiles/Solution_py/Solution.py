#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findPosMed(N):
    return math.ceil(N/2)

def median(x):
    x = sorted(x)
    pos = findPosMed(len(x))
    med = x[pos-1]
    if len(x) % 2 == 0:
        med = (med + x[pos])/2
    return int(med)


def Quartile(arr, n):
    if n % 2 == 0:
        return median(arr)
    startpos = 0
    stoppos = math.floor(len(arr)/2)
    if n == 3:
        startpos = stoppos
        if len(arr) % 2 == 1:
            startpos += 1
        stoppos = len(arr)
    return median(arr[int(startpos): int(stoppos)])


def quartiles(arr):
    # Write your code here
    arr = sorted(arr)
    return [Quartile(arr, 1), Quartile(arr, 2), Quartile(arr, 3)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
