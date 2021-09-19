#sieve of eratosthenes
from math import *

def genprimes(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for pr in range(2,int(sqrt(n)+1)):
        if(primes[pr] == True):
            for i in range(pr*pr,n+1,pr):
                primes[i] = False

    for i in range(0,len(primes)):
        if primes[i] == True:
            print(i,end=" ")



t= int(input())
while t:
    n = int(input())
    genprimes(n)
    t = t-1
