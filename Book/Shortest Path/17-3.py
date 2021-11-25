# mars

import heapq


def dijkstra(start, n, space):
    q = []
    heapq.heappush(q, (space[0][0], start))
    dp = [[1e9] * n for _ in range(n)]
    while q:
        cost, (x, y) = heapq.heappop(q)
        if dp[x][y] < cost:
            continue
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                next_cost = cost + space[next_x][next_y]
                if next_cost < dp[next_x][next_y]:
                    dp[next_x][next_y] = next_cost
                    heapq.heappush(q, (next_cost, (next_x, next_y)))

    return dp[n - 1][n - 1]

t = int(input())

test = [[] for _ in range(t)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(t):
    test[i].append(int(input()))
    n = test[i][0]
    cost = [[] for _ in range(n)]
    for j in range(n):
        cost[j] = list(map(int, input().split()))

    test[i].append(cost)

for i in range(t):
    n = test[i][0]
    space = test[i][1]
    start = (0, 0)
    result = dijkstra(start, n, space)





    print(result)



#
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
