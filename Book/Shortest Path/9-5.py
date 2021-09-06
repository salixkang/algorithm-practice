# message transmission

import heapq

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

distance = [INF] * (n + 1)
start = c

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_time = 0
for i in range(1, n + 1):
    if distance[i] != INF and distance[i] != 0:
        count += 1
        max_time = max(max_time, distance[i])

print(count, end= ' ')
print(max_time, end=' ')