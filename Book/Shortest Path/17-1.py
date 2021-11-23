# Floyd
# https://www.acmicpc.net/problem/11404

MAX = 1e9

n = int(input())

m = int(input())

buses = [[] for _ in range(m)]

for i in range(m):
    buses[i] = list(map(int, input().split()))

dp = [[MAX] * (n + 1) for _ in range(n + 1)]

for a, b, cost in buses:
    dp[a][b] = min(dp[a][b], cost)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                dp[a][b] = 0
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dp[i][j] == MAX:
            print("0", end = " ")
        else:
            print(dp[i][j], end = " ")
    print(end = "\n")