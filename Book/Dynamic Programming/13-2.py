# Laboratory

n, m = map(int, input().split())

mapp = [[] for _ in range(m)]

virus = []
for i in range(n):
    array = list(map(int, input().split()))
    for j in range(m):
        if j == 2:
            virus.append((i, j))
    mapp[i].append(array)

def infection():
    for 