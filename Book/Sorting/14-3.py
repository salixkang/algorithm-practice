# failure
# https://programmers.co.kr/learn/courses/30/lessons/42889

# def solution(N, stages):
#     answer = []
#     stages.sort()
#     temp = []
#     n = 1
#     i = 0
#     failure = []
#     num = len(stages)
#     while n != N + 1:
#         if n != stages[i]:
#             if not temp:
#                 failure.append((n, 0))
#                 n += 1
#             else:
#                 failure.append((temp[0][0], ((i-temp[0][1])/(num-temp[0][1]))))
#                 temp = []
#                 n += 1
#         else:
#             if not temp:
#                 if i == num - 1:
#                     failure.append((n, 1))
#                     break
#                 temp.append((n, i))
#                 i += 1
#             else:
#                 if i == num-1:
#                     failure.append((temp[0][0], ((i-temp[0][1]-1)/(num-temp[0][1]))))
#                     temp = []
#                     n += 1
#                 else:
#                     i += 1
#                     continue
#
#     failure.sort(key=lambda x: (-x[1], x[0]))
#     for e in failure:
#         answer.append(e[0])
#
#     return answer

def solution(N, stages):
    answer = []
    num = len(stages)
    failure = []
    last_cnt = 0
    for n in range(1, N + 1):
        if n not in stages:
            failure.append((n, 0))
        else:
            cnt = stages.count(n)
            failure.append((n, cnt/(num-last_cnt)))
            last_cnt += cnt

    failure.sort(key = lambda x : (-x[1], x[0]))
    for stage, fail in failure:
        answer.append(stage)

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(3, [2, 2, 2, 2, 2]))