#bruteforce solution generate all subarrays

def bruteforce(a):
    n = len(a)
    subarrys = []
    mxsum = float('-inf')
    for i in range(n+1):
        for j in range(i+1,n+1):
            subarry = a[i:j]
            mxsum = max(mxsum,sum(subarry))
            #subarrys.append(subarry)
    #print(subarrys)
    print(mxsum)


def dp(a):
    

testcase = [-2,-3,4,-1,-2,1,5,-3]
bruteforce(testcase)
