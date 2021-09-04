# monetary composition

n, m = map(int, input().split())

d = [0] * 10001

money = []
for _ in range(n):
    money.append(int(input()))

money.sort(reverse=True)

for i in range(1, n+1):
    if i % money[0] == 0:
        d[i] = i//money[0]
    else:
