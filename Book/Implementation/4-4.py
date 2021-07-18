n, m = map(int, input().split())
a, b, d = map(int, input().split())

mymap = [[0]*n for _ in range(m)]

for i in range(m):
    mymap[i] = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
visit = list()
visit.append((a, b))
check = 0
count = 1

while True:
    if check == 0:
        for i in range(4):
            d = (d - 1) % 4
            next_a = a + dy[d]
            next_b = b + dx[d]
            if mymap[next_a][next_b] == 0 and visit.count((next_a, next_b)) == 0:
                a = next_a
                b = next_b
                visit.append((a, b))
                count += 1
                break
            if i == 3:
                check = 1
    else:
        next_a = a + dy[d-2]
        next_b = b + dx[d-2]
        if mymap[next_a][next_b] == 1:
            break
        else:
            a = next_a
            b = next_b
            check = 0

print(count)
for v in visit:
    print(v)