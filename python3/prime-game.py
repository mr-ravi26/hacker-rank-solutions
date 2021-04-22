from math import floor, sqrt

def simpleSieve(limit, primes):
    mark = [False]*(limit+1)
 
    for i in range(2, limit+1):
        if not mark[i]:
            primes.append(i)
            for j in range(i, limit+1, i):
                mark[j] = True

def getPrimes(low, high):
    limit = floor(sqrt(high)) + 1
    primes = list()
    simpleSieve(limit, primes)
 
    n = high - low + 1

    mark = [False]*(n+1)

    retVal = []
 
    for i in range(len(primes)):
 
        loLim = floor(low/primes[i]) * primes[i]
        if loLim < low:
            loLim += primes[i]
        if loLim == primes[i]:
            loLim += primes[i]
 
        for j in range(loLim, high+1, primes[i]):
            mark[j-low] = True
 
    for i in range(low, high+1):
        if not mark[i-low]:
            retVal.append(i)

    return retVal

def main():

    testCase = int(input())

    while testCase > 0:

        LR = list(map(int,input().strip().split()))
        L = LR[0]
        R = LR[1]

        lst = getPrimes(L, R)

        n = len(lst)

        if n > 1:
            print(lst[n-1]-lst[0])

        elif n == 1:
            print(0)

        else:
            print(-1)

        testCase -=1

main()


