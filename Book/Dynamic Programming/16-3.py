# leave
# https://www.acmicpc.net/problem/14501

n = int(input())
plan = [[] for _ in range(n)]
for i in range(n):
    t, p = map(int, input().split())
    plan[i] = (t, p)

# dp[k] = max(plan[k][1] + dp[k + plan[k][0]], dp[k + 1])

dp = [0] * n

for k in range(n-1, -1, -1):
    if (k + plan[k][0]) > n:
        if k == n-1:
            dp[k] = 0
        else:
            dp[k] = dp[k + 1]
    elif (k + plan[k][0]) == n :
        if k == n-1:
            dp[k] =plan[k][1]
        else:
            dp[k] = max(plan[k][1], dp[k + 1])
    else:
        dp[k] = max(plan[k][1] + dp[k + plan[k][0]], dp[k + 1])

print(dp[0])