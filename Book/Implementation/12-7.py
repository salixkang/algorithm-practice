# chicken delivery

from itertools import combinations

# import heapq
# from collections import deque
#
# n, m = map(int, input().split())
#
# city = [[0] for _ in range(n + 1)]
#
# chicken = []
#
# house = []
#
# for i in range(1, n + 1):
#     info = list(map(int, input().split()))
#     for j in range(n):
#         if info[j] == 2:
#             chicken.append((i, j + 1))
#         elif info[j] == 1:
#             house.append((i, j + 1))
#     city[i].append(info)
#
# dist = []
#
#
# for i in range(len(house)):
#     r, c = house[i]
#     for j in range(len(chicken)):
#         a, b = chicken[j]
#         res = abs(r-a) + abs(c-b)
#
#         heapq.heappush(dist, (res, i, j))
#
# while heapq:
#     res, h, c = heapq.heappop(dist)
#

n, m = map(int, input().split())

chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9

for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)