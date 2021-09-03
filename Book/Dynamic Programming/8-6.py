# ant warrior

n = int(input())

k = list(map(int, input().split()))

# d = [0] * 101
# check = [False] * 101
#
# d[1] = k[0]
#
# if k[1] > d[1]:
#     d[2] = k[1]
#     check[2] = True
# else:
#     d[2] = d[1]
#
# for i in range(3, n + 1):
#     if check[i-1] == True and (d[i-1] >= d[i-2] + k[i-1]) :
#         d[i] = d[i-1]
#     elif check[i-1] == True and (d[i-1] < d[i-2] + k[i-1]):
#         d[i] = d[i-2] + k[i-1]
#         check[i] = True
#     elif check[i-1] == False:
#         d[i] = d[i-1] + k[i-1]
#         check[i] = True
#     else :
#         print("error")

d = [0] * 100

d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])




print(d[n-1])

