# hide and seek
import heapq

n, m = map(int, input().split())

go = [[] for _ in range(n + 1)]
back = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    go[a].append(b)
    back[b].append(a)

dist = [1e9] * (n + 1)

start = 1
dist[start] = 0
dist[0] = -1

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue

        for i in go[now]:
            next_cost = cost + 1
            if next_cost < dist[i]:
                dist[i] = next_cost
                heapq.heappush(q, (next_cost, i))

        for i in back[now]:
            next_cost = cost + 1
            if next_cost < dist[i]:
                dist[i] = next_cost
                heapq.heappush(q, (next_cost, i))



    return dist.index(max(dist))

idx = dijkstra(start)
print(idx, dist[idx], dist.count(dist[idx]))
