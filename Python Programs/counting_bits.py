'''
for  i=0 to n
return a list of number of one's in bianry representation of i
'''

def approach1(n):
    res = []
    for i in range(n+1):
        binary = bin(i)[2:]
        res.append(binary.count('1'))
    return res

def cntone(x):
    cnt = 0
    while x:
        cnt+=1
        x = x&(x-1)
    return cnt

# T>C = O(NlogN)
def approach2(n):
    res = []
    for i in range(n+1):
        res.append(cntone(i))
    return res

def approach3(n):
    res = []
    res = [0]
    for  i in range(1,n+1):
        res.append(res[i//2] + i%2)
    return res

N = 5
print(approach1(N))
print(approach2(N))
print(approach3(N))

