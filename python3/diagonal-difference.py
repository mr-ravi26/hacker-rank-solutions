#!/bin/python3
#Author: Ravi B Tripathi
#Date: 10/21/2020

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    first = 0
    second = 0
    length = len(arr[0])

    for count in range(length):
        first = first + arr[count][count]
        second = second + arr[count][(length - count - 1)]

    return abs(first - second)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
