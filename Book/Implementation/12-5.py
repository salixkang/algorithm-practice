# Snake

from collections import deque


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
dir.append((10000, 'L'))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

d = 0
snake_head = [1, 1]
snake_tail = deque([(1, 0)])

time = 0

for i in dir:
    x, c = i[0], i[1]
    answer = 0
    while time < x:
        snake_head[0] += dy[d]
        snake_head[1] += dx[d]
        time += 1
        if snake_head[0] < 1 or snake_head[0] > n or snake_head[1] < 1 or snake_head[1] > n or (snake_head[0], snake_head[1]) in snake_tail:
            answer = 1
            break

        snake_tail.append((snake_head[0], snake_head[1]))

        if (snake_head[0], snake_head[1]) not in apple:
            snake_tail.popleft()

    if answer == 1:
        print(time)
        break

    if c == 'L':
        d -= 1
    elif c == 'D' :
        d += 1
