# number triangle
# https://www.acmicpc.net/problem/1932

n = int(input())
triangle = [[] for _ in range(n)]

for i in range(n):
    triangle[i] = list(map(int, input().split()))

# dp[i][j] = triangle[i][j] + max[dp[i+1][j], dp[i+1][j + 1]]
dp = [[0] * n for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(i, -1, -1):
        if i + 1 >= n:
            dp[i][j] = triangle[i][j]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])
