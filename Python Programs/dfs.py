from collections import defaultdict

def dfs(graph,start,visited,path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if visited[neighbour] == False:
            dfs(graph,neighbour,visited,path)

    return path



v,e = map(int,input().split())

graph = defaultdict(list)

for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)

path = []
start = 'A'
visited = defaultdict(bool)
traversed_path = dfs(graph,start,visited,path)
print(traversed_path)