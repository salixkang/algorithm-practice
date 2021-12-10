# plannet tunnel
# https://www.acmicpc.net/problem/2887

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

n = int(input())

planet = []

for i in range(n):
    x, y, z = map(int, input().split())
    planet.append((i, (x, y, z)))

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

dist = []

list_x = sorted(planet, key=lambda x:x[1][0])
list_y = sorted(planet, key=lambda x:x[1][1])
list_z = sorted(planet, key=lambda x:x[1][2])
list = [list_x, list_y, list_z]
for i in range(n - 1):
    for j in range(3):
        a = list[j][i]
        b = list[j][i + 1]
        heapq.heappush(dist, (abs(a[1][j] - b[1][j]), (a[0], b[0])))

result = 0
route = 0

while dist:
    cost, (a, b) = heapq.heappop(dist)
    if route == n - 1:
        break
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    union_parent(parent, a, b)
    result += cost
    route += 1

print(result)



