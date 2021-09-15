# curriculum

from collections import deque
import copy

v = int(input())

# lec_time = [0] * (v + 1) # lecture time
# graph = [[] for _ in range(v + 1)] # nodes related by directing arrow
# forward = [[] for _ in range(v + 1)] # nodes related by directed arrow
# indegree = [0] * (v + 1) # indegree
#
# for i in range(1, v + 1):
#     input_data = input().split()
#     for j in range(len(input_data)):
#         if j == 0: # first info is lecture time
#             lec_time[i] = int(input_data[j])
#             continue
#         curri = int(input_data[j])
#         if curri != -1:
#             graph[curri].append(i)
#             forward[i].append(curri)
#         elif curri == -1 :
#             break
#     indegree[i] = len(input_data) - 2
#
# def find_relation (forward, related, x):
#     if x not in related:
#         related = related + [x]
#     if not forward[x]:
#         return related
#     else:
#         for i in forward[x]:
#             related = find_relation(forward, related, i)
#         return related
#
# def solution (num):
#     result = 0
#     q = deque()
#     related = [num]
#     indegree_copy = indegree.copy()
#
#     related = find_relation(forward, related, num)
#     print(related)
#
#     related.sort()
#     for i in related:
#         if indegree_copy[i] == 0:
#             q.append(i)
#
#     while q:
#         now = q.popleft()
#         result += lec_time[now]
#         for i in graph[now]:
#             indegree_copy[i] -= 1
#             if indegree_copy[i] == 0 and i in related:
#                 q.append(i)
#
#     return result
#
# for i in range(1, v + 1):
#     print(solution(i))

indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]
time = [0] * (v + 1)

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1 : -1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])

topology_sort()
