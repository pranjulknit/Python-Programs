from math import *

def ispowerof2(n):
    #T.C = O(1)
    if n<=0:
        return False
    x=n
    y=not(n&(n-1))
    return x and y

def brutforce(n):
    s = str(bin(n))[2:]
    print("{}".format(s))
    return s.count('1')

def cntbits(n):
    cnt = 0
    while n:
        cnt+=1
        n = n&(n-1)
    return cnt

t = int(input())

while t:
    n = int(input())
    ispowerof2(n)
    brutforce(n)
    print("number of bits",cntbits(n))
    t = t-1

