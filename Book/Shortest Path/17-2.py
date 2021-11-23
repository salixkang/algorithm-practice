# rank

from collections import deque

n, m = map(int, input().split())

comp = [[] for _ in range(m)]

for i in range(m):
    comp[i] = list(map(int, input().split()))

go = [[] for _ in range(n + 1)]
back = [[] for _ in range(n + 1)]

for a, b in comp:
    go[a].append(b)
    back[b].append(a)

rank = [set([]) for _ in range(n + 1)]


for i in range(1, n + 1):
    q = deque()
    q.append(i)
    while q:
        now = q.popleft()
        rank[i].add(now)
        for e in go[now]:
            q.append(e)

    q.append(i)
    while q:
        now = q.popleft()
        rank[i].add(now)
        for e in back[now]:
            q.append(e)

result = 0
for e in rank:
    if len(e) == n:
        result += 1

print(result)
