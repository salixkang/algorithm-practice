# find the city

from collections import deque

n, m, k, x = map(int, input().split())

edge = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)

dist = [-1] * (n + 1)

dist[x] = 0

queue = deque()

for i in edge[x]:
    queue.append((i, 1))

while queue:
    now = queue.popleft()
    if dist[now[0]] == -1 :
        dist[now[0]] = now[1]
        for i in edge[now[0]]:
            queue.append((i, now[1] + 1))

result = []

for i in range(len(dist)):
    if dist[i] == k:
        result.append(i)

if result :
    result.sort()
    for i in result:
        print(i)
else:
    print('-1')

# from collections import deque
#
# n, m, k, x = map(int, input().split())
#
# edge = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     edge[a].append(b)
#
# dist = [-1] * (n + 1)
#
# dist[x] = 0
#
# queue = deque([x])
#
# while queue:
#     now = queue.popleft()
#     for next_node in edge[now]:
#         if dist[next_node] == -1:
#             dist[next_node] = dist[now] + 1
#             q.append([next_node])
#
# check = False
#
# for i in range(len(dist)):
#     if dist[i] == k:
#         print(i)
#         check = True
#
# if not check:
#     print('-1')