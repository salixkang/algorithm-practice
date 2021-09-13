# curriculum

from collections import deque

n = int(input())

lec_time = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    input_data = input().split()
    for j in range(len(input_data)):
        if j == 0:
            lec_time[i] = int(input_data[j])
            continue
        curri = int(input_data[j])
        if curri != -1:
            graph[curri].append(i)
        elif curri == -1 :
            break
    indegree[i] = len(input_data) - 2


def solution ():
    result = [0] * (n + 1)
    q = deque()

    for i in range(degree, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
        print


