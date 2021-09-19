# n convert it into binary

def intToBin(n):
    return str(bin(n)[2:])

def binToInt(s):
    return int(s,2)      #base2

def kthbit(n,k):
    if(n & (1<< (k-1))):
        print("Set")
    else:
        print("Not set")


def finding_occur(arr):
    res = arr[0]
    for i in range(1,len(arr)):
        res =  res ^ arr[i]
    return res


t = int(input())
while t:
    n,k = map(int,input().split())
    binstring = intToBin(n)
    integer = binToInt(binstring)
    print(n,binstring,integer)
    kthbit(n,k)
    print("finding single element")
    arr = list(map(int,input().split()))
    print(finding_occur(arr))
    t = t-1