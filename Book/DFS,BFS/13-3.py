# infection
import copy
from collections import deque

n, k = map(int, input().split())

tube = [[] for _ in range(n)]
virus = []
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if lst[j] != 0:
            virus.append((lst[j], (i, j)))
    tube[i] = lst

s, x, y = map(int, input().split())

virus.sort(key = lambda var:var[0])

queue = deque()

for vir in virus:
    queue.append(vir)

time = 0
for _ in range(s):
    next_queue = deque()
    while queue:
        now = queue.popleft()
        e = now[0]
        a, b = now[1][0], now[1][1]
        if a + 1 < n and tube[a+1][b] == 0:
            tube[a + 1][b] = e
            next_queue.append((e, (a + 1, b)))
        if a - 1 >= 0 and tube[a-1][b] == 0:
            tube[a - 1][b] = e
            next_queue.append((e, (a - 1, b)))
        if b + 1 < n and tube[a][b + 1] == 0:
            tube[a][b + 1] = e
            next_queue.append((e, (a, b + 1)))
        if b - 1 >= 0 and tube[a][b - 1] == 0:
            tube[a][b - 1] = e
            next_queue.append((e, (a, b - 1)))

    queue = copy.deepcopy(next_queue)

print(tube[x-1][y-1])

