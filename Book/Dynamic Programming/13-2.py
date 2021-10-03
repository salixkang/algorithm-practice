# Laboratory
import copy
import itertools
from collections import deque



n, m = map(int, input().split())

mapp = [[] for _ in range(n)]

virus = []
wall = 0
blank = []

for i in range(n):
    array = list(map(int, input().split()))
    for j in range(m):
        if array[j] == 2:
            virus.append((i, j))
        elif array[j] == 1:
            wall += 1
        elif array[j] == 0 :
            blank.append((i, j))
    mapp[i] = array

queue = deque()
mapp_copy = copy.deepcopy(mapp)

result = 0

for temp in list(itertools.combinations(blank, 3)):
    mapp[temp[0][0]][temp[0][1]] = 1
    mapp[temp[1][0]][temp[1][1]] = 1
    mapp[temp[2][0]][temp[2][1]] = 1
    infection = 0
    for vir in virus:
        queue.append(vir)
    while queue:
        now = queue.popleft()
        infection += 1
        a, b = now[0], now[1]
        if a + 1 < n:
            if mapp[a + 1][b] == 0:
                queue.append((a + 1, b))
                mapp[a+1][b] = 2
        if a - 1 >= 0:
            if mapp[a - 1][b] == 0:
                queue.append((a - 1, b))
                mapp[a - 1][b] = 2
        if b + 1 < m :
            if mapp[a][b + 1] == 0:
                queue.append((a, b + 1))
                mapp[a][b + 1] = 2
        if b - 1 >= 0:
            if mapp[a][b - 1] == 0:
                queue.append((a, b - 1))
                mapp[a][b - 1] = 2
    result_temp = n * m - infection - wall - 3

    result = max(result_temp, result)
    mapp = copy.deepcopy(mapp_copy)

print(result)