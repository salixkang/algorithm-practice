# population

from collections import deque

def make_union(row, col, num):
    union[row][col] = num
    sum_lst[num] += A[row][col]
    cnt_lst[num] += 1
    uni_lst[num].append((row, col))
    if row + 1 < n and l <= abs(A[row][col] - A[row + 1][col]) <= r and union[row + 1][col] == -1:
        make_union(row + 1, col, num)
    if col + 1 < n and l <= abs(A[row][col] - A[row][col + 1]) <= r and union[row][col + 1] == -1:
        make_union(row, col + 1, num)
    if row - 1 >= 0 and l <= abs(A[row][col] - A[row - 1][col]) <= r and union[row - 1][col] == -1:
        make_union(row - 1, col, num)
    if col - 1 >= 0 and l <= abs(A[row][col] - A[row][col - 1]) <= r and union[row][col - 1] == -1:
        make_union(row, col - 1, num)
    return 0

n, l, r = map(int, input().split())

A = [[] for _ in range(n)]

for i in range(n):
    A[i] = list(map(int, input().split()))


result = 0
while result <= 2000:
    union = [[-1] * n for _ in range(n)]
    uni_lst = [[] for _ in range(n * n)]
    sum_lst = [0] * (n * n)
    cnt_lst = [0] * (n * n)
    num = 0
    for row in range(n):
        for col in range(n):
            is_union = False
            if union[row][col] == -1:
                make_union(row, col, num)
                num += 1


    if num != n*n:
        for i in range(num):
            for x, y in uni_lst[i]:
                A[x][y] = sum_lst[i]//cnt_lst[i]
        result += 1
    else:
        break

print(result)


