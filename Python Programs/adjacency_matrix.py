#adjacency matrix
def printmatrix(matrix):
    r,c = len(matrix),len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end = " ")


v,e = map(int,input().split())
matrix = [[0]*v for i in range(v)]
'''
for i in range(e):
    u,v = map(str,input().split())
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    matrix[u][v] = True
'''

for i in range(e):
    u,v,w = map(str,input().split())
    u = ord(u) - ord('A')
    v =  ord(v) - ord('A')
    w = int(w)
    matrix[u][v] = w
    

printmatrix(matrix)
