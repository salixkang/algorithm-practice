# Lock and Key
# https://programmers.co.kr/learn/courses/30/lessons/60059

def solution(key, lock):
    answer = True

    lock_hole = []

    find_zero = 0

    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if lock[i][j] == 0:
                find_zero += 1
                lock_hole.append([i, j])
    if find_zero == 0:
        return True
    key_mount = []
    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j] == 1:
                key_mount.append([i, j])

    if len(key_mount) < len(lock_hole):
        return False

    # dx = [0, 0, -1, 1] # 상 하 좌 우
    # dy = [-1, 1, 0, 0]

    m = len(key)
    n = len(lock)

    for d in range(4):
        for k in key_mount:
            k[0], k[1] = k[1], m - 1 - k[0]

        for i in key_mount:
            dx = lock_hole[0][1] - i[1]
            dy = lock_hole[0][0] - i[0]
            check = 0
            array = []
            for j in key_mount:
                temp = [j[0] + dy, j[1] + dx]
                if temp in lock_hole:
                    check += 1
                elif temp[0] < n and temp[1] < n and temp[0] >= 0 and temp[1] >= 0:
                    check = 0
                    break
            if check == len(lock_hole):
                return True

    return False
