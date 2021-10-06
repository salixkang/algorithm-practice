# operation

import itertools


n = int(input())
seq = list(map(int, input().split()))
opr = []

array = list(map(int, input().split()))

for idx, var in enumerate(array):
    for _ in range(var):
        opr.append(idx)

mx = -1e9
mn = 1e9
for i in list(itertools.permutations(opr)):
    temp = seq[0]
    idx = 1
    for j in i:
        if j == 0:
            temp = temp + seq[idx]
            idx += 1
            continue
        elif j == 1:
            temp = temp - seq[idx]
            idx += 1
            continue
        elif j == 2:
            temp = temp * seq[idx]
            idx += 1
            continue
        elif j == 3:
            if temp < 0:
                temp = -(-temp//seq[idx])
            else:
                temp = temp//seq[idx]
            idx += 1
            continue
    mx = max(mx, temp)
    mn = min(mn, temp)

print(mx)
print(mn)