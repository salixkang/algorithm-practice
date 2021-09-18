# Bowling ball

n, m = map(int, input().split())

weight = list(map(int, input().split()))

result = 0
for i in range(n):
    a = weight[i]
    for j in range(i+1, n):
        b = weight[j]
        if a != b:
            result += 1


print(result)