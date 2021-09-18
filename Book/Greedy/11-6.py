# broadcasting


def solution(food_times, k):
# import heapq

#     if sum(food_times) <= k:
#         return -1

#     q = []
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i + 1))

#     sum_value = 0
#     previous = 0
#     length = len(food_times)

#     while sum_value + ((q[0][0] - previous) * length) <= k :
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1
#         previous = now

#     answer = sorted(q, key = lambda x : x[1])

#     return answer[(k - sum_value) % length][1]

