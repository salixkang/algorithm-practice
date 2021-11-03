# gold
# dp 로 한번 더 풀어보기

from collections import deque

dx = [1, 1, 1]
dy = [-1, 0, 1]


t = int(input())
test = [[] for _ in range(t)]
for i in range(t):
    test[i].append(list(map(int, input().split())))
    test[i].append(list(map(int, input().split())))

test_num = 0
result = [] * t
while test_num in range(t):
    n, m = test[test_num][0]
    gold = test[test_num][1]
    gold_map = [gold[i * m:(i + 1) * m] for i in range(n)]
    test_result = 0
    for i in range(n):
        start_x = 0
        start_y = i
        start_g = gold_map[start_y][start_x]
        res = 0
        queue = deque()
        queue.append([start_x, start_y, start_g])
        while queue:
            now_x, now_y, now_g = queue.popleft()
            if now_x == m-1:
                res = max(res, now_g)
                continue
            for d in range(3):
                next_x , next_y = now_x + dx[d], now_y + dy[d]
                if next_x not in range(m) or next_y not in range(n):
                    continue
                next_g = gold_map[next_y][next_x]
                queue.append([next_x, next_y, now_g + next_g])

        test_result = max(test_result, res)
    print(test_result)

    test_num += 1
