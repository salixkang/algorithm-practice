# moving blocks
# https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solution(board):
    n = len(board)
    in_board = list(range(0, n))
    robot_a = (0, 0)
    robot_b = (0, 1)
    visited = []
    queue = deque()
    queue.append(({robot_a, robot_b}, 0))
    visited.append({robot_a, robot_b})
    while queue:
        pos, num = queue.popleft()
        now_a, now_b = pos
        a0, a1 = now_a
        b0, b1 = now_b
        if (n-1, n-1) in pos:
            return num

        for dx, dy in move:
            next_a = (a0 + dx, a1 + dy)
            next_b = (b0 + dx, b1 + dy)
            if next_a[0] in in_board and next_a[1] in in_board and next_b[0] in in_board and next_b[1] in in_board:
                if board[next_a[0]][next_a[1]] == 0 and board[next_b[0]][next_b[1]] == 0:
                    if {next_a, next_b} not in visited:
                        queue.append(({next_a, next_b}, num + 1))
                        visited.append({next_a, next_b})

        if a0 == b0:
            for i in [-1, 1]:
                if a0 + i in in_board and b0 + i in in_board and board[a0 + i][a1] == 0 and board[b0 + i][b1] == 0:
                    next_a_1 = now_a
                    next_b_1 = (a0 + i, a1)
                    next_a_2 = (b0 + i, b1)
                    next_b_2 = now_b
                    if {next_a_1, next_b_1} not in visited:
                        queue.append(({next_a_1, next_b_1}, num + 1))
                        visited.append({next_a_1, next_b_1})
                    if {next_a_2, next_b_2} not in visited:
                        queue.append(({next_a_2, next_b_2}, num + 1))
                        visited.append({next_a_2, next_b_2})

        elif a1 == b1:
            for i in [-1, 1]:
                if a1 + i in in_board and b1 + i in in_board and board[a0][a1 + i] == 0 and board[b0][b1 + i] == 0:
                    next_a_1 = now_a
                    next_b_1 = (a0, a1 + i)
                    next_a_2 = (b0, b1 + i)
                    next_b_2 = now_b
                    if {next_a_1, next_b_1} not in visited:
                        queue.append(({next_a_1, next_b_1}, num + 1))
                        visited.append({next_a_1, next_b_1})
                    if {next_a_2, next_b_2} not in visited:
                        queue.append(({next_a_2, next_b_2}, num + 1))
                        visited.append({next_a_2, next_b_2})
    return 0
#

# def solution(board):


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
