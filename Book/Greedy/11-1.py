# Hunter Guild

n = int(input())

fear = list(map(int, input().split()))

fear.sort()

result = 0

i = 0
while i <= n:
    num = fear[i]
    i += num - 1
    if fear[i] <= num:
        result += 1
        i += 1
        continue
    else :

