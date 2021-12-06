# dark road

import heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

road = []

for i in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(road, (z, (x, y)))

result = 0

while road:
    z, (x, y) = heapq.heappop(road)
    if sum(parent) == n:
        result += z
        continue
    if find_parent(parent, x) == find_parent(parent, y):
        result += z
        continue
    else:
        union_parent(parent, x, y)

print(result)

