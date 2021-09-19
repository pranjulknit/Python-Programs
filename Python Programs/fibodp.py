#memoization -1d
#tabulation 2-d

GLOBALFIBDYNAMIC = [0,1]

def fib(n):
    if n<len(GLOBALFIBDYNAMIC):
        return GLOBALFIBDYNAMIC[n]
    else:
        for i in range(len(GLOBALFIBDYNAMIC),n+1):
            last = GLOBALFIBDYNAMIC[-1]
            secondlast = GLOBALFIBDYNAMIC[-2]
            GLOBALFIBDYNAMIC.append(last+secondlast)
        return GLOBALFIBDYNAMIC[n]


t = int(input())
for i in range(t):
    N = int(input())
    print(fib(N))