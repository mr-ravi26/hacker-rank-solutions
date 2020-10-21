#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):

    tip_a=0
    trip_b=0
	
    for i in range(3):
        if(a[i] > b[i]):
            tip_a = tip_a + 1
			
        elif(a[i] < b[i]):
            trip_b = trip_b + 1
			
    return (tip_a, trip_b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
