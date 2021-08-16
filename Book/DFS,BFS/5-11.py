# Maze Runner

from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0, 0))
# def route (list, i, j) :
#     global result
#     if i < 0 or i >= N or j < 0 or j >= M :
#         return False
#     if i == N-1 and j == M-1 :
#         result += 1
#         return True
#     if graph[i][j] == 1:
#         graph[i][j] = 0
#         result += 1
#         if route(list, i+1, j) == True :
#             return True
#         elif route (list, i, j+1) == True :
#             return True
#         elif route (list, i-1, j) == True :
#             return True
#         elif route (list, i, j-1) == True :
#             return True
#         else :
#             return False
#      return False
#
# if route(graph, 0, 0) == True :
#     print(result)
# print(graph)
#
