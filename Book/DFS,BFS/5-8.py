def dfs(graph, v, visited):
    # add the node to visited
    visited[v] = True
    print(v, end=' ')
    # visit connected nodes recursively
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

dfs(graph, 1, visited)