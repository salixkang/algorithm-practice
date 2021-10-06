# surveillance

import itertools

n = int(input())

cor = [[] for _ in range(n)]
s = []
t = []
x = []
o = []
for i in range(n):
    lst = list(map(str, input().split()))
    for idx, ele in enumerate(lst):
        if ele == 'S':
            s.append((i, idx))
        elif ele == 'T':
            t.append((i, idx))
        elif ele == 'X':
            x.append((i, idx))
    cor[i].append(lst)

answer = 'NO'
for lst in list(itertools.combinations(x, 3)):
    for e in lst:
        o.append(e)
    watch = True
    for e in t:
        t_row, t_col = e
        for r, c in s:
            if r == t_row:
                watch = True
                if c < t_col - 1:
                    for i in range(c + 1, t_col):
                        if (r, i) in o:
                            watch = False
                            break
                elif c > t_col + 1:
                    for i in range(t_col + 1, c):
                        if (r, i) in o:
                            watch = False
                            break
            elif c == t_col:
                watch = True
                if r < t_row - 1:
                    for i in range(r + 1, t_row):
                        if (i, c) in o:
                            watch = False
                            break
                elif r > t_row + 1:
                    for i in range(t_row + 1, r):
                        if (i, c) in o:
                            watch = False
                            break
            else:
                watch = False
            if watch == True:
                break
        if watch == True:
            break
    if watch == False:
        answer = 'YES'
        break
    o.clear()

print(answer)



