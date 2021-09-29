# Exterior wall Inspection
# https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations

# def solution(n, weak, dist):
#     import heapq
#     answer = -1
#     dist.sort(reverse=True)
#
#     weak_dist = []
#
#     if len(weak) == 1:
#         return 1
#
#     if sum(dist) == len(dist):
#         return len(dist)
#
#     for i in range(len(weak)):
#         if i == len(weak) - 1:
#             weak_dist.append(weak[0] - weak[i] + n)
#         else:
#             weak_dist.append(weak[i + 1] - weak[i])
#
#     weak_dist.sort(reverse=True)
#
#     for i in range(1, len(weak_dist)):
#         if sum(weak_dist[i:]) <= sum(dist[:i]):
#             answer = i
#             break
#
#     return answer

def solution(n, weak, dist):
    length = len(weak) # 4
    for i in range(length): # weak x2
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            print(count)
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))