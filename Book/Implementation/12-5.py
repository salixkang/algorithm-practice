# Snake

n = int(input())
k = int(input())

apple = []

for _ in range(k):
    a, b = map(int, input().split())
    apple.append((a, b))

l = int(input())
dir = []
for _ in range(l):
    x, c = input().split()
    dir.append((int(x), c))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


