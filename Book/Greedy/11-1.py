# Hunter Guild

n = int(input())

fear = list(map(int, input().split()))

fear.sort()

result = 0

i = 0
store = 0
# 1 2 2 2 3 3 4
while i <= (n - 1):
    num = fear[i]
    i += num - 1 - store
    if i >= n : break
    if fear[i] <= num:
        result += 1
        i += 1
        store = 0
        continue
    else : #fear [i] > num
        store += num - 1
        continue

print(result)
