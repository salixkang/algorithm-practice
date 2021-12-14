# rank
# https://www.acmicpc.net/problem/3665

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    team = list(map(int, input().split()))
    m = int(input())
    chg = [[] for _ in range(m)]
    for i in range(m):
        a, b = map(int, input().split())
        chg[i] = (a, b)

    indegree = [0] * (n + 1)
    rank = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            rank[team[i]].append(team[j])
            indegree[team[j]] += 1
    for (a, b) in chg:
        if a in rank[b]:
            rank[b].remove(a)
            indegree[a] -= 1
            rank[a].append(b)
            indegree[b] += 1
        elif b in rank[a]:
            rank[a].remove(b)
            indegree[b] -= 1
            rank[b].append(a)
            indegree[a] += 1

    q = deque()
    result = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    cycle = False
    certain = True
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)
        for k in rank[now]:
            indegree[k] -= 1
            if indegree[k] == 0:
                q.append(k)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()



