# journey plan

n, m = map(int, input().split())

go = [[] for _ in range(n)]
back = [[] for _ in range(n)]


for i in range(n):
    a, b = map(int, input().split())
    go[a].append(b)
    back[b].append(a)

plan = list(map(int, input().split()))
res = 1
for idx, e in enumerate(plan):
    if plan[idx + 1] not in go[e] and plan[idx + 1] not in back[e]:
        print("NO")
        res = 0
        break

if res == 1:
    print("YES")