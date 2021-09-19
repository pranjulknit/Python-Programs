#gcd and lcm 


def gcd(a,b):
    if a == 0:
        return b
    if(a>b):
        a,b = b,a
    return gcd(b%a,a)


def lcm(a,b):
    prod = a*b
    hcf = gcd(a,b)
    return prod // hcf


print("Number of TestCases")
t = int(input())
while t:
    print("Two numbers")
    n,m = map(int,input().split())
    print("gcd  = {} and lcm = {}".format(gcd(n,m),lcm(n,m)))
    t = t -1