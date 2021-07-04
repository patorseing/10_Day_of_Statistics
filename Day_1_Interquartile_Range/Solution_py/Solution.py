#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#


def Seq(values, freqs):
    arr = []
    for i in range(len(freqs)):
        for _ in range(freqs[i]):
            arr.append(values[i])
    return sorted(arr)


def findPosMed(N):
    return math.ceil(N/2)


def median(x):
    x = sorted(x)
    pos = findPosMed(len(x))
    med = x[pos-1]
    if len(x) % 2 == 0:
        med = (med + x[pos])/2
    return med


def Quartile(arr, n):
    if n % 2 == 0:
        return median(arr)
    startpos = 0
    stoppos = len(arr)/2
    stoppos = math.floor(stoppos)
    if n == 3:
        startpos = stoppos
        if len(arr) % 2 == 1:
            startpos += 1
        stoppos = len(arr)
    return median(arr[int(startpos): int(stoppos)])


def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = Seq(values, freqs)
    return "{:.1f}".format(Quartile(arr,3) - Quartile(arr,1))


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    print(interQuartile(val, freq))
