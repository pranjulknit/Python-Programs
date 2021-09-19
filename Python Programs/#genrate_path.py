#generate all paths in matrix
#dfs/recursively
#current index -> matrix[i][j]
#first check if the resent index is valid
#check if the current index can be explored
#move right,down,diagonal
#else backtrack


def findpaths(m,path,i,j):
    r,c = len(m),len(m[0])
    #if destination is reached
    #print
    if i == r-1 and j == c-1:
        print(path+[m[i][j]])
        return
    #explore
    path.append(m[i][j])

    #move down
    if(0<=i<=r-1 and 0<=j+1<=c-1):
        findpaths(m,path,i,j+1)
    #move diagonal
    if(0<=i+1 <= r-1 and 0<=j+1<=c-1):
        findpaths(m,path,i+1,j+1)
    #if none of the above is explorable or invalid
    #backtrack
    path.pop()



mat = []

n = int(input())
for i in range(n):
    row = list(map(int,input().split()))
    mat.append(row)

path = []
findpaths(mat,path,0,0)
