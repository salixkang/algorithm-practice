# number card game

n, m = map(int, input().split())
data = [[0]*m for _ in range(n)]
result = [0]*n
for i in range(n):
    data[i] = list(map(int, input().split()))
    data[i].sort()
    result[i] = data[i][0]

result.sort()
print(result[n-1])



