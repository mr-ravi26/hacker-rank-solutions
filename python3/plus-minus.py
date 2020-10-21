#!/bin/python3
# Author Ravi B
# Date: 10/21/2020

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    pls = 0
    sub = 0
    eql = 0

    for i in range(len(arr)):
        if(arr[i] > 0):
            pls = pls + 1
        elif(arr[i]==0):
            eql = eql + 1
        else:
            sub = sub + 1
            
    print(pls/len(arr))
    print(sub/len(arr))
    print(eql/len(arr))
    


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
