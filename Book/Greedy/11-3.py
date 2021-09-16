# reverse string

s = str(input())

result = [0, 0]
check = int(s[0])
result[check] += 1
for e in s[1:-1]:
    e = int(e)
    if check != e:
        result[e] += 1
        check = e

print(min(result[0], result[1]))