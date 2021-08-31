# array element swap

n, k = map(int, input().split())

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

# arrayA.sort()
# arrayB.sort()
#
# for i in range(k):
#     if arrayA[i] >= arrayB[n-i-1]:
#         break
#     else:
#         arrayA[i], arrayB[n-i-1] = arrayB[n-i-1], arrayA[i]
# result = 0
#
# for i in range(n):
#     result += arrayA[i]
#
# print(result)

arrayA.sort()
arrayB.sort(reverse=True)

for i in range(k):
    if arrayA[i] < arrayB[i]:
        arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
    else:
        break

print(sum(arrayA))
