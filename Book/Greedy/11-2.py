# multiply or addition

s = str(input())

lst = []

for e in s:
    e = int(e)
    if e != 0:
        lst.append(e)

lst.sort(reverse=True)

result = 0

for i in lst:
    result = max(result + i, result * i)

print(result)