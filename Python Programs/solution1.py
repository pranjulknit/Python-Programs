#sum of n numbers

def sum1(n):     #o(1) complexicity
    return n*(n+1) //2


def sum2(n):    #o(n) complexicity
    s = 0
    for i in range(1,n+1):
        s = s+i
    return s

t = int(input())
while t:
    n = int(input())
    print("sum1 executed output {}".format(sum1(n)))
    print("sum2 executed output {}".format(sum2(n)))