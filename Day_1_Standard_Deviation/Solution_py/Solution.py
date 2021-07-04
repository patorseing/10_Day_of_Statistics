#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def mean(arr):
  return sum(arr) / len(arr)

def EachMean(x, u):
  return (x-u) ** 2

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    u = mean(arr)
    sd = math.sqrt(sum(list(map(lambda x: EachMean(x, u), arr)))/len(arr))
    return round(sd, 1)

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    print(stdDev(vals))
