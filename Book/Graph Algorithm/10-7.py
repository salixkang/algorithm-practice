# Team Building

n, m = map(int, input().split())

calc = []
for i in range(m):
    num, a, b = map(int, input().split())
    calc.append((num, a, b))

parent = [0] * (n + 1)
for i in range(0, n + 1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent (parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def check_parent (parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        print("YES")
    else:
        print("NO")

for i in calc:
    if i[0] == 0:
        union_parent(parent, i[1], i[2])
    elif i[0] == 1:
        check_parent(parent, i[1], i[2])

