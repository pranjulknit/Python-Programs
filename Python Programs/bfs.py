#uses queue
from collections import deque
from collections import defaultdict


def bfs(graph,start,visited,path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        tmpnode = queue.popleft()
        for neighbour in graph[tmpnode]:
            if visited[neighbour] == False:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path


v,e = map(int, input().split())
graph = defaultdict(list)
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)

path = []
start = 'A'
visited = defaultdict(bool)
traversed_path = bfs(graph,start,visited,path)
print(traversed_path)