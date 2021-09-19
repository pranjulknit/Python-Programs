# 2 steps staircase proble,
# you can take 1 step/2 step 
#in how many ways you can reach nth step

#base case
#0th step ** to take no step
#1 step you can take one step no. of ways = 1
#2 steps ** you can take either 1+1/ 2** no.o f ways = 2


# a kind of fibonacci problem
def countwaystwosteps(n):
    dp = [0]* (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i]= dp[i-1] + dp[i-2]

def countwaysthreesteps(n):
    dp = [0]*(n+1)
    dp[0]=1
    dp[1]=1
    dp[2]=2
    dp[3]=4
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]