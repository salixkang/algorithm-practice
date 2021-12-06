# plannet tunnel
# https://www.acmicpc.net/problem/2887

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def cost(A, B):
    return min(abs(A[0] - B[0]), abs(A[1] - B[1]), abs(A[2] - B[2]))


n = int(input())

planet = [[] for _ in range(n)]

for i in range(n):
    x, y, z = map(int, input().split())
    planet[i] = (x, y, z)

parent = [] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i



