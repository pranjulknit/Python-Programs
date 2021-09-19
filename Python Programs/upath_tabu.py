#unique Path

t = int(input())
for i in range(t):
    r,c = map(int,input().split())
    dp = [ [0]*c for i in range(r)]
    for i in range(r):
        for j in range(c):
            #move only in one direction either horizontally or vertically
            if i ==0 or j==0:
                dp[i][j] =1
            else:
                #i have a choice move down or right
                dp[i][j]= dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1])
