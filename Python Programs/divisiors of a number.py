#divisors of a number o(sqrt(n))

from math import *

def fun1(n):
    div1 = []
    for i in range(1,n+1):
        if n%i == 0:
            div1.append(i)
    return div1

def fun2(n):
    div2 = set()
    for i in range(1,int(sqrt(n) + 1)):
        if n%i == 0:
            div2.add(i)
            div2.add(n//i)
    return list(div2)

print("No. of Test Cases")
t=int(input())
while t:
    n = int(input())
    ans1 = fun1(n)
    print(*ans1)
    ans2 = fun2(n)
    print(*ans2)
    t = t-1
 