# finding goods by binary search

n = int(input())
goods = list(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

# def goods_search(goods, n, target):
#     index = 0
#     while index < n:
#         if goods[index] == target:
#             return index
#         else:
#             index += 1
#
#     return None
#
# for i in range(m):
#     if goods_search(goods, n, find[i]) == None:
#         print("no", end=' ')
#     else:
#         print("yes", end=' ')


goods.sort()

def binary_search(goods, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if goods[mid] == target:
        return mid
    elif goods[mid] < target:
        return binary_search(goods, target, mid+1, end)
    else :
        return binary_search(goods, target, start, mid-1)

for i in find:
    if binary_search(goods, i, 0, n-1) == None:
        print("no", end = ' ')
    else :
        print("yes", end = ' ')

