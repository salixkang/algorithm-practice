# cutting

# def cutting(array, target, start, end):
#     mid = (start + end) // 2
#     give = sum(array[0:mid + 1]) - (array[mid] * (mid+1))
#     if give == target:
#         return array[mid]
#     elif give > target:
#         return cutting(array, target, start, mid-1)
#     else :
#         return cutting(array, target, mid+1, end)

n, m = map(int, input().split())

array = list(map(int, input().split()))

result = 0

array.sort(reverse=True)

start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array :
        if x > mid :
            total += x - mid

    if total < m :
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

