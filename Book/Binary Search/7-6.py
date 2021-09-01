# by counting sort

# n = int(input())
# goods = list(map(int, input().split()))
#
# m = int(input())
# find = list(map(int, input().split()))
#
# count = [0] * (max(goods) + 1)
#
# for i in range(n):
#     count[goods[i]] += 1
#
# for i in range(m):
#     if count[find[i]] == 0:
#         print("no", end = ' ')
#     else:
#         count[find[i]] -= 1
#         print("yes", end = ' ')

n = int(input())
goods = [0] * 1000001

for i in input().split():
    goods[int(i)] = 1

m = int(input())
find = list(map(int, input().split()))

for i in find:
    if goods[i] == 1:
        print('yes', end = ' ')
    else :
        print('no', end = ' ')
